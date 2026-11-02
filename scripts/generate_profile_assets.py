#!/usr/bin/env python3
"""Generate the light and dark SVG artwork used by the GitHub profile README."""

from __future__ import annotations

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"

PALETTES = {
    "light": {
        "canvas": "#F5F2EC",
        "canvas_alt": "#EDE7DD",
        "panel": "#FFFCF7",
        "text": "#1C1D1F",
        "muted": "#6F6B65",
        "faint": "#A59F96",
        "line": "#DCD5C9",
        "accent": "#B96B2E",
        "accent_soft": "#E8B47F",
    },
    "dark": {
        "canvas": "#111214",
        "canvas_alt": "#191A1E",
        "panel": "#17181C",
        "text": "#F5F0E7",
        "muted": "#A9A49C",
        "faint": "#77736C",
        "line": "#313238",
        "accent": "#E8A15E",
        "accent_soft": "#F3C08C",
    },
}

PROJECTS = [
    {
        "index": "01",
        "slug": "mole-gui",
        "eyebrow": "LOCAL-FIRST  /  MACOS",
        "title": "Mole GUI",
        "description": "A calmer interface for cleanup, disk analysis, and app uninstall.",
        "meta": "TAURI  ·  REACT  ·  TYPESCRIPT",
        "accent": "#D88947",
    },
    {
        "index": "02",
        "slug": "gridcraft",
        "eyebrow": "NATIVE SOFTWARE  /  RUST",
        "title": "GridCraft",
        "description": "A clean-room spreadsheet built from first principles in pure Rust.",
        "meta": "RUST  ·  DESKTOP  ·  OPEN SOURCE",
        "accent": "#6F9B88",
    },
    {
        "index": "03",
        "slug": "rea",
        "eyebrow": "DEVELOPER TOOLS  /  AGENTS",
        "title": "REA",
        "description": "Reverse engineer app behavior, binaries, and shipped artifacts with agents.",
        "meta": "TYPESCRIPT  ·  AGENTS  ·  REVERSE ENGINEERING",
        "accent": "#6F95B5",
    },
    {
        "index": "04",
        "slug": "sunny-ui-design-system",
        "eyebrow": "DESIGN SYSTEM  /  INTERFACE",
        "title": "Sunny UI",
        "description": "Color palettes, layered materials, and reusable React appearance controls.",
        "meta": "CSS  ·  REACT  ·  DESIGN STANDARDS",
        "accent": "#C77D69",
    },
    {
        "index": "05",
        "slug": "lancer",
        "eyebrow": "DESKTOP AI  /  WORKSPACE",
        "title": "Lancer",
        "description": "A focused desktop workspace for working with local AI agents.",
        "meta": "TYPESCRIPT  ·  DESKTOP  ·  AI WORKSPACE",
        "accent": "#B89A5C",
    },
    {
        "index": "06",
        "slug": "zcode-task-queue",
        "eyebrow": "WORKFLOW TOOL  /  AUTOMATION",
        "title": "ZCode Task Queue",
        "description": "A sequential session-resume queue for repeatable coding-agent workflows.",
        "meta": "JAVASCRIPT  ·  AUTOMATION  ·  DESKTOP",
        "accent": "#8590A6",
    },
]


