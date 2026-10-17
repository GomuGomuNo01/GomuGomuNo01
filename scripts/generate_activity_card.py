"""Génère les cartes d'activité GitHub (thèmes sombre et clair, palette Primer) à partir des données publiques réelles."""
import base64
import datetime as dt
import json
import math
import os
import sys
import urllib.request
from xml.sax.saxutils import escape

LOGIN = os.environ.get("GH_LOGIN", "GomuGomuNo01")
TOKEN = os.environ["GH_TOKEN"]
OUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "."

QUERY = """
query($login: String!) {
  user(login: $login) {
    name login createdAt avatarUrl
    repositories(privacy: PUBLIC, first: 100, orderBy: {field: PUSHED_AT, direction: DESC}) {
      totalCount
      nodes { name isFork pushedAt primaryLanguage { name } }
    }
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount weekday } }
      }
    }
  }
}
"""

LANG_COLORS = {
    "Python": "#3572A5", "JavaScript": "#f1e05a", "Jupyter Notebook": "#DA5B0B",
    "PHP": "#4F5D95", "Blade": "#f7523f", "HTML": "#e34c26", "Dart": "#00B4AB",
    "Java": "#b07219", "C#": "#178600", "TypeScript": "#3178c6", "CSS": "#663399",
}
MONTHS = ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."]

