"""
Static Site Generator (SSG) Engine for GKM Elektrik Engineering Hub
Compiles Markdown content into ultra-fast, multi-page, high-ranking static HTML.
Zero external framework dependencies - runs purely on Python.
"""

import os
import re
import json
import glob
from datetime import datetime
from svg_generator import generate_svg_diagram

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(BASE_DIR, "content")
DIST_DIR = os.path.join(BASE_DIR, "dist")

SITE_URL = "https://gokmen-54.github.io/gkm-engineering-hub"
MAIN_WEBSITE = "https://gkmelektrik.com"
WHATSAPP_PHONE = "905377029954"
PHONE_DISPLAY = "0537 702 99 54"

CATEGORIES = {
    "makine-otomasyonu": {
        "title": "Makine Otomasyonu",
        "desc": "Özel makine otomasyon yazılımları, servo/step motor senkronizasyonu, hat revizyonu ve elektronik kamlama çözümleri.",
        "icon": "⚙️",
        "color": "cyan"
    },
    "plc-scada-yazilim": {
        "title": "PLC & SCADA Yazılım",
        "desc": "Siemens, Schneider ve Beckhoff PLC programlama, SCADA mimarisi, Endüstriyel IoT ve Modbus/MQTT veri toplama.",
        "icon": "💻",
        "color": "indigo"
    },
    "pcb-elektronik-tasarim": {
        "title": "PCB & Elektronik Tasarım",
        "desc": "Çok katmanlı endüstriyel elektronik kart tasarımı, Altium/KiCad şematiği, STM32/ESP32 gömülü yazılım ve prototipleme.",
        "icon": "⚡",
        "color": "emerald"
    },
    "elektrik-panosu-salt": {
        "title": "Elektrik Panosu & Şalt",
        "desc": "Tip testli Ana Dağıtım (ADP), MCC motor kontrol panoları, harmonik filtreli kompanzasyon ve toptan şalt tedariği.",
        "icon": "🛡️",
        "color": "amber"
    }
}


def parse_frontmatter(content):
    meta = {}
    body = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            raw_meta = parts[1].strip()
            body = parts[2].strip()
            for line in raw_meta.split("\n"):
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, body


def markdown_to_html(md):
    # Code blocks
    def replace_code_block(match):
        lang = match.group(1) or ""
        code = match.group(2).replace("<", "&lt;").replace(">", "&gt;")
        return f'<pre class="bg-slate-950 text-cyan-300 p-5 rounded-2xl border border-slate-800 text-xs sm:text-sm overflow-x-auto my-6 font-mono"><code>{code}</code></pre>'
    
    html = re.sub(r'```(\w+)?\n([\s\S]*?)```', replace_code_block, md)

    # Tables
    lines = html.split("\n")
    in_table = False
    table_lines = []
    output_lines = []

    for line in lines:
        if "|" in line:
            if not in_table:
                in_table = True
                table_lines = []
            table_lines.append(line)
        else:
            if in_table:
                in_table = False
                # Convert table_lines to HTML table
                t_html = '<div class="overflow-x-auto my-6"><table class="w-full text-left text-xs sm:text-sm border-collapse bg-slate-900/60 rounded-xl border border-slate-800">'
                header = True
                for tl in table_lines:
                    if "---" in tl:
                        continue
                    cells = [c.strip() for c in tl.split("|")[1:-1]]
                    if header:
                        t_html += '<thead class="bg-slate-950 text-cyan-400 font-bold border-b border-slate-800"><tr>' + "".join(f'<th class="p-3.5">{c}</th>' for c in cells) + '</tr></thead><tbody>'
                        header = False
                    else:
                        t_html += '<tr class="border-b border-slate-800/60 hover:bg-slate-800/30 transition">' + "".join(f'<td class="p-3.5">{c}</td>' for c in cells) + '</tr>'
                t_html += '</tbody></table></div>'
                output_lines.append(t_html)
            output_lines.append(line)

    if in_table:
        # flush table at end
        pass

    html = "\n".join(output_lines)

    # Headings
    html = re.sub(r'^### (.*$)', r'<h3 class="text-lg sm:text-xl font-bold text-white mt-8 mb-3">\1</h3>', html, flags=re.M)
    html = re.sub(r'^## (.*$)', r'<h2 class="text-xl sm:text-2xl font-black text-cyan-400 mt-10 mb-4 pb-2 border-b border-slate-800">\1</h2>', html, flags=re.M)
    html = re.sub(r'^# (.*$)', r'<h1 class="text-2xl sm:text-3xl font-black text-white mt-6 mb-4">\1</h1>', html, flags=re.M)

    # Paragraphs & Lists
    html = re.sub(r'^\- (.*$)', r'<li class="ml-4 list-disc text-slate-300 mb-1.5">\1</li>', html, flags=re.M)
    html = re.sub(r'^\d+\. (.*$)', r'<li class="ml-4 list-decimal text-slate-300 mb-1.5">\1</li>', html, flags=re.M)

    # Strong / Emphasis
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong class="text-white font-extrabold">\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em class="text-slate-300 italic">\1</em>', html)

    # Wrap bare lines in <p>
    final_paras = []
    for block in html.split("\n\n"):
        block = block.strip()
        if not block:
            continue
        if block.startswith("<h") or block.startswith("<pre") or block.startswith("<div") or block.startswith("<li"):
            final_paras.append(block)
        else:
            final_paras.append(f'<p class="text-slate-300 leading-relaxed text-sm sm:text-base mb-4">{block}</p>')

    return "\n\n".join(final_paras)


