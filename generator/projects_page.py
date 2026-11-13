"""
Projects & Case Studies Page Generator for GKM Elektrik
Presents real-world industrial automation, panel manufacturing, PCB design and SCADA case studies.
Includes interactive "Panonun İçine & Proje Detayına Bak" modal and full-screen image inspection lightbox.
"""

import json
import os

def generate_projects_page(site_url, main_website, whatsapp_phone, phone_display, header, footer, projects):
    cards_html = ""
    for p in projects:
        wa_text = f"Merhaba GKM Elektrik, '{p['title']}' projenizin pano şeması ve malzeme listesi hakkında detaylı bilgi ve teklif almak istiyorum."
        wa_link = f"https://wa.me/{whatsapp_phone}?text=" + wa_text.replace(" ", "%20").replace("'", "")

        metrics_html = "".join([
            f'<div class="bg-slate-50 border border-slate-200 rounded-xl p-3 text-center">'
            f'<span class="text-[10px] text-slate-500 font-bold uppercase block">{m["label"]}</span>'
            f'<span class="text-xs sm:text-sm font-black text-sky-700">{m["val"]}</span>'
            f'</div>'
            for m in p.get("metrics", [])
        ])

        hw_tags = "".join([
            f'<span class="bg-slate-100 text-slate-700 text-[11px] font-bold px-2.5 py-1 rounded-lg border border-slate-200">{hw}</span>'
            for hw in p.get("hardware_used", [])
        ])

        interior = p.get("interior_details", {})

        cards_html += f"""
        <article class="bg-white rounded-3xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between">
            <div>
                <!-- Top Image with Zoom Button -->
                <div class="h-64 bg-slate-900 relative overflow-hidden group cursor-pointer" onclick="openLightbox('{site_url}/{p['image']}', '{p['title']}')">
                    <img src="{site_url}/{p['image']}" alt="{p['title']}" class="w-full h-full object-cover opacity-90 group-hover:scale-105 transition duration-700">
                    <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent"></div>
                    <span class="absolute top-4 left-4 bg-sky-600 text-white font-black text-xs px-3.5 py-1.5 rounded-full uppercase shadow">
                        {p['category_title']}
                    </span>
                    <span class="absolute top-4 right-4 bg-slate-950/80 text-white text-xs font-bold px-3 py-1.5 rounded-xl border border-white/20 backdrop-blur-sm flex items-center gap-1.5 opacity-0 group-hover:opacity-100 transition">
                        🔍 Fotoğrafı Büyüt
                    </span>
                    <span class="absolute bottom-4 left-4 text-white text-xs font-bold flex items-center gap-1.5">
                        📍 <span>{p['location']}</span> • <span class="text-sky-300">{p['client_industry']}</span>
                    </span>
                </div>

                <div class="p-6 sm:p-8">
                    <!-- Title -->
                    <h2 class="text-xl sm:text-2xl font-black text-slate-900 leading-snug mb-4">
                        {p['title']}
                    </h2>

                    <!-- Key Impact Metrics Grid -->
                    <div class="grid grid-cols-3 gap-2.5 mb-6">
                        {metrics_html}
                    </div>

                    <!-- Problem & Solution Narrative -->
                    <div class="space-y-4 text-xs sm:text-sm text-slate-700 leading-relaxed font-medium mb-6">
                        <div class="p-4 bg-red-50/70 border-l-4 border-red-500 rounded-r-xl">
                            <span class="font-black text-red-900 block mb-1">❌ Karşılaşılan Sanayi Problemi:</span>
                            <p>{p['problem']}</p>
                        </div>
                        <div class="p-4 bg-emerald-50/70 border-l-4 border-emerald-500 rounded-r-xl">
                            <span class="font-black text-emerald-900 block mb-1">✅ GKM Elektrik Mühendislik Çözümü:</span>
                            <p>{p['solution']}</p>
                        </div>
                    </div>

                    <!-- Hardware Used -->
                    <div class="mb-6">
                        <span class="text-[11px] font-black uppercase text-slate-400 tracking-wider block mb-2">Kullanılan Donanım & Standartlar:</span>
                        <div class="flex flex-wrap gap-2">
                            {hw_tags}
                        </div>
                    </div>

                    <!-- Internal Panel Engineering Drawer (Expandable) -->
                    <div class="mt-4 pt-4 border-t border-slate-100">
                        <button type="button" onclick="openProjectModal('{p['id']}')" class="w-full bg-slate-900 hover:bg-slate-800 text-sky-400 font-extrabold text-xs py-3 px-4 rounded-xl transition flex items-center justify-center gap-2 shadow-sm">
                            <span>🔍 Panonun İç Yapısını & Teknik Şemayı İncele</span> ➔
                        </button>
                    </div>
                </div>
            </div>

            <!-- Bottom CTA Button -->
            <div class="p-6 sm:p-8 pt-0 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4 mt-auto">
                <span class="text-xs font-bold text-slate-500 hidden sm:inline">Teslim Tarihi: {p.get('date', '2026')}</span>
                <a href="{wa_link}" target="_blank" rel="noopener" class="w-full sm:w-auto bg-[#25D366] hover:bg-[#20ba5c] text-white font-black text-xs sm:text-sm py-3 px-6 rounded-xl shadow-lg transition flex items-center justify-center gap-2">
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
                    <span>{p.get('cta_text', 'Benzer Proje İçin Teklif Alın')}</span>
                </a>
            </div>
        </article>
        """

    projects_json_str = json.dumps(projects, ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="tr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerçek Sanayi Projeleri & Vaka Analizleri | GKM Elektrik</title>
    <meta name="description" content="Gökmen Elektrik saha referansları: 12 istasyonlu döner tabla servo otomasyonu, 1250 kVA tristörlü harmonik kompanzasyon, soğuk hava SCADA, STM32 CAN-bus kartları ve ISO 13849 emniyet revizyonları.">
    <link rel="canonical" href="{site_url}/projeler/">

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap');
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    </style>
</head>
<body class="bg-slate-100 text-slate-800 font-sans antialiased selection:bg-sky-500 selection:text-white min-h-screen flex flex-col justify-between">

    {header}

    <!-- Hero Header -->
    <section class="py-14 border-b border-sky-950 bg-gradient-to-br from-[#001c30] to-[#00111f] text-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6">
            <span class="text-xs font-black text-sky-400 uppercase tracking-widest block mb-2">SAHA ÇÖZÜMLERİMİZ & REFERANSLAR</span>
            <h1 class="text-3xl sm:text-5xl font-black text-white tracking-tight leading-tight mb-4">
                Gerçek Sanayi Projeleri ve <span class="text-sky-400">Vaka Analizleri</span>
            </h1>
            <p class="text-slate-300 text-sm sm:text-base max-w-3xl leading-relaxed font-medium">
                Fabrikalarda ve makine imalatlarında karşılaşılan gerçek teknik tıkanıklıklar, GKM Elektrik mühendislik ekibinin uyguladığı donanım/yazılım çözümleri, pano içi kablaj standartları ve ölçülebilir performans kazanımları.
            </p>
        </div>
    </section>

    <!-- Projects Grid -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 py-14 flex-1 w-full">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-10">
            {cards_html}
        </div>
    </main>

    <!-- Bottom Conversion Banner -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 pb-16">
        <div class="bg-gradient-to-r from-[#001c30] to-[#00111f] rounded-3xl p-8 sm:p-12 text-white shadow-xl relative overflow-hidden border border-sky-900">
            <div class="max-w-2xl">
                <span class="bg-sky-500 text-slate-950 font-black text-xs px-3 py-1 rounded-full uppercase mb-4 inline-block">ÖZEL PROJE VE FİZİBİLİTE</span>
                <h3 class="text-2xl sm:text-3xl font-black mb-3">Makinanız veya Tesisiniz İçin Benzer Bir Çözüm mü Arıyorsunuz?</h3>
                <p class="text-slate-300 text-sm leading-relaxed mb-6 font-medium">
                    Mevcut hattınızın videosunu veya teknik şartnamenizi bize iletin. Sahada inceleme yaparak en yüksek verimlilik ve en düşük yatırım maliyetiyle projenizi hayata geçirelim.
                </p>
                <div class="flex flex-wrap items-center gap-3">
                    <a href="https://wa.me/{whatsapp_phone}?text=Merhaba%20GKM%20Elektrik,%20tesisimizdeki%20makine%20otomasyonu%20veya%20pano%20projemiz%20için%20teknik%20keşif%20ve%20teklif%20almak%20istiyoruz." target="_blank" class="bg-[#25D366] hover:bg-[#20ba5c] text-white font-black text-xs sm:text-sm py-3.5 px-6 rounded-2xl transition flex items-center gap-2 shadow-lg shadow-emerald-500/20">
                        <span>💬 WhatsApp ile Proje Danış</span>
                    </a>
                    <a href="tel:{whatsapp_phone}" class="bg-white/10 hover:bg-white/20 text-white font-bold text-xs sm:text-sm py-3.5 px-6 rounded-2xl border border-white/20 transition">
                        📞 Doğrudan Ara: {phone_display}
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Fullscreen Image Lightbox Modal -->
    <div id="lightbox-modal" class="fixed inset-0 bg-slate-950/95 backdrop-blur-md z-50 flex items-center justify-center p-4 hidden" onclick="closeLightbox()">
        <div class="max-w-5xl w-full max-h-[90vh] flex flex-col items-center justify-center relative" onclick="event.stopPropagation()">
            <button onclick="closeLightbox()" class="absolute -top-12 right-0 text-white hover:text-sky-400 text-2xl font-black">✕ Kapat</button>
            <img id="lightbox-img" src="" alt="Pano İçi Büyütülmüş Görünüm" class="max-w-full max-h-[80vh] rounded-2xl object-contain shadow-2xl border border-white/20">
            <p id="lightbox-caption" class="text-white text-xs sm:text-sm font-bold mt-4 text-center"></p>
        </div>
    </div>

    <!-- Project Interior Deep Dive Modal -->
    <div id="project-modal" class="fixed inset-0 bg-slate-950/80 backdrop-blur-md z-50 flex items-center justify-center p-4 hidden" onclick="closeProjectModal()">
        <div class="bg-white rounded-3xl p-6 sm:p-10 max-w-3xl w-full max-h-[90vh] overflow-y-auto border border-slate-200 shadow-2xl relative" onclick="event.stopPropagation()">
            <button onclick="closeProjectModal()" class="absolute top-6 right-6 text-slate-400 hover:text-slate-800 text-2xl font-black">✕</button>
            
            <div id="project-modal-content">
                <!-- Dynamically filled -->
            </div>
        </div>
    </div>

    {footer}

    <!-- Lightbox & Project Modal Logic -->
    <script>
    const ALL_PROJECTS = {projects_json_str};

    function openLightbox(imgSrc, caption) {{
        document.getElementById('lightbox-img').src = imgSrc;
        document.getElementById('lightbox-caption').innerText = caption;
        document.getElementById('lightbox-modal').classList.remove('hidden');
    }}

    function closeLightbox() {{
        document.getElementById('lightbox-modal').classList.add('hidden');
    }}

    function openProjectModal(projectId) {{
        const p = ALL_PROJECTS.find(x => x.id === projectId);
        if (!p) return;

        const interior = p.interior_details || {{}};
        const hwTags = (p.hardware_used || []).map(h => `<span class="bg-slate-100 text-slate-800 text-xs font-bold px-3 py-1.5 rounded-xl border border-slate-200">${{h}}</span>`).join(' ');

        const waText = encodeURIComponent(`Merhaba GKM Elektrik, '${{p.title}}' projenizin pano içi teknik şeması ve malzeme listesini incelemek istiyorum.`);
        const waLink = `https://wa.me/{whatsapp_phone}?text=${{waText}}`;

        document.getElementById('project-modal-content').innerHTML = `
            <div class="flex items-center gap-2 mb-2">
                <span class="bg-sky-600 text-white text-[10px] font-black px-3 py-1 rounded-full uppercase">${{p.category_title}}</span>
                <span class="text-xs font-bold text-slate-400">📍 ${{p.location}}</span>
            </div>
            <h2 class="text-xl sm:text-2xl font-black text-slate-950 mb-4">${{p.title}}</h2>

            <div class="h-60 rounded-2xl overflow-hidden mb-6 bg-slate-900 cursor-pointer relative group" onclick="openLightbox('${{p.image.startsWith('http') ? p.image : site_url + '/' + p.image}}', '${{p.title}}')">
                <img src="${{p.image.startsWith('http') ? p.image : site_url + '/' + p.image}}" alt="${{p.title}}" class="w-full h-full object-cover">
                <span class="absolute bottom-3 right-3 bg-slate-950/80 text-white text-xs font-bold px-3 py-1.5 rounded-xl border border-white/20 backdrop-blur-sm">🔍 Fotoğrafı Tam Ekran Büyüt</span>
            </div>

            <div class="space-y-4 mb-6 text-xs sm:text-sm text-slate-700 leading-relaxed font-medium">
                <div class="p-4 bg-sky-50 rounded-2xl border border-sky-200">
                    <h4 class="font-black text-sky-950 text-sm mb-1">🏗️ Pano Karkası & Mekanik Yerleşim</h4>
                    <p>${{interior.panel_structure || 'IEC 61439 standartlarında modüler tip testli hücre yapısı ve iklimlendirme.'}}</p>
                </div>

                <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200">
                    <h4 class="font-black text-slate-900 text-sm mb-1">🔌 Kablaj & Klemens Standartları</h4>
                    <p>${{interior.wiring_system || 'Titreşime dayanıklı yay baskılı Phoenix/Weidmüller klemensler ve IEC 60204-1 renk kodlaması.'}}</p>
                </div>

                <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200">
                    <h4 class="font-black text-slate-900 text-sm mb-1">⚙️ Otomasyon & Kontrol Mimarisi</h4>
                    <p>${{interior.control_architecture || 'Endüstriyel Ethernet / Profinet haberleşme mimarisi ve çift kanal emniyet devresi.'}}</p>
                </div>

                <div class="p-4 bg-emerald-50 rounded-2xl border border-emerald-200">
                    <h4 class="font-black text-emerald-950 text-sm mb-1">✅ Test & Saha Doğrulama (FAT / SAT)</h4>
                    <p>${{interior.testing_verification || 'Saha devreye alma öncesi atölyede tüm fonksiyonel testler ve yalıtım dayanım testleri tamamlanmıştır.'}}</p>
                </div>
            </div>

            <div class="mb-6">
                <h4 class="text-xs font-black uppercase text-slate-400 tracking-wider mb-2">Kullanılan Ana Donanım Parçaları:</h4>
                <div class="flex flex-wrap gap-2">
                    ${{hwTags}}
                </div>
            </div>

            <div class="pt-4 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4">
                <span class="text-xs font-bold text-slate-500">GKM Mühendislik Referans Projesi</span>
                <a href="${{waLink}}" target="_blank" class="w-full sm:w-auto bg-[#25D366] hover:bg-[#20ba5c] text-white font-black text-xs sm:text-sm py-3 px-6 rounded-xl shadow-lg transition flex items-center justify-center gap-2">
                    <span>💬 Bu Sistemin EPLAN Şemasını & Malzeme Listesini İste</span>
                </a>
            </div>
        `;

        document.getElementById('project-modal').classList.remove('hidden');
    }}

    function closeProjectModal() {{
        document.getElementById('project-modal').classList.add('hidden');
    }}
    </script>

</body>
</html>
"""
