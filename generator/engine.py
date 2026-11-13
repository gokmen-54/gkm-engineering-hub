"""
GKM Elektrik & Mühendislik - Programmatic Engineering Hub SSG Compiler
Ultra High-End Corporate Frontend matching gkmelektrik.com
Features:
- Real assets, official logos, brand marquee, project showcase
- Programmatic SEO articles with SVG schematics
- Curated & Live Interactive Engineering Q&A (Discussions Engine)
- 3 Interactive Industrial Engineering Calculators (/hesaplama/)
- Real-World Industrial Project Case Studies (/projeler/)
- Password-Protected Admin Panel (/admin/)
"""

import os
import glob
import re
import json
import shutil
import urllib.parse
from datetime import datetime
from svg_generator import generate_svg_diagram
from calculators_page import generate_calculators_page
from projects_page import generate_projects_page
from admin_page import generate_admin_page

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(BASE_DIR, "content")
DIST_DIR = os.path.join(BASE_DIR, "dist")
DOCS_DIR = os.path.join(BASE_DIR, "docs")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
DISCUSSIONS_FILE = os.path.join(BASE_DIR, "generator", "discussions_database.json")
PROJECTS_FILE = os.path.join(BASE_DIR, "generator", "projects_database.json")

SITE_URL = "https://gokmen-54.github.io/gkm-engineering-hub"
MAIN_WEBSITE = "https://gkmelektrik.com"
WHATSAPP_PHONE = "905377029954"
PHONE_DISPLAY = "0537 702 99 54"

CATEGORIES = {
    "makine-otomasyonu": {
        "title": "Makine Otomasyonu",
        "desc": "Özel makine otomasyon yazılımları, servo/step motor senkronizasyonu, hat revizyonu ve elektronik kamlama çözümleri.",
        "icon": "⚙️",
        "color": "sky",
        "img": "assets/gkm_7_robotik_hat.webp"
    },
    "plc-scada-yazilim": {
        "title": "PLC & SCADA Yazılım",
        "desc": "Siemens, Schneider ve Beckhoff PLC programlama, SCADA mimarisi, Endüstriyel IoT ve Modbus/MQTT veri toplama.",
        "icon": "💻",
        "color": "blue",
        "img": "assets/gkm_1_fabrika_otomasyon.webp"
    },
    "pcb-elektronik-tasarim": {
        "title": "PCB & Elektronik Tasarım",
        "desc": "Çok katmanlı endüstriyel elektronik kart tasarımı, Altium/KiCad şematiği, STM32/ESP32 gömülü yazılım ve prototipleme.",
        "icon": "⚡",
        "color": "emerald",
        "img": "assets/gkm_3_otomasyon.webp"
    },
    "elektrik-panosu-salt": {
        "title": "Elektrik Panosu & Şalt",
        "desc": "Tip testli Ana Dağıtım (ADP), MCC motor kontrol panoları, harmonik filtreli kompanzasyon ve toptan şalt tedariği.",
        "icon": "🛡️",
        "color": "amber",
        "img": "assets/gkm_6_fabrika_da__t_m_panosu.webp"
    }
}

MARQUEE_PROJECTS = [
    {
        "title": "Ana Dağıtım & ADP Pano İmalatı",
        "desc": "IEC 61439 Form 4b Tip Testli İmalat",
        "img": "assets/gkm_6_fabrika_da__t_m_panosu.webp",
        "tag": "Pano İmalatı"
    },
    {
        "title": "Robotik Hat & Makine Otomasyonu",
        "desc": "Çok Eksenli Servo Senkronizasyonu",
        "img": "assets/gkm_7_robotik_hat.webp",
        "tag": "Makine Otomasyonu"
    },
    {
        "title": "Fabrika Dağıtım & PLC / SCADA",
        "desc": "Siemens S7-1500 TIA Portal Entegrasyonu",
        "img": "assets/gkm_1_fabrika_otomasyon.webp",
        "tag": "Endüstriyel Yazılım"
    },
    {
        "title": "Harmonik Filtreli Kompanzasyon",
        "desc": "189 Hz %7 De-Tuned Reaktörlü Pano",
        "img": "assets/gkm_8_kompanzasyon.webp",
        "tag": "Enerji Kalitesi"
    },
    {
        "title": "MCC Motor Kontrol & Sürücü Panoları",
        "desc": "VFD & Soft Starter Güç Dağıtımı",
        "img": "assets/gkm_4_pano_donan_m_.webp",
        "tag": "MCC Panoları"
    },
    {
        "title": "Endüstriyel Busbar & Şalt Altyapısı",
        "desc": "Yüksek Akım Güç İletim Hatları",
        "img": "assets/gkm_9_plaza_busbar.webp",
        "tag": "Tesis Altyapısı"
    }
]

BRANDS = [
    "Siemens", "Schneider Electric", "ABB", "Eaton",
    "Phoenix Contact", "Weidmüller", "Omron", "Delta Electronics", "Beckhoff Automation"
]


def urllib_quote(text):
    return urllib.parse.quote(text)


