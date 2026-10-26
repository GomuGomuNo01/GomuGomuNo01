"""Génère les SVG animés statiques du profil : bandeau de technologies et séparateur."""
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "assets")

ROW1 = [("Python", "#3776AB"), ("pandas", "#150458"), ("NumPy", "#013243"), ("SQL", "#336791"),
        ("Power BI", "#F2C811"), ("DAX", "#E8A33D"), ("Power Query", "#217346"), ("PySpark", "#E25A1C"),
        ("DuckDB", "#FFF000"), ("scikit-learn", "#F7931E"), ("XGBoost", "#1F6FB2"), ("Jupyter", "#F37626"),
        ("Streamlit", "#FF4B4B"), ("LangChain", "#1C3C3C"), ("FAISS", "#0467DF"), ("API Claude", "#D97757"),
        ("Claude Code", "#C2410C"), ("MCP", "#6D28D9")]
ROW2 = [("React", "#61DAFB"), ("TypeScript", "#3178C6"), ("Tailwind CSS", "#06B6D4"), ("Vite", "#646CFF"),
        ("FastAPI", "#009688"), ("Laravel", "#FF2D20"), ("PHP", "#777BB4"), ("Java", "#ED8B00"),
        ("Spring Boot", "#6DB33F"), ("C#", "#512BD4"), ("ASP.NET Core", "#5C2D91"), ("MySQL", "#4479A1"),
        ("PostgreSQL", "#336791"), ("SQLite", "#003B57"), ("Selenium", "#43B02A"), ("Playwright", "#2EAD33"), ("n8n", "#EA4B71"), ("Airtable", "#18BFFF"),
        ("pytest", "#0A9EDC"), ("Docker", "#2496ED"), ("GitHub Actions", "#2088FF"), ("Git", "#F05032")]


def text_color(hex_):
    r, g, b = (int(hex_[i:i + 2], 16) for i in (1, 3, 5))
    return "#111111" if (0.299 * r + 0.587 * g + 0.114 * b) > 165 else "#ffffff"


def pills(items, y):
    out, x = [], 0.0
    for name, col in items:
        w = 26 + len(name) * 7.6
        out.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="32" rx="16" fill="{col}"/>'
                   f'<text x="{x + w / 2:.1f}" y="{y + 21}" text-anchor="middle" font-size="13.5" font-weight="600" '
                   f'fill="{text_color(col)}">{name.replace("&", "&amp;")}</text>')
        x += w + 12
    return "".join(out), x


def marquee():
    W, H = 1000, 96
    r1, w1 = pills(ROW1, 6)
    r2, w2 = pills(ROW2, 56)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Technologies : {', '.join(n for n, _ in ROW1 + ROW2)}">
  <defs>
    <linearGradient id="fade" x1="0" x2="1">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".08" stop-color="#fff"/>
      <stop offset=".92" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <mask id="m"><rect width="{W}" height="{H}" fill="url(#fade)"/></mask>
  </defs>
  <style>
    text{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif}}
    .l{{animation:l 38s linear infinite}} .r{{animation:r 42s linear infinite}}
    @keyframes l{{from{{transform:translateX(0)}}to{{transform:translateX(-{w1:.1f}px)}}}}
    @keyframes r{{from{{transform:translateX(-{w2:.1f}px)}}to{{transform:translateX(0)}}}}
  </style>
  <g mask="url(#m)">
    <g class="l"><g>{r1}</g><g transform="translate({w1:.1f},0)">{r1}</g></g>
    <g class="r"><g>{r2}</g><g transform="translate({w2:.1f},0)">{r2}</g></g>
  </g>
</svg>
"""


def divider():
    return """<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="8" viewBox="0 0 1000 8" preserveAspectRatio="none" role="presentation">
  <defs>
    <linearGradient id="g" x1="0" x2="1">
      <stop offset="0" stop-color="#58a6ff" stop-opacity="0"/>
      <stop offset=".5" stop-color="#e94560"/>
      <stop offset="1" stop-color="#58a6ff" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>.s{animation:s 4.5s ease-in-out infinite}@keyframes s{from{transform:translateX(-320px)}to{transform:translateX(1000px)}}</style>
  <rect y="3.5" width="1000" height="1" fill="#8b949e" fill-opacity=".35"/>
  <rect class="s" y="2.5" width="320" height="3" rx="1.5" fill="url(#g)"/>
</svg>
"""


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, content in (("tech-marquee.svg", marquee()), ("divider.svg", divider())):
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(content)
        print("OK", name)
