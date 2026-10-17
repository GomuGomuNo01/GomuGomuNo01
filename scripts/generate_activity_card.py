"""Génère activity-card.svg : carte d'activité GitHub (style terminal) à partir des données publiques réelles."""
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
OUT = sys.argv[1] if len(sys.argv) > 1 else "activity-card.svg"

QUERY = """
query($login: String!) {
  user(login: $login) {
    name login location createdAt avatarUrl
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
HEAT = ["#1c1917", "#5a2d1c", "#9a4524", "#d45a28", "#ff7a3d"]


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
    with urllib.request.urlopen(urllib.request.Request(f"{url}{sep}s=120", headers={"User-Agent": "activity-card"}), timeout=30) as r:
        return base64.b64encode(r.read()).decode()


def relative(pushed, now):
    days = (now.date() - pushed.date()).days
    if days <= 0:
        return "aujourd'hui"
    if days < 30:
        return f"il y a {days} j"
    return f"il y a {days // 30} mois"


def main():
    u = gql()
    now = dt.datetime.now(dt.timezone.utc)
    cal = u["contributionsCollection"]["contributionCalendar"]
    days = [d for w in cal["weeks"] for d in w["contributionDays"]]
    total = cal["totalContributions"]
    active = sum(1 for d in days if d["contributionCount"] > 0)

    today = now.date().isoformat()
    seq = [d for d in days if d["date"] <= today]
    streak, idx = 0, len(seq) - 1
    if idx >= 0 and seq[idx]["contributionCount"] == 0:
        idx -= 1
    while idx >= 0 and seq[idx]["contributionCount"] > 0:
        streak += 1
        idx -= 1

    weeks = cal["weeks"][-26:]
    peak = max((d["contributionCount"] for w in weeks for d in w["contributionDays"]), default=1) or 1

    repos = u["repositories"]["nodes"]
    own = [r for r in repos if not r["isFork"]]
    langs = {}
    for r in own:
        if r["primaryLanguage"]:
            langs[r["primaryLanguage"]["name"]] = langs.get(r["primaryLanguage"]["name"], 0) + 1
    top_langs = sorted(langs.items(), key=lambda kv: -kv[1])[:5]
    lang_total = sum(c for _, c in top_langs) or 1
    recent = [r for r in repos][:3]

    W, H = 640, 640
    name = escape(u["name"] or u["login"])
    since = u["createdAt"][:4]
    city = escape((u["location"] or "").split(",")[0].strip())
    meta = f"@{escape(u['login'])}" + (f" · {city}" if city else "") + f" · sur GitHub depuis {since}"

    out = []
    a = out.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Activité GitHub de {name}">')
    a("""<style>
      .mono{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}
      .sans{font-family:'Segoe UI',Helvetica,Arial,sans-serif}
      .cell{opacity:0;animation:pop .5s ease-out forwards}
      @keyframes pop{from{opacity:0;transform:scale(.4)}to{opacity:1;transform:scale(1)}}
      .cur{animation:blink 1s steps(1) infinite}
      @keyframes blink{50%{opacity:0}}
      .live{animation:pulse 1.8s ease-in-out infinite}
      @keyframes pulse{50%{opacity:.25}}
    </style>""")
    a(f'<clipPath id="av"><circle cx="70" cy="98" r="26"/></clipPath>')
    a(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="#0b0b0c" stroke="#262626"/>')
    a(f'<path d="M1 36 H{W-1}" stroke="#1f1f1f"/>')
    for i, c in enumerate(("#ff5f57", "#ffbd2e", "#28c840")):
        a(f'<circle cx="{26+i*18}" cy="18" r="5.5" fill="{c}"/>')
    a(f'<text x="{W/2}" y="22" text-anchor="middle" class="mono" font-size="12" fill="#6b6b6b" letter-spacing="1.5">github.com/{escape(u["login"].lower())}</text>')
    a(f'<circle cx="{W-86}" cy="18" r="3.5" fill="#28c840" class="live"/><text x="{W-76}" y="22" class="mono" font-size="11" fill="#28c840" letter-spacing="1.5">LIVE</text>')

    a(f'<circle cx="70" cy="98" r="28" fill="none" stroke="#ff7a3d" stroke-opacity=".6" stroke-width="2"/>')
    a(f'<image href="data:image/jpeg;base64,{avatar_b64(u["avatarUrl"])}" x="44" y="72" width="52" height="52" clip-path="url(#av)" preserveAspectRatio="xMidYMid slice"/>')
    a(f'<text x="112" y="92" class="sans" font-size="21" font-weight="700" fill="#f4f4f4">{name}</text>')
    a(f'<text x="112" y="114" class="sans" font-size="12.5" fill="#8a8a8a">{meta}</text>')
    a(f'<rect x="{W-146}" y="80" width="104" height="34" rx="17" fill="none" stroke="#ff7a3d" stroke-opacity=".7"/>')
    a(f'<text x="{W-94}" y="102" text-anchor="middle" class="mono" font-size="11.5" fill="#ff7a3d" letter-spacing="1.5">PROFIL ↗</text>')

    a(f'<text x="44" y="158" class="mono" font-size="13" fill="#d8d8d8"><tspan fill="#ff7a3d">$</tspan> git log --since="6 months" --author=cedric<tspan class="cur" fill="#ff7a3d">▌</tspan></text>')

    gx, gy, cs, gap = 44, 214, 16, 4
    last_month = None
    for ci, w in enumerate(weeks):
        first = dt.date.fromisoformat(w["contributionDays"][0]["date"])
        if first.month != last_month:
            a(f'<text x="{gx+ci*(cs+gap)}" y="{gy-12}" class="sans" font-size="11" fill="#6b6b6b">{MONTHS[first.month-1]}</text>')
            last_month = first.month
        for d in w["contributionDays"]:
            n = d["contributionCount"]
            lvl = 0 if n == 0 else max(1, min(4, math.ceil(n / peak * 4)))
            x, y = gx + ci * (cs + gap), gy + d["weekday"] * (cs + gap)
            delay = (ci * 0.035)
            a(f'<rect class="cell" style="animation-delay:{delay:.2f}s;transform-origin:{x+cs/2}px {y+cs/2}px" x="{x}" y="{y}" width="{cs}" height="{cs}" rx="3" fill="{HEAT[lvl]}"><title>{d["date"]} : {n}</title></rect>')

    ly = gy + 7 * (cs + gap) + 8
    a(f'<text x="{W-44-5*14-44}" y="{ly+10}" class="sans" font-size="11" fill="#6b6b6b" text-anchor="end">moins</text>')
    for i, c in enumerate(HEAT):
        a(f'<rect x="{W-44-5*14-36+i*14}" y="{ly}" width="11" height="11" rx="2" fill="{c}"/>')
    a(f'<text x="{W-44}" y="{ly+10}" class="sans" font-size="11" fill="#6b6b6b" text-anchor="end">plus</text>')

    sy = ly + 40
    a(f'<path d="M44 {sy-18} H{W-44}" stroke="#1f1f1f"/>')
    stats = [(total, "CONTRIBUTIONS / 12 MOIS", "#ff7a3d"), (active, "JOURS ACTIFS", "#f4f4f4"),
             (f"{streak} j", "SÉRIE EN COURS", "#f4f4f4"), (u["repositories"]["totalCount"], "DÉPÔTS PUBLICS", "#f4f4f4")]
    for i, (v, lab, col) in enumerate(stats):
        x = [44, 232, 368, 494][i]
        a(f'<text x="{x}" y="{sy+22}" class="sans" font-size="28" font-weight="800" fill="{col}">{v}</text>')
        a(f'<text x="{x}" y="{sy+42}" class="mono" font-size="9.5" fill="#6b6b6b" letter-spacing="1">{lab}</text>')

    by = sy + 66
    a(f'<path d="M44 {by-14} H{W-44}" stroke="#1f1f1f"/>')
    x = 44
    bw = W - 88
    for i, (lg, c) in enumerate(top_langs):
        w_ = bw * c / lang_total
        col = LANG_COLORS.get(lg, "#8b949e")
        a(f'<rect x="{x:.1f}" y="{by}" width="{max(w_-2,2):.1f}" height="8" rx="4" fill="{col}"/>')
        x += w_
    lx = 44
    for lg, c in top_langs:
        col = LANG_COLORS.get(lg, "#8b949e")
        a(f'<circle cx="{lx+4}" cy="{by+30}" r="4" fill="{col}"/>')
        label = f"{escape(lg)} {c}"
        a(f'<text x="{lx+14}" y="{by+34}" class="sans" font-size="12" fill="#cfcfcf">{label}</text>')
        lx += 22 + len(label) * 6.6
    a(f'<text x="{W-44}" y="{by+34}" class="sans" font-size="11" fill="#6b6b6b" text-anchor="end">dépôts par langage</text>')

    ry = by + 72
    for i, r in enumerate(recent):
        y = ry + i * 26
        a(f'<circle cx="48" cy="{y-4}" r="3" fill="#28c840"/>')
        a(f'<text x="62" y="{y}" class="mono" font-size="13" font-weight="600" fill="#f0f0f0">{escape(r["name"])}</text>')
        lg = r["primaryLanguage"]["name"] if r["primaryLanguage"] else None
        if lg:
            tx = 398
            a(f'<circle cx="{tx}" cy="{y-4}" r="4" fill="{LANG_COLORS.get(lg, "#8b949e")}"/>')
            a(f'<text x="{tx+10}" y="{y}" class="sans" font-size="12" fill="#8a8a8a">{escape(lg)}</text>')
        pushed = dt.datetime.fromisoformat(r["pushedAt"].replace("Z", "+00:00"))
        a(f'<text x="{W-44}" y="{y}" class="sans" font-size="12" fill="#8a8a8a" text-anchor="end">{relative(pushed, now)}</text>')

    a("</svg>")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"OK {OUT}: total={total} actifs={active} serie={streak} depots={u['repositories']['totalCount']}")


main()