def load_discussions():
    if os.path.exists(DISCUSSIONS_FILE):
        try:
            with open(DISCUSSIONS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def load_projects():
    if os.path.exists(PROJECTS_FILE):
        try:
            with open(PROJECTS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


def parse_frontmatter(content):
    meta = {}
    body = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            body = parts[2]
            for line in fm_text.strip().splitlines():
                if ":" in line:
                    key, val = line.split(":", 1)
                    meta[key.strip()] = val.strip().strip('"').strip("'")
    return meta, body.strip()


def markdown_to_html(md):
    lines = md.splitlines()
    html_lines = []
    in_code = False
    code_lang = ""
    code_buffer = []

    for line in lines:
        if line.startswith("```"):
            if not in_code:
                in_code = True
                code_lang = line[3:].strip()
                code_buffer = []
            else:
                in_code = False
                escaped_code = (
                    "\n".join(code_buffer)
                    .replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                )
                html_lines.append(
                    f'<div class="my-6 rounded-2xl overflow-hidden border border-slate-700 bg-slate-950 shadow-xl">'
                    f'<div class="bg-slate-900 px-4 py-2 text-[11px] font-mono text-sky-400 font-bold border-b border-slate-800 flex items-center justify-between">'
                    f'<span>{code_lang.upper() if code_lang else "KOD ÖRNEĞİ"}</span>'
                    f'<span class="text-slate-500">GKM Endüstriyel Standart</span>'
                    f'</div>'
                    f'<pre class="p-4 text-xs font-mono text-emerald-300 overflow-x-auto leading-relaxed">{escaped_code}</pre>'
                    f'</div>'
                )
            continue

        if in_code:
            code_buffer.append(line)
            continue

        # Headings
        if line.startswith("### "):
            html_lines.append(f'<h3 class="text-xl font-black text-slate-900 mt-8 mb-3 flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-sky-500"></span>{line[4:].strip()}</h3>')
        elif line.startswith("## "):
            html_lines.append(f'<h2 class="text-2xl sm:text-3xl font-black text-slate-950 mt-10 mb-4 pb-2 border-b border-slate-200">{line[3:].strip()}</h2>')
        elif line.startswith("# "):
            html_lines.append(f'<h1 class="text-3xl sm:text-4xl font-black text-slate-950 mb-6">{line[2:].strip()}</h1>')
        elif line.startswith("> "):
            html_lines.append(f'<blockquote class="border-l-4 border-sky-500 bg-sky-50/70 text-slate-800 p-4 my-6 rounded-r-2xl text-sm font-medium leading-relaxed italic">{line[2:].strip()}</blockquote>')
        elif line.startswith("- "):
            html_lines.append(f'<li class="text-slate-700 text-sm sm:text-base leading-relaxed ml-4 list-disc mb-1.5">{line[2:].strip()}</li>')
        elif re.match(r"^\d+\.\s", line):
            content = re.sub(r"^\d+\.\s", "", line)
            html_lines.append(f'<li class="text-slate-700 text-sm sm:text-base leading-relaxed ml-4 list-decimal mb-1.5">{content.strip()}</li>')
        elif line.strip() == "":
            html_lines.append('<div class="h-3"></div>')
        else:
            p_text = line
            p_text = re.sub(r"\*\*(.*?)\*\*", r"<strong class='font-black text-slate-900'>\1</strong>", p_text)
            p_text = re.sub(r"`(.*?)`", r"<code class='bg-slate-100 text-sky-700 font-mono text-xs px-1.5 py-0.5 rounded border border-slate-200'>\1</code>", p_text)
            html_lines.append(f'<p class="text-slate-700 text-sm sm:text-base leading-relaxed mb-4">{p_text}</p>')

    return "\n".join(html_lines)


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
    <!-- Top Announcement Bar (Deep Navy matching gkmelektrik.com) -->
    <div class="bg-[#001c30] text-slate-300 text-xs py-2.5 px-4 border-b border-sky-950">
        <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
            <div class="flex items-center gap-2">
                <span class="inline-block w-2 h-2 rounded-full bg-sky-400 animate-pulse"></span>
                <span class="font-bold text-white">GKM Elektrik & Mühendislik:</span>
                <span class="hidden md:inline text-slate-300">Özel Makine Otomasyonu, PLC/SCADA, PCB ve Tip Testli Pano İmalatı</span>
            </div>
            <div class="flex items-center gap-5 text-xs font-semibold">
                <a href="{SITE_URL}/hesaplama/" class="text-amber-400 hover:text-amber-300 flex items-center gap-1 transition">
                    <span>⚡ <b>Mühendislik Hesaplama Araçları</b></span>
                </a>
                <a href="{MAIN_WEBSITE}" target="_blank" class="text-sky-400 hover:text-sky-300 flex items-center gap-1 transition hidden sm:flex">
                    <span>Resmi Şalt Mağazası: <b>gkmelektrik.com</b></span> ➔
                </a>
                <a href="tel:{WHATSAPP_PHONE}" class="text-slate-300 hover:text-white hidden lg:flex items-center gap-1">
                    <span>📞 {PHONE_DISPLAY}</span>
                </a>
            </div>
        </div>
    </div>

    <!-- Main Clean Navigation Header (White with backdrop blur) -->
    <header class="bg-white/95 backdrop-blur-md border-b border-slate-200 sticky top-0 z-50 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 h-20 flex items-center justify-between gap-4">
            
            <!-- Real Official Logo from gkmelektrik.com -->
            <a href="{SITE_URL}/" class="flex items-center gap-3">
                <img src="{SITE_URL}/assets/logo.webp" alt="Gökmen Elektrik Logo" class="h-10 sm:h-12 w-auto object-contain">
                <div class="border-l border-slate-200 pl-3 hidden sm:block">
                    <span class="text-xs font-black tracking-wider text-slate-900 block uppercase">MÜHENDİSLİK HUB</span>
                    <span class="text-[10px] text-sky-700 font-bold uppercase tracking-wider block">Endüstriyel Otomasyon & Ar-Ge</span>
                </div>
            </a>

            <!-- Nav Links -->
            <nav class="hidden xl:flex items-center gap-6 text-xs sm:text-sm font-bold text-slate-700">
                <a href="{SITE_URL}/makine-otomasyonu/" class="hover:text-sky-600 transition {'text-sky-600 border-b-2 border-sky-600 pb-1' if active_nav == 'makine-otomasyonu' else ''}">Makine Otomasyonu</a>
                <a href="{SITE_URL}/plc-scada-yazilim/" class="hover:text-sky-600 transition {'text-sky-600 border-b-2 border-sky-600 pb-1' if active_nav == 'plc-scada-yazilim' else ''}">PLC & SCADA</a>
                <a href="{SITE_URL}/pcb-elektronik-tasarim/" class="hover:text-sky-600 transition {'text-sky-600 border-b-2 border-sky-600 pb-1' if active_nav == 'pcb-elektronik-tasarim' else ''}">PCB Tasarımı</a>
                <a href="{SITE_URL}/elektrik-panosu-salt/" class="hover:text-sky-600 transition {'text-sky-600 border-b-2 border-sky-600 pb-1' if active_nav == 'elektrik-panosu-salt' else ''}">Pano & Şalt</a>
                <a href="{SITE_URL}/projeler/" class="hover:text-sky-600 transition {'text-sky-600 border-b-2 border-sky-600 pb-1' if active_nav == 'projeler' else ''}">Vaka Analizleri</a>
                <a href="{SITE_URL}/hesaplama/" class="hover:text-sky-600 transition text-amber-600 flex items-center gap-1.5 {'font-extrabold underline' if active_nav == 'hesaplama' else ''}">
                    <span>📐 Hesaplama</span>
                    <span class="bg-amber-100 text-amber-800 text-[10px] font-black px-1.5 py-0.5 rounded-full uppercase">Ücretsiz</span>
                </a>
            </nav>

            <!-- Conversion Action Buttons -->
            <div class="flex items-center gap-3">
                <a href="{MAIN_WEBSITE}" target="_blank" class="hidden md:inline-flex bg-slate-100 hover:bg-slate-200 text-slate-800 text-xs font-bold py-2.5 px-3.5 rounded-xl border border-slate-300 transition">
                    gkmelektrik.com ↗
                </a>

                <a href="https://wa.me/{WHATSAPP_PHONE}?text={urllib_quote('Merhaba GKM Elektrik, mühendislik projemiz için teknik görüşme ve teklif almak istiyoruz.')}" target="_blank" rel="noopener" class="bg-[#25D366] hover:bg-[#20ba5c] text-white font-black text-xs sm:text-sm py-2.5 px-4 sm:px-5 rounded-full shadow-lg shadow-emerald-500/20 transition flex items-center gap-2">
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
    <div class="lg:hidden fixed bottom-0 left-0 right-0 z-50 bg-white/95 border-t border-slate-200 backdrop-blur-lg px-4 py-2.5 flex items-center justify-between gap-2 shadow-2xl">
        <a href="{SITE_URL}/hesaplama/" class="flex-1 bg-amber-500 hover:bg-amber-600 text-slate-950 font-black text-xs py-2.5 px-2 rounded-xl flex items-center justify-center gap-1 shadow">
            📐 Hesaplayıcılar
        </a>
        <a href="https://wa.me/{WHATSAPP_PHONE}?text={urllib_quote('Merhaba GKM Elektrik, teknik projemiz için şema/liste gönderip teklif almak istiyoruz.')}" target="_blank" class="flex-1 bg-[#25D366] hover:bg-[#20ba5c] text-white font-black text-xs py-2.5 px-2 rounded-xl shadow-lg shadow-emerald-500/25 flex items-center justify-center gap-1">
            <span>WhatsApp Şema Gönder</span>
        </a>
    </div>

    <!-- Corporate Footer (Deep Navy) -->
    <footer class="border-t border-slate-200 bg-[#001c30] text-slate-400 text-xs py-14 pb-24 lg:pb-14">
        <div class="max-w-7xl mx-auto px-4 sm:px-6">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8 pb-10 border-b border-slate-800">
                <div class="md:col-span-1">
                    <img src="{SITE_URL}/assets/logo.webp" alt="Gökmen Elektrik Logo" class="h-10 w-auto object-contain brightness-0 invert mb-4">
                    <p class="text-slate-300 leading-relaxed text-xs mb-4">
                        Özel makine otomasyonu, PLC/SCADA yazılımı, çok katmanlı endüstriyel PCB tasarımı ve IEC 61439 tip testli pano imalatı.
                    </p>
                    <a href="{MAIN_WEBSITE}" target="_blank" class="text-sky-400 font-bold hover:underline block mb-2">
                        ➔ Resmi E-Ticaret: gkmelektrik.com
                    </a>
                    <a href="{SITE_URL}/admin/" class="text-slate-500 hover:text-slate-400 font-semibold block text-[11px]">
                        🔐 Soru-Cevap Yönetici Girişi
                    </a>
                </div>

                <div>
                    <h4 class="font-bold text-white uppercase text-xs tracking-wider mb-3">Mühendislik Çözümleri</h4>
                    <ul class="space-y-2">
                        <li><a href="{SITE_URL}/makine-otomasyonu/" class="hover:text-sky-400 transition">Makine Otomasyonu & Servo</a></li>
                        <li><a href="{SITE_URL}/plc-scada-yazilim/" class="hover:text-sky-400 transition">PLC Programlama & SCADA</a></li>
                        <li><a href="{SITE_URL}/pcb-elektronik-tasarim/" class="hover:text-sky-400 transition">Özel PCB & Gömülü Sistemler</a></li>
                        <li><a href="{SITE_URL}/elektrik-panosu-salt/" class="hover:text-sky-400 transition">Tip Testli Pano & Kompanzasyon</a></li>
                        <li><a href="{SITE_URL}/projeler/" class="hover:text-sky-400 transition">Gerçek Vaka Analizleri</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="font-bold text-white uppercase text-xs tracking-wider mb-3">Hesaplama Araçları (0 TL)</h4>
                    <ul class="space-y-2 text-slate-300">
                        <li><a href="{SITE_URL}/hesaplama/#kompanzasyon-hesabi" class="hover:text-amber-400 transition">📊 Harmonik Kompanzasyon Hesabı</a></li>
                        <li><a href="{SITE_URL}/hesaplama/#kablo-kesiti-hesabi" class="hover:text-amber-400 transition">🔌 IEC Kablo Kesiti & Gerilim Düşümü</a></li>
                        <li><a href="{SITE_URL}/hesaplama/#servo-tork-hesabi" class="hover:text-amber-400 transition">⚙️ Servo Motor Tork & Güç Seçimi</a></li>
                        <li><a href="{SITE_URL}/admin/" class="hover:text-sky-400 transition">💬 Soru & Tartışma Yönetimi</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="font-bold text-white uppercase text-xs tracking-wider mb-3">İletişim & Fabrika Destek</h4>
                    <ul class="space-y-2 text-slate-300 mb-4">
                        <li><b>Telefon:</b> <a href="tel:{WHATSAPP_PHONE}" class="hover:text-white">{PHONE_DISPLAY}</a></li>
                        <li><b>WhatsApp Destek:</b> <a href="https://wa.me/{WHATSAPP_PHONE}" target="_blank" class="hover:text-emerald-400">+90 537 702 99 54</a></li>
                        <li><b>Hizmet Sahası:</b> Sakarya, Kocaeli, Gebze, Bursa, Marmara & Tüm Türkiye</li>
                    </ul>
                    <a href="https://wa.me/{WHATSAPP_PHONE}?text={urllib_quote('Merhaba, projemiz için teknik döküman paylaşmak istiyoruz.')}" target="_blank" class="inline-block bg-sky-600 hover:bg-sky-500 text-white px-4 py-2 rounded-xl text-xs font-bold transition shadow-md">
                        Şema & Liste Gönder ➔
                    </a>
                </div>
            </div>

            <div class="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-[11px] text-slate-400">
                <p>© 2026 GKM Elektrik & Otomasyon Sistemleri. Tüm hakları saklıdır.</p>
                <p>Programmatic Engineering Hub • Yüksek Performanslı Teknik Blog ve Müşteri Yakalama Motoru</p>
            </div>
        </div>
    </footer>
    """


def build_homepage(articles):
    header = get_base_header(active_nav="")
    footer = get_base_footer()

    # Brand badges HTML
    brands_html = "".join([
        f'<div class="flex items-center gap-2 bg-white border border-slate-200 px-5 py-2.5 rounded-xl shadow-sm font-bold text-xs text-slate-800 whitespace-nowrap">'
        f'<span class="w-2 h-2 rounded-full bg-sky-500"></span>{b}'
        f'</div>'
        for b in BRANDS * 2
    ])

    # Real project marquee cards HTML
    project_cards = []
    for p in MARQUEE_PROJECTS:
        wa_text = urllib_quote(f"Merhaba GKM Elektrik, {p['title']} benzeri projemiz için bilgi ve teklif almak istiyoruz.")
        project_cards.append(
            f'<div class="flex-none w-[320px] bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-md hover:shadow-xl hover:border-sky-500 transition duration-300 flex flex-col">'
            f'<div class="h-48 overflow-hidden bg-slate-900 relative">'
            f'<img src="{SITE_URL}/{p["img"]}" alt="{p["title"]}" class="w-full h-full object-cover hover:scale-105 transition duration-500">'
            f'<span class="absolute top-3 left-3 bg-sky-600 text-white font-extrabold text-[10px] px-2.5 py-1 rounded-full uppercase shadow">{p["tag"]}</span>'
            f'</div>'
            f'<div class="p-4 flex-1 flex flex-col justify-between">'
            f'<div>'
            f'<h4 class="font-black text-slate-900 text-sm leading-snug mb-1">{p["title"]}</h4>'
            f'<p class="text-slate-500 text-xs font-medium">{p["desc"]}</p>'
            f'</div>'
            f'<a href="https://wa.me/{WHATSAPP_PHONE}?text={wa_text}" target="_blank" class="mt-3 text-sky-600 hover:text-sky-700 text-xs font-bold flex items-center gap-1">'
            f'<span>Detay & Teklif Al</span> ➔'
            f'</a>'
            f'</div>'
            f'</div>'
        )
    project_cards_html = "".join(project_cards)

    # Articles HTML (Daily Presentation Feed)
    cards_html = ""
    for a in articles:
        cat_info = CATEGORIES.get(a["category"], {})
        cat_img = cat_info.get("img", "assets/gkm_0_g_kmen_elektrik__amp__otomasyo.webp")

        cards_html += f"""
        <article class="bg-white rounded-2xl border border-slate-200 hover:border-sky-500 transition-all duration-300 hover:shadow-xl hover:-translate-y-1 flex flex-col justify-between overflow-hidden group">
            <div class="h-44 bg-slate-900 relative overflow-hidden">
                <img src="{SITE_URL}/{cat_img}" alt="{a['title']}" class="w-full h-full object-cover opacity-90 group-hover:scale-105 group-hover:opacity-100 transition duration-500">
                <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent"></div>
                <span class="absolute bottom-3 left-3 bg-white text-slate-900 font-extrabold text-[10px] px-3 py-1 rounded-full uppercase shadow">
                    {a.get('category_title', 'Mühendislik')}
                </span>
            </div>

            <div class="p-6 flex-1 flex flex-col justify-between">
                <div>
                    <div class="flex items-center justify-between text-xs font-bold text-slate-400 mb-2">
                        <span class="text-sky-600 font-extrabold">⏱️ {a.get('reading_time', '7 dk')}</span>
                        <span>📅 {a.get('date', 'Güncel')}</span>
                    </div>

                    <h3 class="text-base sm:text-lg font-black text-slate-900 leading-snug group-hover:text-sky-600 transition mb-3">
                        <a href="{SITE_URL}/rehber/{a['slug']}/">{a['title']}</a>
                    </h3>

                    <p class="text-slate-600 text-xs sm:text-sm line-clamp-3 leading-relaxed mb-6 font-medium">
                        {a['summary']}
                    </p>
                </div>

                <div class="pt-4 border-t border-slate-100 flex items-center justify-between">
                    <span class="text-[11px] font-semibold text-slate-500">🎯 {a.get('target_audience', 'Mühendisler')}</span>
                    <a href="{SITE_URL}/rehber/{a['slug']}/" class="text-sky-600 hover:text-sky-700 font-bold text-xs flex items-center gap-1 group-hover:translate-x-1 transition">
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
    <meta name="description" content="Gökmen Elektrik: Özel makine otomasyonu, Siemens/Beckhoff PLC ve SCADA yazılımı, 4 katmanlı PCB tasarımı, IEC 61439 tip testli pano imalatı ve şalt çözümleri.">
    <meta name="keywords" content="gökmen elektrik, makine otomasyonu, plc programlama, scada yazılımı, pcb tasarımı, gömülü sistemler, elektrik panosu imalatı, kompanzasyon, sakarya elektrik, kocaeli otomasyon">
    <link rel="canonical" href="{SITE_URL}/">

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap');
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
        
        .gkm-watermark {{
            font-size: clamp(40px, 8vw, 120px);
            font-weight: 900;
            color: transparent;
            -webkit-text-stroke: 1.5px rgba(255, 255, 255, 0.08);
            letter-spacing: -2px;
            line-height: 0.85;
            user-select: none;
            pointer-events: none;
            text-transform: uppercase;
        }}

        @keyframes marquee {{
            0% {{ transform: translateX(0); }}
            100% {{ transform: translateX(-50%); }}
        }}
        .animate-marquee {{
            display: flex;
            width: max-content;
            animation: marquee 25s linear infinite;
        }}
        .animate-marquee:hover {{
            animation-play-state: paused;
        }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased selection:bg-sky-500 selection:text-white min-h-screen flex flex-col justify-between">

    {header}

    <!-- Hero Section -->
    <section class="relative bg-gradient-to-br from-[#001c30] via-[#001726] to-[#00111f] text-white pt-14 pb-16 border-b border-sky-950 overflow-hidden">
        <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#38bdf8_1px,transparent_1px)] [background-size:16px_16px] pointer-events-none"></div>
        
        <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
                
                <!-- Left Column -->
                <div class="lg:col-span-7 text-left">
                    <div class="gkm-watermark mb-2">GKM ELEKTRİK</div>
                    
                    <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-sky-900/60 border border-sky-400/30 text-sky-300 text-xs font-bold mb-4">
                        <span>⚡ GÖKMEN ELEKTRİK & OTOMASYON MÜHENDİSLİK SİSTEMLERİ</span>
                    </div>

                    <h1 class="text-3xl sm:text-5xl font-black text-white tracking-tight leading-tight mb-4">
                        Özel Makine Otomasyonu, <span class="text-sky-400">Gömülü PCB Tasarımı</span> ve Tip Testli Pano İmalatı
                    </h1>

                    <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-8 max-w-2xl font-medium">
                        Endüstriyel tesisleriniz ve makine imalat projeleriniz için komple mühendislik: PLC/SCADA yazılımı, yüksek hassasiyetli servo kontrolü, 4 katmanlı EMC uyumlu PCB üretimi ve IEC 61439 tip testli pano çözümleri tek çatı altında.
                    </p>

                    <!-- Hero Action Buttons -->
                    <div class="flex flex-wrap items-center gap-3">
                        <a href="https://wa.me/{WHATSAPP_PHONE}?text={urllib_quote('Merhaba GKM Elektrik, projemiz için şema/şartname gönderip teknik teklif almak istiyoruz.')}" target="_blank" class="bg-[#25D366] hover:bg-[#20ba5c] text-white font-black text-sm py-3.5 px-6 rounded-2xl shadow-xl shadow-emerald-500/20 transition transform hover:scale-105 flex items-center gap-2">
                            <span>💬 WhatsApp ile Şema / Proje Danış</span>
                        </a>
                        
                        <a href="{SITE_URL}/hesaplama/" class="bg-amber-500 hover:bg-amber-400 text-slate-950 font-black text-sm py-3.5 px-6 rounded-2xl shadow-lg transition flex items-center gap-2">
                            <span>📐 Ücretsiz Hesaplama Araçları</span> ➔
                        </a>
                    </div>

                    <!-- Industrial Trust Badges -->
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-10 pt-8 border-t border-slate-800/80 text-left">
                        <div>
                            <span class="text-xl font-black text-sky-400 block">IEC 61439</span>
                            <span class="text-[11px] text-slate-400 font-semibold">Tip Testli Pano</span>
                        </div>
                        <div>
                            <span class="text-xl font-black text-emerald-400 block">TIA & SCL</span>
                            <span class="text-[11px] text-slate-400 font-semibold">Siemens & Beckhoff</span>
                        </div>
                        <div>
                            <span class="text-xl font-black text-amber-400 block">4-Katman EMC</span>
                            <span class="text-[11px] text-slate-400 font-semibold">Endüstriyel PCB</span>
                        </div>
                        <div>
                            <span class="text-xl font-black text-indigo-400 block">7/24 Saha</span>
                            <span class="text-[11px] text-slate-400 font-semibold">Devreye Alma</span>
                        </div>
                    </div>
                </div>

                <!-- Right Column: Workshop Image -->
                <div class="lg:col-span-5">
                    <div class="relative rounded-3xl overflow-hidden border-2 border-sky-400/30 shadow-2xl bg-slate-900 group">
                        <img src="{SITE_URL}/assets/gkm_0_g_kmen_elektrik__amp__otomasyo.webp" alt="Gökmen Elektrik & Otomasyon - Pano İmalatı ve Atölye" class="w-full h-[400px] object-cover group-hover:scale-105 transition duration-700">
                        <div class="absolute inset-0 bg-gradient-to-t from-[#001c30] via-transparent to-transparent"></div>
                        <div class="absolute bottom-4 left-4 right-4 bg-white/90 backdrop-blur-md rounded-2xl p-4 border border-slate-200 text-slate-900">
                            <div class="flex items-center gap-2 text-xs font-black text-sky-700 uppercase mb-1">
                                <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
                                <span>GÖKMEN ELEKTRİK SAHA EKİBİ & İMALAT</span>
                            </div>
                            <p class="text-xs font-bold text-slate-700 leading-snug">
                                Kendi atölyemizde tip testli pano montajı, kablaj ve test süreçleri uzman mühendis kadromuzla yürütülmektedir.
                            </p>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Interactive Free Engineering Tools Callout Banner -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 -mt-6 z-20 relative">
        <div class="bg-gradient-to-r from-amber-500 via-amber-400 to-yellow-500 rounded-3xl p-6 sm:p-8 text-slate-950 shadow-2xl border border-amber-300 flex flex-col md:flex-row items-center justify-between gap-6">
            <div class="flex items-center gap-4">
                <div class="w-14 h-14 rounded-2xl bg-slate-950 text-amber-400 flex items-center justify-center text-3xl font-black shadow">
                    📐
                </div>
                <div>
                    <span class="bg-slate-950 text-white font-extrabold text-[10px] px-2.5 py-1 rounded-full uppercase tracking-wider mb-1 inline-block">MÜHENDİSLİK HESAPLAMA MOTORU</span>
                    <h3 class="text-lg sm:text-2xl font-black leading-tight">
                        Kompanzasyon, Kablo Kesiti & Servo Tork Hesaplayıcı
                    </h3>
                    <p class="text-xs sm:text-sm font-semibold text-slate-900 mt-0.5">
                        IEC standartlarında reaktif ceza, kablo gerilim düşümü ve motor güç hesabını tarayıcınızda 0 TL ile anında yapın.
                    </p>
                </div>
            </div>
            <a href="{SITE_URL}/hesaplama/" class="bg-slate-950 hover:bg-slate-900 text-white font-black text-xs sm:text-sm py-3.5 px-6 rounded-2xl transition shadow-xl whitespace-nowrap">
                Hesaplama Aracını Başlat ➔
            </a>
        </div>
    </section>

    <!-- Infinite Brand Ticker -->
    <section class="bg-white border-b border-slate-200 py-5 overflow-hidden mt-8">
        <div class="max-w-7xl mx-auto px-4 mb-2 text-center">
            <span class="text-[10px] font-black uppercase tracking-widest text-slate-400">Çözüm Ortağı Olduğumuz Dünya Standartlarında Markalar</span>
        </div>
        <div class="flex overflow-hidden">
            <div class="animate-marquee flex items-center gap-4 py-2">
                {brands_html}
            </div>
        </div>
    </section>

    <!-- 4 Core Service Pillars -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 py-16">
        <div class="mb-10 text-center">
            <span class="text-xs font-black text-sky-600 uppercase tracking-widest block mb-1">MÜHENDİSLİK DİSİPLİNLERİMİZ</span>
            <h2 class="text-2xl sm:text-4xl font-black text-slate-950">Fabrikalar ve Makine İmalatçıları İçin Çözümler</h2>
            <p class="text-slate-500 text-sm max-w-2xl mx-auto mt-2">Aradığınız mühendislik alanına tıklayarak hazır vaka analizlerini ve teknik rehberleri inceleyebilirsiniz.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            
            <a href="{SITE_URL}/makine-otomasyonu/" class="bg-white p-6 rounded-2xl border border-slate-200 hover:border-sky-500 hover:shadow-xl transition flex flex-col justify-between group">
                <div>
                    <div class="h-36 rounded-xl overflow-hidden mb-4 bg-slate-900">
                        <img src="{SITE_URL}/assets/gkm_7_robotik_hat.webp" alt="Makine Otomasyonu" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                    </div>
                    <h3 class="text-lg font-black text-slate-900 mb-2 group-hover:text-sky-600 transition">Makine Otomasyonu</h3>
                    <p class="text-slate-600 text-xs leading-relaxed mb-4 font-medium">
                        Elektronik kamlama, çok eksenli servo senkronizasyonu, hat revizyonları ve paketleme/dolum makineleri yazılımı.
                    </p>
                </div>
                <span class="text-sky-600 text-xs font-black flex items-center gap-1 group-hover:translate-x-1 transition">Rehberleri İncele ➔</span>
            </a>

            <a href="{SITE_URL}/plc-scada-yazilim/" class="bg-white p-6 rounded-2xl border border-slate-200 hover:border-sky-500 hover:shadow-xl transition flex flex-col justify-between group">
                <div>
                    <div class="h-36 rounded-xl overflow-hidden mb-4 bg-slate-900">
                        <img src="{SITE_URL}/assets/gkm_1_fabrika_otomasyon.webp" alt="PLC & SCADA" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                    </div>
                    <h3 class="text-lg font-black text-slate-900 mb-2 group-hover:text-sky-600 transition">PLC & SCADA Yazılım</h3>
                    <p class="text-slate-600 text-xs leading-relaxed mb-4 font-medium">
                        Siemens TIA SCL, Beckhoff TwinCAT, WinCC/Ignition SCADA ve Modbus/MQTT Endüstriyel IoT veri toplama.
                    </p>
                </div>
                <span class="text-sky-600 text-xs font-black flex items-center gap-1 group-hover:translate-x-1 transition">Rehberleri İncele ➔</span>
            </a>

            <a href="{SITE_URL}/pcb-elektronik-tasarim/" class="bg-white p-6 rounded-2xl border border-slate-200 hover:border-sky-500 hover:shadow-xl transition flex flex-col justify-between group">
                <div>
                    <div class="h-36 rounded-xl overflow-hidden mb-4 bg-slate-900">
                        <img src="{SITE_URL}/assets/gkm_3_otomasyon.webp" alt="Özel PCB" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                    </div>
                    <h3 class="text-lg font-black text-slate-900 mb-2 group-hover:text-sky-600 transition">Özel PCB & Gömülü</h3>
                    <p class="text-slate-600 text-xs leading-relaxed mb-4 font-medium">
                        Çok katmanlı endüstriyel PCB tasarımı, STM32/ESP32 gömülü yazılım, optokuplör izolasyonlu I/O kartları.
                    </p>
                </div>
                <span class="text-sky-600 text-xs font-black flex items-center gap-1 group-hover:translate-x-1 transition">Rehberleri İncele ➔</span>
            </a>

            <a href="{SITE_URL}/elektrik-panosu-salt/" class="bg-white p-6 rounded-2xl border border-slate-200 hover:border-sky-500 hover:shadow-xl transition flex flex-col justify-between group">
                <div>
                    <div class="h-36 rounded-xl overflow-hidden mb-4 bg-slate-900">
                        <img src="{SITE_URL}/assets/gkm_6_fabrika_da__t_m_panosu.webp" alt="Pano İmalatı" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                    </div>
                    <h3 class="text-lg font-black text-slate-900 mb-2 group-hover:text-sky-600 transition">Pano İmalatı & Şalt</h3>
                    <p class="text-slate-600 text-xs leading-relaxed mb-4 font-medium">
                        Tip testli ADP ana dağıtım, MCC sürücü panoları, de-tuned %7 reaktörlü harmonik kompanzasyon panoları.
                    </p>
                </div>
                <span class="text-sky-600 text-xs font-black flex items-center gap-1 group-hover:translate-x-1 transition">Rehberleri İncele ➔</span>
            </a>

        </div>
    </section>

    <!-- Real Project Showcase Carousel -->
    <section class="bg-slate-100 py-14 border-y border-slate-200 overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 mb-6 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
            <div>
                <span class="text-xs font-black text-sky-600 uppercase tracking-widest block">GERÇEK İMALAT & SAHA ÇÖZÜMLERİMİZ</span>
                <h3 class="text-xl sm:text-2xl font-black text-slate-900">Gökmen Elektrik Proje Galerisi & Referanslar</h3>
            </div>
            <div class="flex items-center gap-3">
                <a href="{SITE_URL}/projeler/" class="bg-sky-600 hover:bg-sky-700 text-white text-xs font-bold py-2 px-4 rounded-xl shadow transition">
                    Tüm Vaka Analizleri ➔
                </a>
            </div>
        </div>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 overflow-x-auto pb-4 scrollbar-none">
            <div class="flex gap-5 w-max">
                {project_cards_html}
            </div>
        </div>
    </section>

    <!-- Daily Technical Blog & Client Presentation Feed -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 py-16 flex-1 w-full">
        <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 mb-10 pb-4 border-b border-slate-200">
            <div>
                <span class="text-xs font-black text-sky-600 uppercase tracking-widest block mb-1">PROGRAMMATIC ENGINEERING BLOG</span>
                <h2 class="text-2xl sm:text-3xl font-black text-slate-950">Günlük Teknik Rehberler & Mühendislik Vaka Analizleri</h2>
            </div>
            <span class="bg-sky-100 text-sky-900 font-extrabold text-xs px-3.5 py-1.5 rounded-full border border-sky-300">
                ⚡ 7/24 Otomatik Güncellenir
            </span>
        </div>

        <!-- Filter Badges -->
        <div class="flex flex-wrap items-center gap-2 mb-8 text-xs font-bold">
            <span class="bg-slate-900 text-white px-4 py-2 rounded-full cursor-pointer">Tüm Konular ({len(articles)})</span>
            <a href="{SITE_URL}/makine-otomasyonu/" class="bg-white hover:bg-slate-100 text-slate-700 border border-slate-300 px-4 py-2 rounded-full transition">⚙️ Makine Otomasyonu</a>
            <a href="{SITE_URL}/plc-scada-yazilim/" class="bg-white hover:bg-slate-100 text-slate-700 border border-slate-300 px-4 py-2 rounded-full transition">💻 PLC & SCADA</a>
            <a href="{SITE_URL}/pcb-elektronik-tasarim/" class="bg-white hover:bg-slate-100 text-slate-700 border border-slate-300 px-4 py-2 rounded-full transition">⚡ PCB Tasarımı</a>
            <a href="{SITE_URL}/elektrik-panosu-salt/" class="bg-white hover:bg-slate-100 text-slate-700 border border-slate-300 px-4 py-2 rounded-full transition">🛡️ Pano & Şalt</a>
            <a href="{SITE_URL}/projeler/" class="bg-sky-50 text-sky-700 border border-sky-300 px-4 py-2 rounded-full transition">🏭 Vaka Analizleri</a>
        </div>

        <!-- Grid of Articles -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
            {cards_html}
        </div>
    </main>

    <!-- Bottom Conversion Banner -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 pb-16">
        <div class="bg-gradient-to-r from-[#001c30] to-[#00111f] rounded-3xl p-8 sm:p-12 text-white shadow-xl relative overflow-hidden border border-sky-900">
            <div class="max-w-2xl">
                <span class="bg-sky-500 text-slate-950 font-black text-xs px-3 py-1 rounded-full uppercase mb-4 inline-block">MÜHENDİSLİK DANIŞMANLIĞI</span>
                <h3 class="text-2xl sm:text-3xl font-black mb-3">Fabrikanız veya Yeni Makinanız İçin Proje Danışın</h3>
                <p class="text-slate-300 text-sm leading-relaxed mb-6 font-medium">
                    Projenizin elektrik şemasını, pano malzeme listesini veya PCB gerber çizimini WhatsApp hattımıza gönderin; mühendislerimiz teknik incelemeyi yapıp 2 saat içinde fiyatlandırsın.
                </p>
                <div class="flex flex-wrap items-center gap-3">
                    <a href="https://wa.me/{WHATSAPP_PHONE}?text={urllib_quote('Merhaba GKM Elektrik, projemizin detaylarını paylaşmak ve teklif almak istiyoruz.')}" target="_blank" class="bg-[#25D366] hover:bg-[#20ba5c] text-white font-black text-xs sm:text-sm py-3.5 px-6 rounded-2xl transition flex items-center gap-2 shadow-lg shadow-emerald-500/20">
                        <span>💬 WhatsApp'tan Şema & Liste Gönder</span>
                    </a>
                    <a href="tel:{WHATSAPP_PHONE}" class="bg-white/10 hover:bg-white/20 text-white font-bold text-xs sm:text-sm py-3.5 px-6 rounded-2xl border border-white/20 transition">
                        📞 Doğrudan Ara: {PHONE_DISPLAY}
                    </a>
                </div>
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
        cards_html += f"""
        <article class="bg-white rounded-2xl border border-slate-200 hover:border-sky-500 transition-all duration-300 hover:shadow-xl hover:-translate-y-1 flex flex-col justify-between overflow-hidden group">
            <div class="h-44 bg-slate-900 relative overflow-hidden">
                <img src="{SITE_URL}/{cat_info['img']}" alt="{a['title']}" class="w-full h-full object-cover opacity-90 group-hover:scale-105 group-hover:opacity-100 transition duration-500">
                <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent"></div>
                <span class="absolute bottom-3 left-3 bg-white text-slate-900 font-extrabold text-[10px] px-3 py-1 rounded-full uppercase shadow">
                    {cat_info['title']}
                </span>
            </div>

            <div class="p-6 flex-1 flex flex-col justify-between">
                <div>
                    <div class="flex items-center justify-between text-xs font-bold text-slate-400 mb-2">
                        <span class="text-sky-600 font-extrabold">⏱️ {a.get('reading_time', '7 dk')}</span>
                        <span>📅 {a.get('date', 'Güncel')}</span>
                    </div>

                    <h3 class="text-base sm:text-lg font-black text-slate-900 leading-snug group-hover:text-sky-600 transition mb-3">
                        <a href="{SITE_URL}/rehber/{a['slug']}/">{a['title']}</a>
                    </h3>

                    <p class="text-slate-600 text-xs sm:text-sm line-clamp-3 leading-relaxed mb-6 font-medium">
                        {a['summary']}
                    </p>
                </div>

                <div class="pt-4 border-t border-slate-100 flex items-center justify-between">
                    <span class="text-[11px] font-semibold text-slate-500">🎯 {a.get('target_audience', 'Mühendisler')}</span>
                    <a href="{SITE_URL}/rehber/{a['slug']}/" class="text-sky-600 hover:text-sky-700 font-bold text-xs flex items-center gap-1 group-hover:translate-x-1 transition">
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
<body class="bg-slate-50 text-slate-800 font-sans antialiased selection:bg-sky-500 selection:text-white min-h-screen flex flex-col justify-between">

    {header}

    <section class="py-14 border-b border-sky-950 bg-gradient-to-br from-[#001c30] to-[#00111f] text-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6">
            <span class="text-xs font-black text-sky-400 uppercase tracking-widest block mb-2">{cat_info['icon']} UZMANLIK ALANIMIZ</span>
            <h1 class="text-3xl sm:text-4xl font-black text-white mb-4">{cat_info['title']}</h1>
            <p class="text-slate-300 text-sm sm:text-base max-w-3xl leading-relaxed font-medium">
                {cat_info['desc']}
            </p>
        </div>
    </section>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 py-12 flex-1 w-full">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
            {cards_html}
        </div>
    </main>

    {footer}

</body>
</html>
    """


def build_article_page(article, all_discussions):
    header = get_base_header(active_nav=article["category"])
    footer = get_base_footer()
    svg_diagram = generate_svg_diagram(article.get("diagram_type", "default"), article["title"])

    # WhatsApp pre-filled link
    wa_msg = f"Merhaba GKM Elektrik, '{article['title']}' konulu rehberinizi okudum. Benzer bir projemiz var, teknik detayları danışmak ve teklif almak istiyorum."
    wa_link = f"https://wa.me/{WHATSAPP_PHONE}?text={urllib_quote(wa_msg)}"

    cat_info = CATEGORIES.get(article["category"], {})
    cat_img = cat_info.get("img", "assets/gkm_0_g_kmen_elektrik__amp__otomasyo.webp")

    # Discussions for this article
    article_discussions = all_discussions.get(article["slug"], [])
    qa_cards_html = ""
    schema_faq_items = []

    for item in article_discussions:
        replies_html = ""
        for rep in item.get("replies", []):
            replies_html += f"""
            <div class="mt-3.5 p-4 rounded-2xl {'bg-sky-50/90 border border-sky-200' if rep.get('verified') else 'bg-slate-100 border border-slate-200'} text-xs leading-relaxed">
                <div class="flex items-center justify-between mb-1.5">
                    <span class="font-black text-slate-900 flex items-center gap-1.5">
                        {'<span class="bg-sky-600 text-white text-[10px] font-bold px-2 py-0.5 rounded-md">GKM Ekibi</span> ' + rep['author'] if rep.get('verified') else '👤 ' + rep['author']}
                    </span>
                    <span class="text-[10px] text-slate-400 font-semibold">{rep['date']}</span>
                </div>
                <p class="text-slate-700 font-medium">{rep['text']}</p>
            </div>
            """

            # Add to Schema FAQ
            if rep.get("verified"):
                schema_faq_items.append({
                    "@type": "Question",
                    "name": item["question"],
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": rep["text"]
                    }
                })

        qa_cards_html += f"""
        <div class="bg-slate-50 rounded-2xl border border-slate-200 p-5 sm:p-6 transition hover:border-sky-300">
            <div class="flex items-center justify-between gap-2 mb-2">
                <div class="flex items-center gap-2">
                    <span class="w-8 h-8 rounded-full bg-slate-200 text-slate-700 flex items-center justify-center font-black text-xs">
                        {item['author_name'][:1]}
                    </span>
                    <div>
                        <span class="font-black text-slate-900 text-xs sm:text-sm block">{item['author_name']}</span>
                        <span class="text-[11px] text-slate-400 font-semibold">{item.get('company', 'Mühendis')}</span>
                    </div>
                </div>
                <span class="text-[11px] font-bold text-slate-400">📅 {item.get('date', 'Güncel')}</span>
            </div>

            <p class="text-slate-800 text-xs sm:text-sm font-semibold mt-2 mb-3 bg-white p-3.5 rounded-xl border border-slate-200">
                ❓ {item['question']}
            </p>

            <div class="pl-2 sm:pl-4 border-l-2 border-sky-300 space-y-2">
                {replies_html}
            </div>
        </div>
        """

    # Schema FAQ JSON fragment
    faq_schema_str = ""
    if schema_faq_items:
        faq_schema_json = {
            "@type": "FAQPage",
            "mainEntity": schema_faq_items
        }
        faq_schema_str = ",\n" + json.dumps(faq_schema_json, ensure_ascii=False, indent=8)

    return f"""<!DOCTYPE html>
<html lang="tr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{article['title']} | GKM Elektrik & Mühendislik</title>
    <meta name="description" content="{article['summary']}">
    <link rel="canonical" href="{SITE_URL}/rehber/{article['slug']}/">

    <!-- Security Headers -->
    <meta http-equiv="X-Content-Type-Options" content="nosniff">
    <meta name="referrer" content="strict-origin-when-cross-origin">

    <!-- Open Graph -->
    <meta property="og:title" content="{article['title']}">
    <meta property="og:description" content="{article['summary']}">
    <meta property="og:url" content="{SITE_URL}/rehber/{article['slug']}/">
    <meta property="og:image" content="{SITE_URL}/{cat_img}">
    <meta property="og:type" content="article">

    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap');
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    </style>

    <!-- Schema.org Article, Breadcrumbs & Q&A FAQ -->
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
        }}{faq_schema_str}
      ]
    }}
    </script>
</head>
<body class="bg-slate-100 text-slate-800 font-sans antialiased selection:bg-sky-500 selection:text-white min-h-screen flex flex-col justify-between">

    {header}

    <!-- Article Header Banner -->
    <section class="py-12 border-b border-sky-950 bg-gradient-to-br from-[#001c30] to-[#00111f] text-white">
        <div class="max-w-4xl mx-auto px-4 sm:px-6">
            
            <nav class="flex items-center gap-2 text-xs font-semibold text-slate-400 mb-4">
                <a href="{SITE_URL}/" class="hover:text-sky-400">Ana Sayfa</a>
                <span>/</span>
                <a href="{SITE_URL}/{article['category']}/" class="text-sky-400 hover:underline">{article.get('category_title', 'Kategori')}</a>
                <span>/</span>
                <span class="text-slate-500 truncate max-w-xs">{article['slug']}</span>
            </nav>

            <div class="flex items-center gap-3 text-xs font-bold text-slate-300 mb-4">
                <span class="bg-sky-500 text-slate-950 px-3 py-1 rounded-full uppercase">{article.get('category_title', 'Mühendislik')}</span>
                <span>⏱️ {article.get('reading_time', '7 dk')}</span>
                <span>📅 {article.get('date', 'Güncel')}</span>
            </div>

            <h1 class="text-2xl sm:text-4xl font-black text-white leading-tight mb-4">
                {article['title']}
            </h1>

            <p class="text-slate-300 text-sm sm:text-base leading-relaxed font-medium">
                {article['summary']}
            </p>

            <div class="mt-6 pt-6 border-t border-slate-800 flex items-center justify-between text-xs text-slate-400">
                <span>🎯 <b>Hedef Kitle:</b> {article.get('target_audience', 'Mühendisler')}</span>
                <span class="text-sky-400 font-bold">GKM Elektrik Mühendislik Ekibi</span>
            </div>

        </div>
    </section>

    <!-- Article Content Body -->
    <main class="max-w-4xl mx-auto px-4 sm:px-6 py-12 flex-1 w-full">
        <div class="bg-white rounded-3xl p-6 sm:p-12 border border-slate-200 shadow-sm">
            
            <!-- Technical SVG Schematic -->
            <div class="mb-10 rounded-2xl overflow-hidden border border-slate-200 shadow-sm">
                {svg_diagram}
            </div>

            <!-- Body HTML -->
            <div class="prose max-w-none">
                {article['html_body']}
            </div>

            <!-- Article Call To Action Box -->
            <div class="mt-14 p-8 rounded-2xl bg-gradient-to-r from-[#001c30] to-[#00111f] text-white border border-sky-900 shadow-xl">
                <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-6">
                    <div>
                        <span class="text-[10px] font-black uppercase tracking-widest text-sky-400 block mb-1">PROJENİZ İÇİN TEKNİK DESTEK</span>
                        <h3 class="text-xl sm:text-2xl font-black mb-2">{article.get('cta_headline', 'Bu Alanda Projeniz mi Var?')}</h3>
                        <p class="text-slate-300 text-xs sm:text-sm font-medium leading-relaxed max-w-xl">
                            {article.get('cta_text', 'Mühendislerimizle görüşerek teknik detayları netleştirebilir, malzeme listesi ve anahtar teslim uygulama teklifi alabilirsiniz.')}
                        </p>
                    </div>
                    <div class="flex flex-col sm:flex-row gap-3 w-full sm:w-auto">
                        <a href="{wa_link}" target="_blank" class="bg-[#25D366] hover:bg-[#20ba5c] text-white font-black text-xs sm:text-sm py-3 px-5 rounded-xl shadow-lg transition text-center flex items-center justify-center gap-2">
                            <span>💬 WhatsApp ile Proje Danış</span>
                        </a>
                        <a href="tel:{WHATSAPP_PHONE}" class="bg-white/10 hover:bg-white/20 text-white font-bold text-xs py-3 px-5 rounded-xl border border-white/20 transition text-center">
                            📞 {PHONE_DISPLAY}
                        </a>
                    </div>
                </div>
            </div>

            <!-- Q&A and Engineering Discussions Section -->
            <section id="soru-cevap-bolumu" class="mt-16 pt-12 border-t border-slate-200">
                <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 mb-8">
                    <div>
                        <div class="flex items-center gap-2 mb-1">
                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
                            <span class="text-xs font-black text-sky-600 uppercase tracking-widest">MÜHENDİSLİK TARTIŞMALARI & SORU-CEVAP</span>
                        </div>
                        <h3 class="text-xl sm:text-2xl font-black text-slate-900">Teknik Soru-Cevap & Saha Danışmanlığı</h3>
                    </div>
                    <span class="bg-slate-100 text-slate-700 font-bold text-xs px-3.5 py-1.5 rounded-full border border-slate-200">
                        💬 {len(article_discussions)} Teknik Tartışma
                    </span>
                </div>

                <!-- Discussion Items -->
                <div id="qa-thread-list" class="space-y-6 mb-10">
                    {qa_cards_html if qa_cards_html else '<div class="text-xs text-slate-500 bg-slate-50 p-6 rounded-2xl border border-slate-200 text-center font-medium">Bu rehber için henüz soru sorulmamış. İlk teknik soruyu siz sorun!</div>'}
                </div>

                <!-- User Question Submission Form -->
                <div class="bg-gradient-to-br from-slate-50 to-sky-50/50 p-6 sm:p-8 rounded-3xl border border-sky-200 shadow-sm">
                    <div class="max-w-2xl mb-6">
                        <span class="bg-sky-600 text-white font-black text-[10px] px-2.5 py-1 rounded-full uppercase tracking-wider mb-2 inline-block">MÜHENDİSE DANIŞIN</span>
                        <h4 class="text-lg sm:text-xl font-black text-slate-900 mb-1">Bu Konuda Bir Probleminiz mi Var? Soru Sorun</h4>
                        <p class="text-xs sm:text-sm text-slate-600 font-medium leading-relaxed">
                            Sahada karşılaştığınız arıza, PLC hata kodu veya tasarım sorusunu yazın; GKM Elektrik mühendislik ekibimiz inceleyip ücretsiz yanıtlasın.
                        </p>
                    </div>

                    <form id="user-qa-form" onsubmit="handleUserSubmitQuestion(event, '{article['slug']}', '{article['title']}')" class="space-y-4">
                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                            <div>
                                <label class="block text-xs font-bold text-slate-700 mb-1">Adınız Soyadınız *</label>
                                <input type="text" id="uqa-name" placeholder="Örn: Ahmet Yılmaz" required class="w-full bg-white border border-slate-300 rounded-xl px-3.5 py-2.5 text-xs font-bold text-slate-900 focus:ring-2 focus:ring-sky-500 focus:outline-none">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-slate-700 mb-1">Şirket / Rol *</label>
                                <input type="text" id="uqa-company" placeholder="Örn: Tesis Bakım Şefi / Fabrika" required class="w-full bg-white border border-slate-300 rounded-xl px-3.5 py-2.5 text-xs font-bold text-slate-900 focus:ring-2 focus:ring-sky-500 focus:outline-none">
                            </div>
                            <div>
                                <label class="block text-xs font-bold text-slate-700 mb-1">WhatsApp / Telefon *</label>
                                <input type="text" id="uqa-phone" placeholder="05XX XXX XX XX" required class="w-full bg-white border border-slate-300 rounded-xl px-3.5 py-2.5 text-xs font-bold text-slate-900 focus:ring-2 focus:ring-sky-500 focus:outline-none">
                            </div>
                        </div>

                        <div>
                            <label class="block text-xs font-bold text-slate-700 mb-1">Sorunuz / Yaşadığınız Teknik Problem *</label>
                            <textarea id="uqa-question" rows="3" placeholder="Örn: Makinemizde servo frenleme anında aşırı gerilim (DC Bus Overvoltage) alıyoruz, parametre veya reaktör seçimi nasıl olmalı?" required class="w-full bg-white border border-slate-300 rounded-xl p-3 text-xs font-medium text-slate-900 focus:ring-2 focus:ring-sky-500 focus:outline-none"></textarea>
                        </div>

                        <div class="flex flex-col sm:flex-row items-center justify-between gap-4 pt-2">
                            <span class="text-[11px] text-slate-500 font-medium">🔒 Bilgileriniz gizli tutulur, yanıt WhatsApp veya e-posta ile iletilir.</span>
                            <button type="submit" class="w-full sm:w-auto bg-sky-600 hover:bg-sky-500 text-white font-black text-xs py-3 px-6 rounded-xl transition shadow-md shadow-sky-600/20">
                                Sorumu Mühendise İlet ➔
                            </button>
                        </div>
                    </form>

                    <div id="uqa-success-msg" class="mt-4 p-4 rounded-xl bg-emerald-50 border border-emerald-300 text-emerald-900 text-xs hidden">
                        <div class="font-black text-sm mb-1">🎉 Sorunuz Başarıyla Alındı!</div>
                        <p class="mb-3">Mühendislik ekibimiz teknik incelemeyi yapıp yanıtınızı bu sayfada ve WhatsApp numaranıza gönderecektir.</p>
                        <a id="uqa-wa-direct-link" href="#" target="_blank" class="inline-flex items-center gap-1.5 bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs px-3.5 py-2 rounded-lg transition shadow">
                            <span>💬 Bu Soruyu WhatsApp ile Doğrudan Gökmen'e İlet (Öncelikli)</span> ➔
                        </a>
                    </div>
                </div>
            </section>

        </div>
    </main>

    {footer}

    <!-- Client-Side Q&A Form Script with LocalStorage Persistence -->
    <script>
    function handleUserSubmitQuestion(e, slug, articleTitle) {{
        e.preventDefault();
        const name = document.getElementById('uqa-name').value.trim();
        const company = document.getElementById('uqa-company').value.trim();
        const phone = document.getElementById('uqa-phone').value.trim();
        const question = document.getElementById('uqa-question').value.trim();

        if (!name || !phone || !question) return;

        const newQ = {{
            id: 'user-' + Date.now(),
            slug: slug,
            author_name: name,
            company: company,
            phone: phone,
            date: new Date().toLocaleDateString('tr-TR'),
            question: question,
            is_user_submitted: true,
            replies: []
        }};

        // Store in localStorage for admin panel & persistence
        let userQuestions = [];
        try {{
            const stored = localStorage.getItem('gkm_user_questions');
            if (stored) userQuestions = JSON.parse(stored);
        }} catch(e) {{}}
        userQuestions.push(newQ);
        localStorage.setItem('gkm_user_questions', JSON.stringify(userQuestions));

        // Add live to current DOM thread
        const threadList = document.getElementById('qa-thread-list');
        const newCard = document.createElement('div');
        newCard.className = "bg-amber-50/80 rounded-2xl border border-amber-300 p-5 sm:p-6 transition";
        newCard.innerHTML = `
            <div class="flex items-center justify-between gap-2 mb-2">
                <div class="flex items-center gap-2">
                    <span class="w-8 h-8 rounded-full bg-amber-200 text-amber-800 flex items-center justify-center font-black text-xs">
                        ${{name.charAt(0)}}
                    </span>
                    <div>
                        <span class="font-black text-slate-900 text-xs sm:text-sm block">${{name}}</span>
                        <span class="text-[11px] text-amber-700 font-semibold">${{company}} (Yeni)</span>
                    </div>
                </div>
                <span class="bg-amber-200 text-amber-900 text-[10px] font-black px-2 py-0.5 rounded-full uppercase">🕒 Cevap Bekliyor</span>
            </div>
            <p class="text-slate-800 text-xs sm:text-sm font-semibold mt-2 mb-2 bg-white p-3.5 rounded-xl border border-amber-200">
                ❓ ${{question}}
            </p>
            <p class="text-[11px] text-slate-500 italic">Mühendislerimiz sorunuzu inceleyip 24 saat içinde yanıtlayacaktır.</p>
        `;
        threadList.appendChild(newCard);

        // Prepare WhatsApp link
        const waText = encodeURIComponent(`Merhaba GKM Elektrik, '${{articleTitle}}' yazınız üzerinden soru sordum:\n\nAd: ${{name}}\nFirma: ${{company}}\nSoru: ${{question}}\n\nTeknik yanıtınızı rica ederim.`);
        const waLink = `https://wa.me/{WHATSAPP_PHONE}?text=${{waText}}`;
        document.getElementById('uqa-wa-direct-link').href = waLink;

        // Reset form & show success
        document.getElementById('user-qa-form').reset();
        document.getElementById('uqa-success-msg').classList.remove('hidden');
    }}
    </script>

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
  </url>""",
        f"""  <url>
    <loc>{SITE_URL}/hesaplama/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.95</priority>
  </url>""",
        f"""  <url>
    <loc>{SITE_URL}/projeler/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>"""
    ]

    for cat_key in CATEGORIES.keys():
        urls.append(f"""  <url>
    <loc>{SITE_URL}/{cat_key}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>""")

    for a in articles:
        date_val = a.get("date", today)
        urls.append(f"""  <url>
    <loc>{SITE_URL}/rehber/{a['slug']}/</loc>
    <lastmod>{date_val}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""")

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>
"""


def build_robots_txt():
    return f"""# GKM Elektrik & Mühendislik Robots Policy
User-agent: Googlebot
Allow: /

User-agent: Googlebot-Image
Allow: /

User-agent: Bingbot
Allow: /

User-agent: Yandex
Allow: /

# Block admin panel from crawling
User-agent: *
Disallow: /admin/
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""


def compile_site():
    print("[SSG] Derleme baslatildi...")
    articles = load_all_articles()
    discussions = load_discussions()
    projects = load_projects()
    print(f"[SSG] Yuklenen makale: {len(articles)}, Tartisma: {len(discussions)}, Vaka Projesi: {len(projects)}")

    # Clean and prepare dist directory
    if os.path.exists(DIST_DIR):
        shutil.rmtree(DIST_DIR)
    os.makedirs(DIST_DIR, exist_ok=True)

    header = get_base_header(active_nav="")
    footer = get_base_footer()

    # 1. Homepage
    home_html = build_homepage(articles)
    with open(os.path.join(DIST_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(home_html)
    print(" -> index.html olusturuldu.")

    # 2. Categories
    for cat_key in CATEGORIES.keys():
        cat_dir = os.path.join(DIST_DIR, cat_key)
        os.makedirs(cat_dir, exist_ok=True)
        cat_html = build_category_page(cat_key, articles)
        with open(os.path.join(cat_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(cat_html)
        print(f" -> /{cat_key}/index.html olusturuldu.")

    # 3. Individual Guide / Article pages with Q&A
    for a in articles:
        art_dir = os.path.join(DIST_DIR, "rehber", a["slug"])
        os.makedirs(art_dir, exist_ok=True)
        art_html = build_article_page(a, discussions)
        with open(os.path.join(art_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(art_html)
    print(f" -> {len(articles)} adet /rehber/[slug]/ sayfasi (Soru-Cevap dahil) olusturuldu.")

    # 4. Interactive Engineering Calculators (/hesaplama/)
    calc_dir = os.path.join(DIST_DIR, "hesaplama")
    os.makedirs(calc_dir, exist_ok=True)
    calc_header = get_base_header(active_nav="hesaplama")
    calc_html = generate_calculators_page(SITE_URL, MAIN_WEBSITE, WHATSAPP_PHONE, PHONE_DISPLAY, calc_header, footer)
    with open(os.path.join(calc_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(calc_html)
    print(" -> /hesaplama/index.html (3 Mühendislik Hesaplayıcı) olusturuldu.")

    # 5. Real-World Projects & Case Studies (/projeler/)
    proj_dir = os.path.join(DIST_DIR, "projeler")
    os.makedirs(proj_dir, exist_ok=True)
    proj_header = get_base_header(active_nav="projeler")
    proj_html = generate_projects_page(SITE_URL, MAIN_WEBSITE, WHATSAPP_PHONE, PHONE_DISPLAY, proj_header, footer, projects)
    with open(os.path.join(proj_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(proj_html)
    print(" -> /projeler/index.html (Vaka Analizleri & Proje Galerisi) olusturuldu.")

    # 6. Admin Panel (/admin/)
    admin_dir = os.path.join(DIST_DIR, "admin")
    os.makedirs(admin_dir, exist_ok=True)
    admin_header = get_base_header(active_nav="")
    discussions_json_str = json.dumps(discussions, ensure_ascii=False)
    admin_html = generate_admin_page(SITE_URL, MAIN_WEBSITE, WHATSAPP_PHONE, PHONE_DISPLAY, admin_header, footer, discussions_json_str)
    with open(os.path.join(admin_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(admin_html)
    print(" -> /admin/index.html (Yönetici & Soru Paneli) olusturuldu.")

    # 7. Sitemap & Robots
    with open(os.path.join(DIST_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(build_sitemap(articles))
    print(" -> sitemap.xml olusturuldu.")

    with open(os.path.join(DIST_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(build_robots_txt())
    print(" -> robots.txt olusturuldu.")

    # 8. Copy Assets into dist/assets
    dist_assets = os.path.join(DIST_DIR, "assets")
    os.makedirs(dist_assets, exist_ok=True)
    if os.path.exists(ASSETS_DIR):
        for f in os.listdir(ASSETS_DIR):
            shutil.copy2(os.path.join(ASSETS_DIR, f), os.path.join(dist_assets, f))
    print(" -> assets kopyalandi.")

    # 9. Mirror to /docs for GitHub Pages
    if os.path.exists(DOCS_DIR):
        shutil.rmtree(DOCS_DIR)
    shutil.copytree(DIST_DIR, DOCS_DIR)
    print(f" -> docs/ klasorune tam ayna senkronizasyonu tamamlandi.")
    print("[SSG] Site derlemesi basariyla tamamlandi!")


if __name__ == "__main__":
    compile_site()