def load_all_articles():
    articles = []
    files = glob.glob(os.path.join(CONTENT_DIR, "**", "*.md"), recursive=True)
    for f in files:
        with open(f, "r", encoding="utf-8") as fp:
            content = fp.read()
        meta, body = parse_frontmatter(content)
        if meta.get("slug"):
            meta["html_body"] = markdown_to_html(body)
            articles.append(meta)

    # Sort newest first
    articles.sort(key=lambda x: x.get("date", ""), reverse=True)
    return articles


def get_base_header(active_nav=""):
    return f"""
    <!-- Top Announcement Bar -->
    <div class="bg-gradient-to-r from-slate-950 via-cyan-950/40 to-slate-950 text-slate-300 text-xs py-2.5 px-4 border-b border-slate-800">
        <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
            <div class="flex items-center gap-2">
                <span class="inline-block w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span>
                <span><b>GKM Elektrik & Mühendislik:</b> Endüstriyel Otomasyon, PLC/SCADA, PCB ve Pano İmalatı</span>
            </div>
            <div class="flex items-center gap-4 text-xs font-semibold">
                <a href="{MAIN_WEBSITE}" target="_blank" class="text-cyan-400 hover:underline flex items-center gap-1">
                    <span>Resmi Sitemiz: gkmelektrik.com</span> ➔
                </a>
                <a href="tel:{WHATSAPP_PHONE}" class="text-slate-400 hover:text-white hidden sm:inline">
                    📞 {PHONE_DISPLAY}
                </a>
            </div>
        </div>
    </div>

    <!-- Main Navigation Header -->
    <header class="border-b border-slate-800 bg-slate-950/90 backdrop-blur-md sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 h-20 flex items-center justify-between gap-4">
            
            <!-- Logo -->
            <a href="{SITE_URL}/" class="flex items-center gap-3">
                <div class="w-11 h-11 rounded-xl bg-gradient-to-tr from-cyan-500 to-blue-600 flex items-center justify-center text-slate-950 font-black text-xl shadow-lg shadow-cyan-500/20">
                    ⚡
                </div>
                <div>
                    <span class="text-xl font-black text-white tracking-tight block">GKM<span class="text-cyan-400">MÜHENDİSLİK</span></span>
                    <span class="text-[10px] text-slate-400 uppercase tracking-widest block font-bold">Endüstriyel Çözüm & Teknik Hub</span>
                </div>
            </a>

            <!-- Nav Links -->
            <nav class="hidden lg:flex items-center gap-6 text-xs sm:text-sm font-bold text-slate-300">
                <a href="{SITE_URL}/makine-otomasyonu/" class="hover:text-cyan-400 transition {'text-cyan-400' if active_nav == 'makine-otomasyonu' else ''}">Makine Otomasyonu</a>
                <a href="{SITE_URL}/plc-scada-yazilim/" class="hover:text-cyan-400 transition {'text-cyan-400' if active_nav == 'plc-scada-yazilim' else ''}">PLC & SCADA</a>
                <a href="{SITE_URL}/pcb-elektronik-tasarim/" class="hover:text-cyan-400 transition {'text-cyan-400' if active_nav == 'pcb-elektronik-tasarim' else ''}">PCB Tasarımı</a>
                <a href="{SITE_URL}/elektrik-panosu-salt/" class="hover:text-cyan-400 transition {'text-cyan-400' if active_nav == 'elektrik-panosu-salt' else ''}">Pano & Şalt</a>
            </nav>

            <!-- CTA Buttons -->
            <div class="flex items-center gap-3">
                <a href="https://wa.me/{WHATSAPP_PHONE}?text={urllib_quote('Merhaba, mühendislik projemiz için teknik görüşme ve teklif almak istiyoruz.')}" target="_blank" rel="noopener" class="bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 font-black text-xs sm:text-sm py-2.5 px-4 sm:px-5 rounded-full shadow-lg shadow-emerald-500/20 transition flex items-center gap-2">
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
                    <span>WhatsApp Proje Danış</span>
                </a>
            </div>

        </div>
    </header>
    """


