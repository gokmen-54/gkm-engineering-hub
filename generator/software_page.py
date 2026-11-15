# -*- coding: utf-8 -*-
"""
Software & Web Solutions Page Generator for GKM Engineering Hub
Focuses on Sakarya & Marmara industrial businesses, factories, and SMEs.
Includes 3 interactive real-time live demos (Mini CRM, Live SCADA Dashboard, Web Template Switcher).
"""

import urllib.parse

def generate_software_page(SITE_URL, MAIN_WEBSITE, WHATSAPP_PHONE, PHONE_DISPLAY, header, footer):
    wa_msg = urllib.parse.quote("Merhaba GKM Elektrik & Mühendislik, Sakarya'daki işletmemiz için web sitesi / özel yazılım projesi hakkında görüşmek ve teklif almak istiyoruz.")
    
    html = f"""<!DOCTYPE html>
<html lang="tr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sakarya İşletme Yazılımları & Web Tasarım | Fabrika Otomasyon & ERP Çözümleri - GKM Mühendislik</title>
    <meta name="description" content="Sakarya 1. OSB, Hendek OSB ve Marmara sanayisi için özel işletme yazılımları, üretim takip, barkodlu depo, web tabanlı SCADA ve anahtar teslim kurumsal fabrika web siteleri.">
    <meta name="keywords" content="Sakarya web tasarım, Sakarya işletme yazılımı, Sakarya ERP, fabrika üretim takip programı, Sakarya web yazılım, Sakarya otomasyon yazılımı, Hendek OSB web tasarım">
    
    <link rel="canonical" href="{SITE_URL}/isletme-yazilimlari-web/">
    <meta property="og:title" content="Sakarya İşletme Yazılımları & Web Tasarım | GKM Mühendislik">
    <meta property="og:description" content="Fabrikanız ve atölyeniz için 3 günde anahtar teslim web sitesi, mini CRM ve canlı üretim takip yazılımları.">
    <meta property="og:url" content="{SITE_URL}/isletme-yazilimlari-web/">
    <meta property="og:type" content="website">

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        brand: {{
                            navy: '#001c30',
                            blue: '#003366',
                            sky: '#0284c7',
                            gold: '#f59e0b',
                            emerald: '#10b981'
                        }}
                    }}
                }}
            }}
        }}
    </script>

    <!-- Schema.org LocalBusiness with Sakarya Geotargeting -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "GKM Elektrik & Mühendislik - Sakarya İşletme Yazılımları",
      "image": "{SITE_URL}/assets/logo.webp",
      "telephone": "{PHONE_DISPLAY}",
      "url": "{SITE_URL}/isletme-yazilimlari-web/",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "Adapazarı",
        "addressRegion": "Sakarya",
        "addressCountry": "TR"
      }},
      "geo": {{
        "@type": "GeoCoordinates",
        "latitude": 40.7731,
        "longitude": 30.4043
      }},
      "areaServed": ["Sakarya", "Adapazarı", "Serdivan", "Erenler", "Hendek", "Akyazı", "Kocaeli", "Bursa"],
      "priceRange": "$$"
    }}
    </script>
</head>
<body class="bg-slate-50 text-slate-900 font-sans antialiased selection:bg-indigo-500 selection:text-white">

    {header}

    <!-- Hero Section -->
    <section class="relative bg-gradient-to-br from-slate-950 via-[#001c30] to-indigo-950 text-white py-16 sm:py-24 overflow-hidden border-b border-slate-800">
        <div class="absolute inset-0 bg-[radial-gradient(circle_at_30%_20%,rgba(99,102,241,0.15),transparent_40%)]"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
            <div class="max-w-3xl">
                <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-indigo-500/20 border border-indigo-400/30 text-indigo-300 text-xs font-bold uppercase tracking-wider mb-6">
                    <span class="w-2 h-2 rounded-full bg-indigo-400 animate-pulse"></span>
                    Sakarya & Marmara Sanayi Yazılım Evi
                </div>
                <h1 class="text-3xl sm:text-5xl font-black tracking-tight leading-tight mb-6">
                    Makinelerinizin ve Fabrikanızın Dilinden Anlayan <span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-sky-300">Özel İşletme Yazılımları</span>
                </h1>
                <p class="text-slate-300 text-base sm:text-lg leading-relaxed mb-8">
                    Klasik reklam ajanslarını unutun. Sakarya 1. OSB, Hendek OSB ve atölyeler için hem fabrikanın elektrik/otomasyon altyapısına bağlanan üretim takip panelleri, hem de <b>3 günde anahtar teslim modern kurumsal web siteleri</b> üretiyoruz.
                </p>
                <div class="flex flex-wrap items-center gap-4">
                    <a href="#demolar" class="bg-indigo-600 hover:bg-indigo-500 text-white font-extrabold px-6 py-3.5 rounded-xl shadow-lg shadow-indigo-500/25 transition flex items-center gap-2">
                        <span>🚀 Canlı Demoları İncele</span>
                    </a>
                    <a href="https://wa.me/{WHATSAPP_PHONE}?text={wa_msg}" target="_blank" class="bg-[#25D366] hover:bg-[#20ba5c] text-white font-black px-6 py-3.5 rounded-xl shadow-lg shadow-emerald-500/20 transition flex items-center gap-2">
                        <span>💬 WhatsApp Proje Teklifi Al</span>
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- LIVE INTERACTIVE DEMOS SECTION -->
    <section id="demolar" class="py-16 sm:py-24 bg-slate-100">
        <div class="max-w-7xl mx-auto px-4 sm:px-6">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <span class="text-indigo-600 font-extrabold text-xs uppercase tracking-wider">İnteraktif Laboratuvar</span>
                <h2 class="text-2xl sm:text-4xl font-black text-slate-900 mt-2 mb-4">Gerçekten Çalışan Canlı Demolar</h2>
                <p class="text-slate-600 text-sm sm:text-base">Aşağıdaki panellerde butonlara basıp değerleri değiştirebilir, işletmeniz için nasıl çalışacağını canlı olarak test edebilirsiniz.</p>
            </div>

            <!-- 3 Demos Grid -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12">
                
                <!-- DEMO 1: Mini CRM & Anlık Teklif Motoru -->
                <div class="bg-white rounded-2xl border border-slate-200 shadow-xl overflow-hidden p-6 sm:p-8 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <span class="bg-indigo-100 text-indigo-800 font-extrabold text-xs px-3 py-1 rounded-full uppercase">Demo #1: CRM & Teklif Motoru</span>
                            <span class="text-xs font-bold text-slate-400">Canlı Hesaplayıcı</span>
                        </div>
                        <h3 class="text-xl font-black text-slate-900 mb-2">İşletmeniz İçin Hızlı Teklif & Müşteri Formu</h3>
                        <p class="text-slate-600 text-xs sm:text-sm mb-6">Müşterilerinize 3 gün bekletmeden, 30 saniyede WhatsApp üzerinden antetli resmi teklif gönderme sistemi.</p>

                        <!-- Interactive Form -->
                        <div class="space-y-4 bg-slate-50 p-4 rounded-xl border border-slate-200 text-xs sm:text-sm">
                            <div>
                                <label class="font-bold text-slate-700 block mb-1">Müşteri / Firma Adı:</label>
                                <input type="text" id="demo_client" value="Sakarya Makine San. Tic." class="w-full bg-white border border-slate-300 rounded-lg px-3 py-2 font-medium focus:ring-2 focus:ring-indigo-500 outline-none">
                            </div>
                            <div>
                                <label class="font-bold text-slate-700 block mb-1">İhtiyaç Duyulan Yazılım Modülü:</label>
                                <select id="demo_module" onchange="updateCrmTotal()" class="w-full bg-white border border-slate-300 rounded-lg px-3 py-2 font-medium focus:ring-2 focus:ring-indigo-500 outline-none">
                                    <option value="28000">Kurumsal Fabrika Web Sitesi (Mobil Uyumlu & Çok Dilli) - 28.000 TL</option>
                                    <option value="42000">Barkodlu Stok & Depo Yönetim Sistemi - 42.000 TL</option>
                                    <option value="65000">Web Tabanlı Canlı SCADA & Üretim Takip Paneli - 65.000 TL</option>
                                    <option value="85000">Özel B2B Bayi Sipariş & Teklif Portalı - 85.000 TL</option>
                                </select>
                            </div>
                            <div class="flex items-center justify-between pt-2 border-t border-slate-200">
                                <span class="font-bold text-slate-600">Tahmini Proje Bedeli:</span>
                                <span id="demo_total" class="text-lg font-black text-indigo-600">28.000 TL</span>
                            </div>
                        </div>
                    </div>

                    <button onclick="sendCrmWhatsApp()" class="mt-6 w-full bg-indigo-600 hover:bg-indigo-700 text-white font-extrabold py-3 px-4 rounded-xl transition flex items-center justify-center gap-2 shadow">
                        <span>📱 Bu Teklifi WhatsApp'tan Bize İlet</span>
                    </button>
                </div>

                <!-- DEMO 2: Canlı Fabrika SCADA & Üretim Takip Ekranı -->
                <div class="bg-slate-900 rounded-2xl border border-slate-800 shadow-xl overflow-hidden p-6 sm:p-8 text-white flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-4">
                            <span class="bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 font-extrabold text-xs px-3 py-1 rounded-full uppercase">Demo #2: Web SCADA & IoT</span>
                            <span class="flex items-center gap-1.5 text-xs font-bold text-emerald-400">
                                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span> Canlı Veri Akışı
                            </span>
                        </div>
                        <h3 class="text-xl font-black mb-2">Fabrika Üretim & Makine Metraj Takibi</h3>
                        <p class="text-slate-400 text-xs sm:text-sm mb-6">Makinelerinizden PLC verisini alıp fabrika patronunun cebine canlı aktaran web mimarimiz.</p>

                        <!-- Simulated SCADA Dials -->
                        <div class="grid grid-cols-2 gap-3 mb-4">
                            <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-center">
                                <span class="text-slate-400 text-xs block">Hat Hızı (m/dk)</span>
                                <span id="scada_speed" class="text-2xl sm:text-3xl font-black text-sky-400">42.5</span>
                            </div>
                            <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-center">
                                <span class="text-slate-400 text-xs block">Vardiya Metrajı (m)</span>
                                <span id="scada_metraj" class="text-2xl sm:text-3xl font-black text-emerald-400">1,842</span>
                            </div>
                            <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-center">
                                <span class="text-slate-400 text-xs block">Motor Sıcaklığı (°C)</span>
                                <span id="scada_temp" class="text-2xl sm:text-3xl font-black text-amber-400">54°C</span>
                            </div>
                            <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-center">
                                <span class="text-slate-400 text-xs block">Hat Durumu</span>
                                <span id="scada_status" class="text-base sm:text-lg font-black text-emerald-400">ÇALIŞIYOR</span>
                            </div>
                        </div>
                    </div>

                    <!-- Interactive Motor Toggle -->
                    <div class="flex items-center gap-3">
                        <button id="btn_motor" onclick="toggleScadaMotor()" class="flex-1 bg-red-600 hover:bg-red-700 text-white font-extrabold py-3 px-4 rounded-xl transition">
                            Hattı Durdur (Simülasyon)
                        </button>
                    </div>
                </div>

            </div>

            <!-- DEMO 3: Sektörel Sanayi Web Şablonları -->
            <div class="bg-white rounded-2xl border border-slate-200 shadow-xl p-6 sm:p-8">
                <div class="flex flex-wrap items-center justify-between gap-4 mb-6 pb-6 border-b border-slate-100">
                    <div>
                        <span class="bg-sky-100 text-sky-800 font-extrabold text-xs px-3 py-1 rounded-full uppercase">Demo #3: 3 Günde Teslim Web Siteleri</span>
                        <h3 class="text-xl font-black text-slate-900 mt-2">Sektörünüze Özel Kurumsal Sanayi Şablonları</h3>
                    </div>
                    <div class="flex flex-wrap gap-2 text-xs font-bold" id="sector_tabs">
                        <button onclick="switchSector('makine')" class="sector-tab bg-indigo-600 text-white px-3 py-1.5 rounded-lg">Makine İmalatçıları</button>
                        <button onclick="switchSector('tekstil')" class="sector-tab bg-slate-100 text-slate-700 hover:bg-slate-200 px-3 py-1.5 rounded-lg">Tekstil & Sarım</button>
                        <button onclick="switchSector('torna')" class="sector-tab bg-slate-100 text-slate-700 hover:bg-slate-200 px-3 py-1.5 rounded-lg">Talaşlı İmalat / Torna</button>
                        <button onclick="switchSector('gida')" class="sector-tab bg-slate-100 text-slate-700 hover:bg-slate-200 px-3 py-1.5 rounded-lg">Soğuk Depo & Gıda</button>
                    </div>
                </div>

                <div id="sector_preview" class="bg-slate-900 text-white p-6 rounded-xl border border-slate-800">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-4">
                        <span id="sector_title" class="font-extrabold text-indigo-400">Makine İmalat Sanayisi Web Sitesi</span>
                        <span class="text-xs text-slate-400">İngilizce / Türkçe • Mobil & Tablet %100 Uyumlu</span>
                    </div>
                    <p id="sector_desc" class="text-slate-300 text-sm mb-4">
                        Ürettiğiniz makinelerin teknik çizimlerini, katalog PDF'lerini ve çalışma videolarını profesyonelce sergileyen, yurtdışı ihracat müşterilerine hitap eden hızlı ve SEO uyumlu web sitesi.
                    </p>
                    <div class="flex items-center gap-4 text-xs text-slate-400">
                        <span>✓ Kurumsal E-Posta Dahil</span>
                        <span>✓ SSL Güvenlik Kilidi Dahil</span>
                        <span>✓ 3 Günde Teslim</span>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- Sakarya Local Districts Grid -->
    <section class="py-16 bg-white border-t border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6">
            <div class="text-center max-w-2xl mx-auto mb-12">
                <h2 class="text-xl sm:text-3xl font-black text-slate-900">Sakarya ve Bölge Sanayisine Birebir Hizmet</h2>
                <p class="text-slate-600 text-xs sm:text-sm mt-2">Uzakta değiliz; Sakarya'daki tesisinize gelip ihtiyacınızı yerinde dinliyor, mühendislik ekibimizle yazılımınızı kuruyoruz.</p>
            </div>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 text-center font-bold text-xs sm:text-sm text-slate-700">
                <div class="bg-slate-50 border border-slate-200 p-4 rounded-xl">📍 Sakarya 1. OSB</div>
                <div class="bg-slate-50 border border-slate-200 p-4 rounded-xl">📍 Hendek 2. OSB</div>
                <div class="bg-slate-50 border border-slate-200 p-4 rounded-xl">📍 Söğütlü 3. OSB</div>
                <div class="bg-slate-50 border border-slate-200 p-4 rounded-xl">📍 Adapazarı Sanayi</div>
                <div class="bg-slate-50 border border-slate-200 p-4 rounded-xl">📍 Serdivan & Erenler</div>
                <div class="bg-slate-50 border border-slate-200 p-4 rounded-xl">📍 Akyazı Sanayi</div>
                <div class="bg-slate-50 border border-slate-200 p-4 rounded-xl">📍 Karasu Liman Bölgesi</div>
                <div class="bg-slate-50 border border-slate-200 p-4 rounded-xl">📍 Kocaeli & Dilovası</div>
            </div>
        </div>
    </section>

    {footer}

    <!-- Live Demo Scripts -->
    <script>
        function updateCrmTotal() {{
            const val = document.getElementById('demo_module').value;
            document.getElementById('demo_total').innerText = parseInt(val).toLocaleString('tr-TR') + ' TL';
        }}

        function sendCrmWhatsApp() {{
            const client = document.getElementById('demo_client').value;
            const sel = document.getElementById('demo_module');
            const modName = sel.options[sel.selectedIndex].text;
            const msg = `Merhaba GKM Mühendislik, firmamız (${{client}}) için "${{modName}}" projesi hakkında teklif almak ve görüşmek istiyoruz.`;
            window.open(`https://wa.me/{WHATSAPP_PHONE}?text=${{encodeURIComponent(msg)}}`, '_blank');
        }}

        let isRunning = true;
        let metraj = 1842;
        setInterval(() => {{
            if (isRunning) {{
                metraj += Math.floor(Math.random() * 3) + 1;
                document.getElementById('scada_metraj').innerText = metraj.toLocaleString('tr-TR');
                const speed = (42.0 + (Math.random() * 2 - 1)).toFixed(1);
                document.getElementById('scada_speed').innerText = speed;
            }}
        }}, 1000);

        function toggleScadaMotor() {{
            isRunning = !isRunning;
            const btn = document.getElementById('btn_motor');
            const status = document.getElementById('scada_status');
            const speed = document.getElementById('scada_speed');
            if (isRunning) {{
                btn.innerText = 'Hattı Durdur (Simülasyon)';
                btn.className = 'flex-1 bg-red-600 hover:bg-red-700 text-white font-extrabold py-3 px-4 rounded-xl transition';
                status.innerText = 'ÇALIŞIYOR';
                status.className = 'text-base sm:text-lg font-black text-emerald-400';
            }} else {{
                btn.innerText = 'Hattı Başlat (Simülasyon)';
                btn.className = 'flex-1 bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold py-3 px-4 rounded-xl transition';
                status.innerText = 'DURDURULDU';
                status.className = 'text-base sm:text-lg font-black text-amber-400';
                speed.innerText = '0.0';
            }}
        }}

        const sectors = {{
            'makine': {{
                title: 'Makine İmalat Sanayisi Web Sitesi',
                desc: 'Ürettiğiniz makinelerin teknik çizimlerini, katalog PDF\\'lerini ve çalışma videolarını profesyonelce sergileyen, yurtdışı ihracat müşterilerine hitap eden hızlı ve SEO uyumlu web sitesi.'
            }},
            'tekstil': {{
                title: 'Tekstil & Kumaş Sarım Tesisleri Web Sitesi',
                desc: 'Kumaş muayene, sarım ve barkodlu tartım hatlarınızı tanıtan, toptan kumaş sipariş formları ve üretim kapasitenizi sergileyen modern web arayüzü.'
            }},
            'torna': {{
                title: 'Talaşlı İmalat, Torna & Kalıp Atölyesi Sitesi',
                desc: 'CNC tezgah parkurunuzu, talaşlı imalat toleranslarınızı ve referans fason işlerinizi kurumsal müşterilere kanıtlayan, teklif talep modüllü web sitesi.'
            }},
            'gida': {{
                title: 'Soğuk Hava Deposu & Gıda İşleme Portalı',
                desc: 'Depolama kapasitenizi, hijyen sertifikalarınızı ve OTS uzaktan izleme standartlarınızı müşterilerinize gösteren prestijli kurumsal web sitesi.'
            }}
        }};

        function switchSector(key) {{
            const s = sectors[key];
            document.getElementById('sector_title').innerText = s.title;
            document.getElementById('sector_desc').innerText = s.desc;
        }}
    </script>
</body>
</html>
"""
    return html