def banner_svg(theme: str) -> str:
    p = PALETTES[theme]
    glow_opacity = "0.30" if theme == "dark" else "0.22"
    grid_opacity = "0.10" if theme == "dark" else "0.08"
    return f"""<svg width="1280" height="340" viewBox="0 0 1280 340" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc">
  <title id="title">Samoyer — Small tools. Real workflows.</title>
  <desc id="desc">A warm slate banner with amber line art inspired by a cat and a small companion.</desc>
  <defs>
    <linearGradient id="bg" x1="72" y1="24" x2="1170" y2="326" gradientUnits="userSpaceOnUse">
      <stop stop-color="{p['canvas']}"/>
      <stop offset="1" stop-color="{p['canvas_alt']}"/>
    </linearGradient>
    <radialGradient id="glow" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(1038 169) rotate(90) scale(315 430)">
      <stop stop-color="{p['accent']}" stop-opacity="{glow_opacity}"/>
      <stop offset="1" stop-color="{p['accent']}" stop-opacity="0"/>
    </radialGradient>
    <pattern id="grid" width="38" height="38" patternUnits="userSpaceOnUse">
      <path d="M38 0H0V38" stroke="{p['line']}" stroke-opacity="{grid_opacity}"/>
    </pattern>
    <clipPath id="frame">
      <rect x="18" y="18" width="1244" height="304" rx="30"/>
    </clipPath>
  </defs>
  <g clip-path="url(#frame)">
    <rect x="18" y="18" width="1244" height="304" rx="30" fill="url(#bg)"/>
    <rect x="18" y="18" width="1244" height="304" rx="30" fill="url(#grid)"/>
    <rect x="18" y="18" width="1244" height="304" rx="30" fill="url(#glow)"/>
    <path d="M982 54C1042 89 1101 84 1173 54" stroke="{p['accent_soft']}" stroke-opacity=".34" stroke-width="1.5"/>
    <path d="M935 279C1025 240 1112 250 1213 297" stroke="{p['accent']}" stroke-opacity=".18" stroke-width="1.5"/>

    <g opacity=".95">
      <path d="M1047 214C1019 192 1001 163 1000 129C999 96 1017 71 1047 68C1077 71 1095 96 1094 129C1093 163 1075 192 1047 214Z" stroke="{p['accent_soft']}" stroke-width="2.5"/>
      <path d="M1004 100L991 59L1022 78" stroke="{p['accent_soft']}" stroke-width="2.5" stroke-linejoin="round"/>
      <path d="M1090 100L1103 59L1072 78" stroke="{p['accent_soft']}" stroke-width="2.5" stroke-linejoin="round"/>
      <path d="M1017 128C1024 123 1030 123 1036 128M1058 128C1064 123 1070 123 1077 128" stroke="{p['accent_soft']}" stroke-width="2.5" stroke-linecap="round"/>
      <path d="M1046 139L1040 149H1052L1046 139Z" fill="{p['accent']}"/>
      <path d="M1040 158C1045 163 1049 163 1054 158" stroke="{p['accent_soft']}" stroke-width="2" stroke-linecap="round"/>
      <path d="M1007 144L970 136M1006 151L968 153M1008 158L975 169M1085 144L1122 136M1086 151L1124 153M1084 158L1117 169" stroke="{p['accent']}" stroke-opacity=".72" stroke-width="1.8" stroke-linecap="round"/>
      <circle cx="1047" cy="39" r="19" fill="{p['panel']}" stroke="{p['accent_soft']}" stroke-width="2"/>
      <path d="M1038 29L1034 19L1043 24M1056 29L1060 19L1051 24" stroke="{p['accent_soft']}" stroke-width="1.6" stroke-linejoin="round"/>
      <circle cx="1042" cy="37" r="1.4" fill="{p['accent']}"/>
      <circle cx="1052" cy="37" r="1.4" fill="{p['accent']}"/>
      <path d="M1047 42V44M1044 47C1046 49 1048 49 1050 47" stroke="{p['accent_soft']}" stroke-width="1.2" stroke-linecap="round"/>
    </g>

    <rect x="70" y="64" width="142" height="28" rx="14" fill="{p['accent']}" fill-opacity=".12" stroke="{p['accent']}" stroke-opacity=".34"/>
    <circle cx="86" cy="78" r="3" fill="{p['accent']}"/>
    <text x="98" y="82" fill="{p['accent']}" font-family="'SFMono-Regular',Consolas,monospace" font-size="11" font-weight="700" letter-spacing="1.8">BUILD LOG / 001</text>

    <text x="70" y="174" fill="{p['text']}" font-family="'SF Pro Display',-apple-system,BlinkMacSystemFont,'Helvetica Neue',sans-serif" font-size="86" font-weight="700" letter-spacing="-5">SAMOYER</text>
    <text x="74" y="218" fill="{p['text']}" font-family="'SF Pro Display',-apple-system,BlinkMacSystemFont,'Helvetica Neue',sans-serif" font-size="27" font-weight="500" letter-spacing="-.4">Small tools. Real workflows.</text>
    <path d="M74 246H604" stroke="{p['line']}" stroke-width="1"/>
    <text x="74" y="275" fill="{p['muted']}" font-family="'SF Pro Text',-apple-system,BlinkMacSystemFont,'Helvetica Neue',sans-serif" font-size="14" letter-spacing=".2">LOCAL-FIRST SOFTWARE  ·  DESKTOP SYSTEMS  ·  DEVELOPER TOOLS</text>

    <text x="1182" y="286" text-anchor="end" fill="{p['faint']}" font-family="'SFMono-Regular',Consolas,monospace" font-size="10" letter-spacing="1.7">OPEN SOURCE / MADE WITH CARE</text>
    <rect x="18.5" y="18.5" width="1243" height="303" rx="29.5" stroke="{p['line']}"/>
  </g>
</svg>
"""