def get_base_footer():
    return f"""
    <!-- Mobile Sticky Action Bar -->
    <div class="lg:hidden fixed bottom-0 left-0 right-0 z-50 bg-slate-950/95 border-t border-slate-800 backdrop-blur-lg px-4 py-2.5 flex items-center justify-between gap-2 shadow-2xl">
        <a href="tel:{WHATSAPP_PHONE}" class="flex-1 bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs py-2.5 px-3 rounded-xl border border-slate-700 flex items-center justify-center gap-1.5">
            📞 Hemen Ara: {PHONE_DISPLAY}
        </a>
        <a href="https://wa.me/{WHATSAPP_PHONE}?text={urllib_quote('Merhaba GKM Elektrik, teknik projemiz için şema/liste gönderip teklif almak istiyoruz.')}" target="_blank" class="flex-1 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-black text-xs py-2.5 px-3 rounded-xl shadow-lg shadow-emerald-500/25 flex items-center justify-center gap-1.5">
            <span>WhatsApp Şema Gönder</span>
        </a>
    </div>

    <!-- Footer -->
    <footer class="border-t border-slate-800 bg-slate-950 text-slate-500 text-xs py-14 pb-24 lg:pb-14">
        <div class="max-w-7xl mx-auto px-4 sm:px-6">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8 pb-10 border-b border-slate-900">
                <div class="md:col-span-1">
                    <div class="flex items-center gap-3 mb-3">
                        <div class="w-8 h-8 rounded-lg bg-cyan-500 flex items-center justify-center text-slate-950 font-black">⚡</div>
                        <span class="font-black text-white text-base">GKM Elektrik</span>
                    </div>
                    <p class="text-slate-400 leading-relaxed text-xs mb-4">
                        Özel makine otomasyonu, PLC/SCADA yazılımı, çok katmanlı PCB tasarımı ve tip testli elektrik panosu imalatı.
                    </p>
                    <a href="{MAIN_WEBSITE}" target="_blank" class="text-cyan-400 font-bold hover:underline block">
                        ➔ Resmi Web Sitemiz: gkmelektrik.com
                    </a>
                </div>

                <div>
                    <h4 class="font-bold text-white uppercase text-xs tracking-wider mb-3">Hizmet Alanlarımız</h4>
                    <ul class="space-y-2">
                        <li><a href="{SITE_URL}/makine-otomasyonu/" class="hover:text-cyan-400 transition">Makine Otomasyonu & Servo</a></li>
                        <li><a href="{SITE_URL}/plc-scada-yazilim/" class="hover:text-cyan-400 transition">PLC Programlama & SCADA</a></li>
                        <li><a href="{SITE_URL}/pcb-elektronik-tasarim/" class="hover:text-cyan-400 transition">Özel PCB & Gömülü Sistemler</a></li>
                        <li><a href="{SITE_URL}/elektrik-panosu-salt/" class="hover:text-cyan-400 transition">Tip Testli Pano & Kompanzasyon</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="font-bold text-white uppercase text-xs tracking-wider mb-3">Mühendislik İletişim</h4>
                    <ul class="space-y-2 text-slate-400">
                        <li><b>Telefon:</b> <a href="tel:{WHATSAPP_PHONE}" class="hover:text-white">{PHONE_DISPLAY}</a></li>
                        <li><b>WhatsApp:</b> <a href="https://wa.me/{WHATSAPP_PHONE}" target="_blank" class="hover:text-emerald-400">+90 537 702 99 54</a></li>
                        <li><b>Hizmet Sahası:</b> Sakarya, Kocaeli, Marmara & Tüm Türkiye</li>
                    </ul>
                </div>

                <div>
                    <h4 class="font-bold text-white uppercase text-xs tracking-wider mb-3">Hızlı Şema & Teklif</h4>
                    <p class="text-slate-400 text-xs mb-3">
                        EPLAN pano projenizi, makine fonksiyon şemanızı veya PCB gerber dosyalarınızı WhatsApp üzerinden anında iletebilirsiniz.
                    </p>
                    <a href="https://wa.me/{WHATSAPP_PHONE}?text={urllib_quote('Merhaba, projemiz için teknik döküman paylaşmak istiyoruz.')}" target="_blank" class="inline-block bg-slate-900 hover:bg-slate-800 text-cyan-400 border border-slate-800 px-4 py-2 rounded-xl text-xs font-bold transition">
                        Şema & Liste Gönder ➔
                    </a>
                </div>
            </div>

            <div class="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-[11px] text-slate-600">
                <p>© 2026 GKM Elektrik & Mühendislik. Tüm hakları saklıdır.</p>
                <p>Programmatic Engineering Hub • Yüksek Performanslı SEO ve Müşteri Yakalama Motoru</p>
            </div>
        </div>
    </footer>
    """


def urllib_quote(text):
    import urllib.parse
    return urllib.parse.quote(text)