THEMES = {
    "dark": dict(bg="#0d1117", border="#30363d", divider="#21262d", text="#e6edf3", muted="#8b949e",
                 link="#58a6ff", green="#3fb950", tile="#161b22",
                 heat=["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]),
    "light": dict(bg="#ffffff", border="#d0d7de", divider="#d8dee4", text="#1f2328", muted="#656d76",
                  link="#0969da", green="#1a7f37", tile="#f6f8fa",
                  heat=["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"]),
}


def gql():
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode(),
        headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json", "User-Agent": "activity-card"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    if "errors" in data:
        raise SystemExit(data["errors"])
    return data["data"]["user"]


def avatar_b64(url):
    sep = "&" if "?" in url else "?"
    req = urllib.request.Request(f"{url}{sep}s=120", headers={"User-Agent": "activity-card"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return base64.b64encode(r.read()).decode()


def relative(pushed, now):
    days = (now.date() - pushed.date()).days
    if days <= 0:
        return "aujourd'hui"
    if days < 30:
        return f"il y a {days} j"
    return f"il y a {days // 30} mois"


def collect():
    u = gql()
    now = dt.datetime.now(dt.timezone.utc)
    cal = u["contributionsCollection"]["contributionCalendar"]
    days = [d for w in cal["weeks"] for d in w["contributionDays"]]
    today = now.date().isoformat()
    seq = [d for d in days if d["date"] <= today]

    streak, idx = 0, len(seq) - 1
    if idx >= 0 and seq[idx]["contributionCount"] == 0:
        idx -= 1
    while idx >= 0 and seq[idx]["contributionCount"] > 0:
        streak += 1
        idx -= 1
    best, run = 0, 0
    for d in seq:
        run = run + 1 if d["contributionCount"] > 0 else 0
        best = max(best, run)

    repos = u["repositories"]["nodes"]
    langs = {}
    for r in repos:
        if not r["isFork"] and r["primaryLanguage"]:
            n = r["primaryLanguage"]["name"]
            langs[n] = langs.get(n, 0) + 1
    ranked = sorted(langs.items(), key=lambda kv: -kv[1])
    total_l = sum(langs.values()) or 1
    top = ranked[:5]
    others = sum(c for _, c in ranked[5:])

    return dict(
        now=now, name=u["name"] or u["login"], login=u["login"], since=u["createdAt"][:4],
        avatar=avatar_b64(u["avatarUrl"]), weeks=cal["weeks"][-53:],
        total=cal["totalContributions"], active=sum(1 for d in days if d["contributionCount"] > 0),
        streak=streak, best=best, repos=u["repositories"]["totalCount"],
        top=top, others=others, total_l=total_l, recent=repos[:3],
    )


def build(t, c):
    W, H = 900, 470
    out = []
    a = out.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
      f'aria-label="Activité GitHub de {escape(c["name"])} : {c["total"]} contributions publiques sur 12 mois">')
    a(f"""<style>
      .sans{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif}}
      .mono{{font-family:ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace}}
      .cell{{opacity:0;animation:pop .45s ease-out forwards}}
      @keyframes pop{{from{{opacity:0;transform:scale(.3)}}to{{opacity:1;transform:scale(1)}}}}
    </style>""")
    a(f'<clipPath id="av"><circle cx="64" cy="40" r="20"/></clipPath>')
    a(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="6" fill="{t["bg"]}" stroke="{t["border"]}"/>')

    a(f'<circle cx="64" cy="40" r="21" fill="none" stroke="{t["border"]}"/>')
    a(f'<image href="data:image/jpeg;base64,{c["avatar"]}" x="44" y="20" width="40" height="40" clip-path="url(#av)" preserveAspectRatio="xMidYMid slice"/>')
    a(f'<text x="98" y="36" class="sans" font-size="16" font-weight="600" fill="{t["text"]}">{escape(c["name"])}</text>')
    a(f'<text x="98" y="55" class="sans" font-size="12.5" fill="{t["muted"]}">@{escape(c["login"])} · sur GitHub depuis {c["since"]}</text>')
    a(f'<text x="{W-44}" y="38" class="sans" font-size="26" font-weight="600" fill="{t["green"]}" text-anchor="end">{c["total"]}</text>')
    a(f'<text x="{W-44}" y="56" class="sans" font-size="12.5" fill="{t["muted"]}" text-anchor="end">contributions publiques sur les 12 derniers mois</text>')
    a(f'<path d="M0 78 H{W}" stroke="{t["divider"]}"/>')

    gx, gy, cs, step = 84, 122, 12, 14.5
    peak = max((d["contributionCount"] for w in c["weeks"] for d in w["contributionDays"]), default=1) or 1
    for row, label in ((1, "Lun"), (3, "Mer"), (5, "Ven")):
        a(f'<text x="44" y="{gy + row*step + 10}" class="sans" font-size="11" fill="{t["muted"]}">{label}</text>')
    last_month = None
    for ci, w in enumerate(c["weeks"]):
        first = dt.date.fromisoformat(w["contributionDays"][0]["date"])
        if first.month != last_month and ci < len(c["weeks"]) - 2:
            a(f'<text x="{gx + ci*step}" y="{gy-12}" class="sans" font-size="11" fill="{t["muted"]}">{MONTHS[first.month-1]}</text>')
            last_month = first.month
        for d in w["contributionDays"]:
            n = d["contributionCount"]
            lvl = 0 if n == 0 else max(1, min(4, math.ceil(n / peak * 4)))
            x, y = gx + ci * step, gy + d["weekday"] * step
            a(f'<rect class="cell" style="animation-delay:{ci*0.03:.2f}s;transform-origin:{x+cs/2}px {y+cs/2}px" '
              f'x="{x:.1f}" y="{y:.1f}" width="{cs}" height="{cs}" rx="2" fill="{t["heat"][lvl]}">'
              f'<title>{d["date"]} : {n} contribution{"s" if n > 1 else ""}</title></rect>')

    ly = gy + 7 * step + 6
    a(f'<text x="{W-44-5*15-34}" y="{ly+10}" class="sans" font-size="11" fill="{t["muted"]}" text-anchor="end">Moins</text>')
    for i, col in enumerate(t["heat"]):
        a(f'<rect x="{W-44-5*15-28+i*15}" y="{ly}" width="{cs}" height="{cs}" rx="2" fill="{col}"/>')
    a(f'<text x="{W-44}" y="{ly+10}" class="sans" font-size="11" fill="{t["muted"]}" text-anchor="end">Plus</text>')

    ty = ly + 34
    a(f'<path d="M0 {ty-12} H{W}" stroke="{t["divider"]}"/>')
    stats = [(c["total"], "Contributions"), (c["active"], "Jours actifs"), (f'{c["streak"]} j', "Série en cours"),
             (f'{c["best"]} j', "Meilleure série"), (c["repos"], "Dépôts publics")]
    cw = (W - 88) / len(stats)
    for i, (v, lab) in enumerate(stats):
        x = 44 + i * cw
        if i:
            a(f'<path d="M{x-12:.1f} {ty+4} V{ty+50}" stroke="{t["divider"]}"/>')
        a(f'<text x="{x:.1f}" y="{ty+28}" class="sans" font-size="26" font-weight="600" fill="{t["text"]}">{v}</text>')
        a(f'<text x="{x:.1f}" y="{ty+48}" class="sans" font-size="12.5" fill="{t["muted"]}">{lab}</text>')

    by = ty + 78
    a(f'<path d="M0 {by-12} H{W}" stroke="{t["divider"]}"/>')
    a(f'<text x="44" y="{by+12}" class="sans" font-size="13" font-weight="600" fill="{t["text"]}">Langages</text>')
    bw, x = 380, 44.0
    segs = [(n, cnt) for n, cnt in c["top"]] + ([("Autres", c["others"])] if c["others"] else [])
    a(f'<clipPath id="bar"><rect x="44" y="{by+24}" width="{bw}" height="8" rx="4"/></clipPath><g clip-path="url(#bar)">')
    for n, cnt in segs:
        w_ = bw * cnt / c["total_l"]
        a(f'<rect x="{x:.1f}" y="{by+24}" width="{w_:.1f}" height="8" fill="{LANG_COLORS.get(n, "#8b949e")}"/>')
        x += w_
    a("</g>")
    for i, (n, cnt) in enumerate(segs):
        col, row = i % 2, i // 2
        lx, ly2 = 44 + col * 195, by + 56 + row * 22
        a(f'<circle cx="{lx+5}" cy="{ly2-4}" r="5" fill="{LANG_COLORS.get(n, "#8b949e")}"/>')
        a(f'<text x="{lx+16}" y="{ly2}" class="sans" font-size="12.5" fill="{t["text"]}" font-weight="600">{escape(n)}</text>')
        a(f'<text x="{lx+16+len(n)*7.1+8:.0f}" y="{ly2}" class="sans" font-size="12.5" fill="{t["muted"]}">{round(100*cnt/c["total_l"])} %</text>')

    rx = 500
    a(f'<text x="{rx}" y="{by+12}" class="sans" font-size="13" font-weight="600" fill="{t["text"]}">Activité récente</text>')
    for i, r in enumerate(c["recent"]):
        y = by + 44 + i * 30
        a(f'<path d="M{rx} {y-12} H{W-44}" stroke="{t["divider"]}"/>' if i else "")
        a(f'<rect x="{rx}" y="{y-9}" width="12" height="14" rx="2" fill="none" stroke="{t["muted"]}" stroke-width="1.4"/>')
        a(f'<text x="{rx+22}" y="{y+2}" class="sans" font-size="13.5" font-weight="600" fill="{t["link"]}">{escape(r["name"])}</text>')
        pushed = dt.datetime.fromisoformat(r["pushedAt"].replace("Z", "+00:00"))
        a(f'<text x="{W-44}" y="{y+2}" class="sans" font-size="12.5" fill="{t["muted"]}" text-anchor="end">{relative(pushed, c["now"])}</text>')

    a("</svg>")
    return "\n".join(out)


def main():
    c = collect()
    os.makedirs(OUT_DIR, exist_ok=True)
    for name, theme in THEMES.items():
        path = os.path.join(OUT_DIR, f"activity-card-{name}.svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(build(theme, c))
        print(f"OK {path}")
    print(f"total={c['total']} actifs={c['active']} serie={c['streak']} meilleure={c['best']} depots={c['repos']}")


main()