def card_svg(project: dict[str, str], theme: str) -> str:
    p = PALETTES[theme]
    accent = project["accent"]
    glow_opacity = "0.20" if theme == "dark" else "0.13"
    title = escape(project["title"])
    description = escape(project["description"])
    eyebrow = escape(project["eyebrow"])
    meta = escape(project["meta"])
    return f"""<svg width="1080" height="142" viewBox="0 0 1080 142" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc">
  <title id="title">{title}</title>
  <desc id="desc">{description}</desc>
  <defs>
    <linearGradient id="card-bg" x1="0" y1="0" x2="1080" y2="142" gradientUnits="userSpaceOnUse">
      <stop stop-color="{p['panel']}"/>
      <stop offset="1" stop-color="{p['canvas_alt']}"/>
    </linearGradient>
    <radialGradient id="card-glow" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(962 75) rotate(90) scale(150 330)">
      <stop stop-color="{accent}" stop-opacity="{glow_opacity}"/>
      <stop offset="1" stop-color="{accent}" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect x="0.75" y="0.75" width="1078.5" height="140.5" rx="22.25" fill="url(#card-bg)" stroke="{p['line']}" stroke-width="1.5"/>
  <rect x="0.75" y="0.75" width="1078.5" height="140.5" rx="22.25" fill="url(#card-glow)"/>
  <rect x="26" y="25" width="4" height="92" rx="2" fill="{accent}"/>
  <text x="54" y="37" fill="{accent}" font-family="'SFMono-Regular',Consolas,monospace" font-size="10.5" font-weight="700" letter-spacing="1.65">{eyebrow}</text>
  <text x="53" y="76" fill="{p['text']}" font-family="'SF Pro Display',-apple-system,BlinkMacSystemFont,'Helvetica Neue',sans-serif" font-size="30" font-weight="700" letter-spacing="-.7">{title}</text>
  <text x="54" y="102" fill="{p['muted']}" font-family="'SF Pro Text',-apple-system,BlinkMacSystemFont,'Helvetica Neue',sans-serif" font-size="14.5">{description}</text>
  <text x="54" y="125" fill="{p['faint']}" font-family="'SFMono-Regular',Consolas,monospace" font-size="9.5" letter-spacing="1.25">{meta}</text>
  <text x="1042" y="30" text-anchor="end" fill="{p['faint']}" font-family="'SFMono-Regular',Consolas,monospace" font-size="11" letter-spacing="1.5">{project['index']}</text>
  <g transform="translate(992 96)">
    <circle cx="22" cy="22" r="21" stroke="{p['line']}"/>
    <path d="M15 22H29M24 16L30 22L24 28" stroke="{accent}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
</svg>
"""


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    for theme in PALETTES:
        (ASSETS / f"profile-banner-{theme}.svg").write_text(
            banner_svg(theme), encoding="utf-8"
        )
        for project in PROJECTS:
            (ASSETS / f"card-{project['slug']}-{theme}.svg").write_text(
                card_svg(project, theme), encoding="utf-8"
            )


if __name__ == "__main__":
    main()