def build_homepage(articles):
    header = get_base_header(active_nav="")
    footer = get_base_footer()

    # Cards HTML for all articles
    cards_html = ""
    for a in articles:
        cat_info = CATEGORIES.get(a["category"], {})
        badge_color = cat_info.get("color", "cyan")
        svg_preview = generate_svg_diagram(a.get("diagram_type", "default"), a["title"])
        
        cards_html += f"""
        <article class="bg-slate-900/70 rounded-2xl border border-slate-800 hover:border-cyan-500/50 transition-all duration-300 hover:shadow-2xl hover:-translate-y-1 flex flex-col justify-between overflow-hidden group">
            <div class="p-3 bg-slate-950 border-b border-slate-800">
                {svg_preview}
            </div>

            <div class="p-6 flex-1 flex flex-col justify-between">
                <div>
                    <div class="flex items-center justify-between text-xs font-bold text-slate-400 mb-2">
                        <span class="text-cyan-400 uppercase tracking-wider">{a.get('category_title', 'Mühendislik')}</span>
                        <span>{a.get('reading_time', '7 dk')}</span>
                    </div>

                    <h3 class="text-lg font-black text-white leading-snug group-hover:text-cyan-400 transition mb-3">
                        <a href="{SITE_URL}/rehber/{a['slug']}/">{a['title']}</a>
                    </h3>

                    <p class="text-slate-400 text-xs sm:text-sm line-clamp-3 leading-relaxed mb-6">
                        {a['summary']}
                    </p>
                </div>

                <div class="pt-4 border-t border-slate-800/80 flex items-center justify-between">
                    <span class="text-[11px] font-semibold text-slate-500">🎯 {a.get('target_audience', 'Mühendisler')}</span>
                    <a href="{SITE_URL}/rehber/{a['slug']}/" class="text-cyan-400 hover:text-cyan-300 font-bold text-xs flex items-center gap-1 group-hover:translate-x-1 transition">
                        <span>Teknik Analizi İncele</span> ➔
                    </a>
                </div>
            </div>
        </article>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="tr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GKM Elektrik & Mühendislik | Makine Otomasyonu, PLC/SCADA, PCB Tasarımı ve Pano İmalatı</title>
    <meta name="description" content="Özel makine otomasyonu, Siemens/Beckhoff PLC ve SCADA yazılımı, çok katmanlı PCB ve gömülü sistemler, tip testli elektrik panoları ve kompanzasyon çözümleri.">
    <meta name="keywords" content="makine otomasyonu, plc programlama, scada yazılımı, pcb tasarımı, gömülü sistemler, elektrik panosu imalatı, harmonik filtre kompanzasyon, sakarya otomasyon, kocaeli otomasyon">
    <link rel="canonical" href="{SITE_URL}/">

    <!-- Open Graph -->
    <meta property="og:title" content="GKM Elektrik & Mühendislik | Endüstriyel Çözüm & Otomasyon Hub">
    <meta property="og:description" content="Fabrikalar ve makine imalatçıları için ileri teknoloji mühendislik, PLC/SCADA, özel PCB ve şalt çözümleri.">
    <meta property="og:url" content="{SITE_URL}/">
    <meta property="og:type" content="website">

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap');
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    </style>

    <!-- Schema.org Structured Data -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@graph": [
        {{
          "@type": "Organization",
          "@id": "{SITE_URL}/#organization",
          "name": "GKM Elektrik & Mühendislik",
          "url": "{MAIN_WEBSITE}",
          "logo": "{SITE_URL}/assets/logo.png",
          "contactPoint": {{
            "@type": "ContactPoint",
            "telephone": "+{WHATSAPP_PHONE}",
            "contactType": "customer service",
            "areaServed": "TR"
          }},
          "sameAs": [
            "{MAIN_WEBSITE}"
          ]
        }},
        {{
          "@type": "WebSite",
          "@id": "{SITE_URL}/#website",
          "name": "GKM Mühendislik Hub",
          "url": "{SITE_URL}/"
        }}
      ]
    }}
    </script>
</head>
<body class="bg-slate-950 text-slate-100 font-sans antialiased selection:bg-cyan-500 selection:text-black min-h-screen flex flex-col justify-between">

    {header}

    <!-- Hero Section -->
    <section class="relative pt-16 pb-20 border-b border-slate-800 overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-b from-cyan-500/10 via-slate-950 to-slate-950 pointer-events-none"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10 text-center">
            
            <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-slate-900 border border-cyan-500/30 text-cyan-400 text-xs font-bold mb-6">
                <span>⚡ PROGRAMMATIC ENGINEERING & INDUSTRIAL AUTOMATION HUB</span>
            </div>

            <h1 class="text-3xl sm:text-5xl lg:text-6xl font-black text-white tracking-tight max-w-4xl mx-auto leading-tight mb-6">
                Özel Makine Otomasyonu, <span class="bg-gradient-to-r from-cyan-400 to-blue-400 bg-clip-text text-transparent">Gömülü PCB Tasarımı</span> ve Tip Testli Pano Sistemleri
            </h1>

            <p class="text-slate-400 text-sm sm:text-base max-w-3xl mx-auto leading-relaxed mb-10">
                Endüstriyel tesisler, makine imalatçıları ve Ar-Ge departmanları için uçtan uca mühendislik: PLC/SCADA yazılımı, yüksek hassasiyetli servo kontrolü, 4 katmanlı EMC uyumlu PCB üretimi ve harmonik filtreli kompanzasyon panoları.
            </p>

            <!-- Quick Action Hero Buttons -->
            <div class="flex flex-wrap items-center justify-center gap-4">
                <a href="https://wa.me/{WHATSAPP_PHONE}?text={urllib_quote('Merhaba GKM Elektrik, projemiz için şema/şartname gönderip teknik teklif almak istiyoruz.')}" target="_blank" class="bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-slate-950 font-black text-sm py-4 px-8 rounded-2xl shadow-xl shadow-cyan-500/20 transition transform hover:scale-105 flex items-center gap-2">
                    <span>⚡ WhatsApp'tan Proje / Şema Danış</span>
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
                </a>
                
                <a href="{MAIN_WEBSITE}" target="_blank" class="bg-slate-900 hover:bg-slate-800 text-white font-bold text-sm py-4 px-8 rounded-2xl border border-slate-700 transition flex items-center gap-2">
                    <span>Resmi Şirket Sitemiz (gkmelektrik.com)</span> ➔
                </a>
            </div>

            <!-- Industrial Trust Metrics -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 max-w-4xl mx-auto mt-14 pt-10 border-t border-slate-800/80 text-left">
                <div>
                    <span class="text-2xl font-black text-cyan-400 block">IEC 61439</span>
                    <span class="text-xs text-slate-400">Tip Testli Pano Standartları</span>
                </div>
                <div>
                    <span class="text-2xl font-black text-emerald-400 block">TIA & TwinCAT</span>
                    <span class="text-xs text-slate-400">Siemens & Beckhoff PLC/SCL</span>
                </div>
                <div>
                    <span class="text-2xl font-black text-amber-400 block">4-Katman EMC</span>
                    <span class="text-xs text-slate-400">Endüstriyel PCB & STM32</span>
                </div>
                <div>
                    <span class="text-2xl font-black text-indigo-400 block">24/7 Saha</span>
                    <span class="text-xs text-slate-400">Devreye Alma & Revizyon</span>
                </div>
            </div>

        </div>
    </section>

    <!-- 4 Core Service Pillars -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 py-16">
        <div class="mb-10 text-center">
            <span class="text-xs font-black text-cyan-400 uppercase tracking-widest block mb-1">MÜHENDİSLİK DİSİPLİNLERİMİZ</span>
            <h2 class="text-2xl sm:text-3xl font-black text-white">Fabrikalar ve Makine İmalatçıları İçin Çözümler</h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div class="bg-slate-900/60 p-6 rounded-2xl border border-slate-800 hover:border-cyan-500/40 transition">
                <div class="w-12 h-12 rounded-xl bg-cyan-500/10 text-cyan-400 flex items-center justify-center text-2xl mb-4">⚙️</div>
                <h3 class="text-lg font-bold text-white mb-2">Makine Otomasyonu</h3>
                <p class="text-slate-400 text-xs leading-relaxed mb-4">
                    Elektronik kamlama, çok eksenli servo senkronizasyonu, hat revizyonları ve paketleme/dolum makineleri yazılımı.
                </p>
                <a href="{SITE_URL}/makine-otomasyonu/" class="text-cyan-400 text-xs font-bold hover:underline">Rehberleri İncele ➔</a>
            </div>

            <div class="bg-slate-900/60 p-6 rounded-2xl border border-slate-800 hover:border-indigo-500/40 transition">
                <div class="w-12 h-12 rounded-xl bg-indigo-500/10 text-indigo-400 flex items-center justify-center text-2xl mb-4">💻</div>
                <h3 class="text-lg font-bold text-white mb-2">PLC & SCADA Yazılım</h3>
                <p class="text-slate-400 text-xs leading-relaxed mb-4">
                    Siemens TIA SCL, Beckhoff TwinCAT, WinCC/Ignition SCADA ve Modbus/MQTT Endüstriyel IoT veri toplama.
                </p>
                <a href="{SITE_URL}/plc-scada-yazilim/" class="text-indigo-400 text-xs font-bold hover:underline">Rehberleri İncele ➔</a>
            </div>

            <div class="bg-slate-900/60 p-6 rounded-2xl border border-slate-800 hover:border-emerald-500/40 transition">
                <div class="w-12 h-12 rounded-xl bg-emerald-500/10 text-emerald-400 flex items-center justify-center text-2xl mb-4">⚡</div>
                <h3 class="text-lg font-bold text-white mb-2">Özel PCB & Elektronik</h3>
                <p class="text-slate-400 text-xs leading-relaxed mb-4">
                    Çok katmanlı endüstriyel PCB tasarımı, STM32/ESP32 gömülü yazılım, optokuplör izolasyonlu I/O kartları.
                </p>
                <a href="{SITE_URL}/pcb-elektronik-tasarim/" class="text-emerald-400 text-xs font-bold hover:underline">Rehberleri İncele ➔</a>
            </div>

            <div class="bg-slate-900/60 p-6 rounded-2xl border border-slate-800 hover:border-amber-500/40 transition">
                <div class="w-12 h-12 rounded-xl bg-amber-500/10 text-amber-400 flex items-center justify-center text-2xl mb-4">🛡️</div>
                <h3 class="text-lg font-bold text-white mb-2">Elektrik Panosu & Şalt</h3>
                <p class="text-slate-400 text-xs leading-relaxed mb-4">
                    Tip testli ADP ana dağıtım, MCC sürücü panoları, de-tuned %7 reaktörlü harmonik kompanzasyon panoları.
                </p>
                <a href="{SITE_URL}/elektrik-panosu-salt/" class="text-amber-400 text-xs font-bold hover:underline">Rehberleri İncele ➔</a>
            </div>
        </div>
    </section>

    <!-- Engineering Guides & Articles Grid -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 py-12 border-t border-slate-800">
        <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 mb-10 pb-4 border-b border-slate-800">
            <div>
                <span class="text-xs font-black text-cyan-400 uppercase tracking-widest block mb-1">PROGRAMMATIC TEKNİK KÜTÜPHANE</span>
                <h2 class="text-2xl sm:text-3xl font-black text-white">En Son Mühendislik ve Tasarım Makaleleri</h2>
            </div>
            <p class="text-slate-400 text-xs max-w-md">
                Şemalar, hesaplama yöntemleri ve saha tecrübeleri ile hazırlanmış güncel endüstriyel uygulama rehberleri.
            </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-8">
            {cards_html}
        </div>
    </section>

    <!-- Hot Conversion Lead Banner -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 py-16">
        <div class="bg-gradient-to-r from-slate-900 via-cyan-950/40 to-slate-900 rounded-3xl border border-cyan-500/30 p-8 sm:p-12 flex flex-col lg:flex-row items-center justify-between gap-8 shadow-2xl">
            <div class="max-w-2xl">
                <span class="text-xs font-black text-cyan-400 uppercase tracking-widest block mb-2">HIZLI TEKNİK İNCELEME & ÖN FİZİBİLİTE</span>
                <h3 class="text-2xl sm:text-3xl font-black text-white mb-3">Mevcut Bir Makine, Kart veya Pano Projeniz mi Var?</h3>
                <p class="text-slate-300 text-sm leading-relaxed mb-4">
                    EPLAN proje şemanızı, PLC fonksiyonel tanımınızı veya PCB gerber dosyalarınızı WhatsApp hattımıza gönderin; mühendislerimiz 24 saat içinde ön fizibilite ve bütçelendirmeyi tamamlasın.
                </p>
                <div class="flex items-center gap-6 text-xs text-slate-400">
                    <span>✓ Gizlilik Sözleşmesi (NDA) Korumalı</span>
                    <span>✓ Doğrudan Mühendis Görüşmesi</span>
                </div>
            </div>

            <div class="flex flex-col sm:flex-row gap-3 w-full lg:w-auto">
                <a href="https://wa.me/{WHATSAPP_PHONE}?text={urllib_quote('Merhaba, teknik bir projemiz var (EPLAN şema / gerber / otomasyon). Birlikte değerlendirmek istiyoruz.')}" target="_blank" class="bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-black text-sm py-4 px-8 rounded-2xl shadow-xl shadow-emerald-500/25 transition text-center flex items-center justify-center gap-2">
                    <span>WhatsApp'tan Dosya Gönder</span>
                </a>
                <a href="tel:{WHATSAPP_PHONE}" class="bg-slate-900 hover:bg-slate-800 text-white font-bold text-sm py-4 px-6 rounded-2xl border border-slate-700 transition text-center">
                    📞 {PHONE_DISPLAY}
                </a>
            </div>
        </div>
    </section>

    {footer}

</body>
</html>
"""
    return full_html


def build_category_page(cat_key, articles):
    cat_info = CATEGORIES[cat_key]
    cat_articles = [a for a in articles if a["category"] == cat_key]
    header = get_base_header(active_nav=cat_key)
    footer = get_base_footer()

    cards_html = ""
    for a in cat_articles:
        svg_preview = generate_svg_diagram(a.get("diagram_type", "default"), a["title"])
        cards_html += f"""
        <article class="bg-slate-900/70 rounded-2xl border border-slate-800 hover:border-cyan-500/50 transition-all duration-300 hover:shadow-2xl hover:-translate-y-1 flex flex-col justify-between overflow-hidden group">
            <div class="p-3 bg-slate-950 border-b border-slate-800">
                {svg_preview}
            </div>

            <div class="p-6 flex-1 flex flex-col justify-between">
                <div>
                    <div class="flex items-center justify-between text-xs font-bold text-slate-400 mb-2">
                        <span class="text-cyan-400 uppercase tracking-wider">{cat_info['title']}</span>
                        <span>{a.get('reading_time', '7 dk')}</span>
                    </div>

                    <h3 class="text-lg font-black text-white leading-snug group-hover:text-cyan-400 transition mb-3">
                        <a href="{SITE_URL}/rehber/{a['slug']}/">{a['title']}</a>
                    </h3>

                    <p class="text-slate-400 text-xs sm:text-sm line-clamp-3 leading-relaxed mb-6">
                        {a['summary']}
                    </p>
                </div>

                <div class="pt-4 border-t border-slate-800/80 flex items-center justify-between">
                    <span class="text-[11px] font-semibold text-slate-500">🎯 {a.get('target_audience', 'Mühendisler')}</span>
                    <a href="{SITE_URL}/rehber/{a['slug']}/" class="text-cyan-400 hover:text-cyan-300 font-bold text-xs flex items-center gap-1 group-hover:translate-x-1 transition">
                        <span>Teknik Analizi İncele</span> ➔
                    </a>
                </div>
            </div>
        </article>
        """

    return f"""<!DOCTYPE html>
<html lang="tr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{cat_info['title']} Çözümleri & Teknik Rehberler | GKM Elektrik</title>
    <meta name="description" content="{cat_info['desc']}">
    <link rel="canonical" href="{SITE_URL}/{cat_key}/">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap');
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    </style>
</head>
<body class="bg-slate-950 text-slate-100 font-sans antialiased selection:bg-cyan-500 selection:text-black min-h-screen flex flex-col justify-between">

    {header}

    <section class="py-14 border-b border-slate-800 bg-gradient-to-b from-slate-900 to-slate-950">
        <div class="max-w-7xl mx-auto px-4 sm:px-6">
            <span class="text-xs font-black text-cyan-400 uppercase tracking-widest block mb-2">{cat_info['icon']} UZMANLIK ALANIMIZ</span>
            <h1 class="text-3xl sm:text-4xl font-black text-white mb-4">{cat_info['title']}</h1>
            <p class="text-slate-400 text-sm sm:text-base max-w-3xl leading-relaxed">
                {cat_info['desc']}
            </p>
        </div>
    </section>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 py-12 flex-1 w-full">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            {cards_html}
        </div>
    </main>

    {footer}

</body>
</html>
"""


def build_article_page(article):
    header = get_base_header(active_nav=article["category"])
    footer = get_base_footer()
    svg_diagram = generate_svg_diagram(article.get("diagram_type", "default"), article["title"])

    # WhatsApp pre-filled link
    wa_msg = f"Merhaba GKM Elektrik, '{article['title']}' konulu rehberinizi okudum. Benzer bir projemiz var, teknik detayları danışmak ve teklif almak istiyorum."
    wa_link = f"https://wa.me/{WHATSAPP_PHONE}?text={urllib_quote(wa_msg)}"

    return f"""<!DOCTYPE html>
<html lang="tr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{article['title']} | GKM Elektrik & Mühendislik</title>
    <meta name="description" content="{article['summary']}">
    <link rel="canonical" href="{SITE_URL}/rehber/{article['slug']}/">

    <!-- Open Graph -->
    <meta property="og:title" content="{article['title']}">
    <meta property="og:description" content="{article['summary']}">
    <meta property="og:url" content="{SITE_URL}/rehber/{article['slug']}/">
    <meta property="og:type" content="article">

    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap');
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    </style>

    <!-- Schema.org Article & Breadcrumbs -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@graph": [
        {{
          "@type": "BreadcrumbList",
          "itemListElement": [
            {{
              "@type": "ListItem",
              "position": 1,
              "name": "Ana Sayfa",
              "item": "{SITE_URL}/"
            }},
            {{
              "@type": "ListItem",
              "position": 2,
              "name": "{article.get('category_title', 'Mühendislik')}",
              "item": "{SITE_URL}/{article['category']}/"
            }},
            {{
              "@type": "ListItem",
              "position": 3,
              "name": "{article['title']}",
              "item": "{SITE_URL}/rehber/{article['slug']}/"
            }}
          ]
        }},
        {{
          "@type": "TechArticle",
          "headline": "{article['title']}",
          "description": "{article['summary']}",
          "author": {{
            "@type": "Organization",
            "name": "GKM Elektrik & Mühendislik",
            "url": "{MAIN_WEBSITE}"
          }},
          "publisher": {{
            "@type": "Organization",
            "name": "GKM Elektrik",
            "url": "{MAIN_WEBSITE}"
          }},
          "datePublished": "{article.get('date', '2026-11-12')}",
          "inLanguage": "tr"
        }}
      ]
    }}
    </script>
</head>
<body class="bg-slate-950 text-slate-100 font-sans antialiased selection:bg-cyan-500 selection:text-black min-h-screen flex flex-col justify-between">

    {header}

    <!-- Article Breadcrumb & Title Header -->
    <section class="py-12 border-b border-slate-800 bg-slate-900/40">
        <div class="max-w-4xl mx-auto px-4 sm:px-6">
            
            <nav class="flex items-center gap-2 text-xs font-semibold text-slate-400 mb-4">
                <a href="{SITE_URL}/" class="hover:text-cyan-400">Ana Sayfa</a>
                <span>/</span>
                <a href="{SITE_URL}/{article['category']}/" class="text-cyan-400 hover:underline">{article.get('category_title', 'Kategori')}</a>
                <span>/</span>
                <span class="text-slate-500 truncate max-w-xs">{article['slug']}</span>
            </nav>

            <div class="flex items-center gap-3 text-xs font-bold text-slate-400 mb-4">
                <span class="bg-cyan-500/10 text-cyan-400 px-3 py-1 rounded-full border border-cyan-500/20">{article.get('category_title', 'Mühendislik')}</span>
                <span>⏱️ {article.get('reading_time', '7 dk')}</span>
                <span>📅 {article.get('date', '2026-11-12')}</span>
            </div>

            <h1 class="text-2xl sm:text-4xl font-black text-white leading-tight mb-4">
                {article['title']}
            </h1>

            <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
                {article['summary']}
            </p>

        </div>
    </section>

    <!-- Article Body & Diagram -->
    <main class="max-w-4xl mx-auto px-4 sm:px-6 py-12 flex-1 w-full">
        
        <!-- Technical Vector Schematic -->
        <div class="mb-10">
            {svg_diagram}
            <span class="text-[11px] text-slate-500 font-mono block text-center mt-2">Şekil 1: GKM Mühendislik Teknik Mimari ve Sinyal Akış Diyagramı</span>
        </div>

        <!-- Rendered Markdown Body -->
        <div class="prose prose-invert max-w-none text-slate-300">
            {article['html_body']}
        </div>

        <!-- Hot Lead Magnet & Call To Action Box -->
        <div class="mt-14 p-8 sm:p-10 rounded-3xl bg-gradient-to-r from-slate-900 via-cyan-950/40 to-slate-900 border border-cyan-500/40 shadow-2xl">
            <span class="text-xs font-black text-cyan-400 uppercase tracking-widest block mb-2">GKM MÜHENDİSLİK TEKNİK DANIŞMANLIK</span>
            <h3 class="text-xl sm:text-2xl font-black text-white mb-3">{article.get('cta_headline', 'Bu Proje İçin Destek mi Gerekiyor?')}</h3>
            <p class="text-slate-300 text-sm leading-relaxed mb-6">
                {article.get('cta_text', 'Mevcut sisteminizi inceleyelim, mühendislik ekibimizle en uygun çözümü projelendirelim.')}
            </p>

            <div class="flex flex-col sm:flex-row gap-4">
                <a href="{wa_link}" target="_blank" class="bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-black text-sm py-3.5 px-6 rounded-2xl shadow-lg shadow-emerald-500/20 transition flex items-center justify-center gap-2">
                    <span>WhatsApp'tan Proje / Şema Gönder</span>
                </a>
                <a href="tel:{WHATSAPP_PHONE}" class="bg-slate-900 hover:bg-slate-800 text-white font-bold text-sm py-3.5 px-6 rounded-2xl border border-slate-700 transition flex items-center justify-center gap-2">
                    <span>📞 {PHONE_DISPLAY}</span>
                </a>
                <a href="{MAIN_WEBSITE}" target="_blank" class="bg-slate-950 hover:bg-slate-900 text-cyan-400 font-bold text-sm py-3.5 px-6 rounded-2xl border border-slate-800 transition flex items-center justify-center gap-2">
                    <span>Resmi Site: gkmelektrik.com</span>
                </a>
            </div>
        </div>

    </main>

    {footer}

</body>
</html>
"""


def build_sitemap(articles):
    today = datetime.now().strftime("%Y-%m-%d")
    urls = [
        f"""  <url>
    <loc>{SITE_URL}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>"""
    ]

    for cat in CATEGORIES:
        urls.append(f"""  <url>
    <loc>{SITE_URL}/{cat}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>""")

    for a in articles:
        urls.append(f"""  <url>
    <loc>{SITE_URL}/rehber/{a['slug']}/</loc>
    <lastmod>{a.get('date', today)}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>""")

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>
"""


def build_robots_txt():
    return f"""User-agent: *
Allow: /
Sitemap: {SITE_URL}/sitemap.xml
"""


def compile_site():
    print("[ENGINE] Static compilation starting...")
    articles = load_all_articles()
    print(f"[ENGINE] Loaded {len(articles)} technical articles.")

    # 1. Homepage
    home_html = build_homepage(articles)
    with open(os.path.join(DIST_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(home_html)
    print(" -> dist/index.html compiled.")

    # 2. Categories
    for cat in CATEGORIES:
        cat_dir = os.path.join(DIST_DIR, cat)
        os.makedirs(cat_dir, exist_ok=True)
        cat_html = build_category_page(cat, articles)
        with open(os.path.join(cat_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(cat_html)
        print(f" -> dist/{cat}/index.html compiled.")

    # 3. Articles
    for a in articles:
        art_dir = os.path.join(DIST_DIR, "rehber", a["slug"])
        os.makedirs(art_dir, exist_ok=True)
        art_html = build_article_page(a)
        with open(os.path.join(art_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(art_html)
        print(f" -> dist/rehber/{a['slug']}/index.html compiled.")

    # 4. Sitemap & Robots
    with open(os.path.join(DIST_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(build_sitemap(articles))
    print(" -> dist/sitemap.xml compiled.")

    with open(os.path.join(DIST_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(build_robots_txt())
    print(" -> dist/robots.txt compiled.")

    # 5. Mirror to docs/ for GitHub Pages
    import shutil
    docs_dir = os.path.join(BASE_DIR, "docs")
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)
    shutil.copytree(DIST_DIR, docs_dir)
    print(" -> Mirrored dist/ to docs/ for GitHub Pages.")

    print(f"[ENGINE] All pages compiled successfully into dist/ and docs/. Total articles: {len(articles)}")


if __name__ == "__main__":
    compile_site()
