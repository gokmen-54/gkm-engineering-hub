# -*- coding: utf-8 -*-
"""
Software & Web Solutions Page Generator for GKM Engineering Hub
Focuses on Sakarya & Marmara industrial businesses, factories, and manufacturers.
High-end corporate showcase with real industrial visuals and zero price tags.
"""

import urllib.parse

def generate_software_page(SITE_URL, MAIN_WEBSITE, WHATSAPP_PHONE, PHONE_DISPLAY, header, footer):
    wa_msg = urllib.parse.quote("Merhaba GKM Elektrik & Mühendislik, Sakarya'daki tesisimiz için kurumsal web sitesi / endüstriyel yazılım projesi hakkında yerinde keşif ve teknik görüşme talep ediyoruz.")
    
    html = f"""<!DOCTYPE html>
<html lang="tr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sakarya Sanayi Web Tasarım & Endüstriyel Yazılım Çözümleri | GKM Mühendislik</title>
    <meta name="description" content="Sakarya 1. OSB, Hendek OSB ve Marmara sanayisi için kurumsal fabrika web siteleri, özel üretim takip yazılımları (MES), barkodlu depo ve SCADA izleme sistemleri.">
    <meta name="keywords" content="Sakarya fabrika web tasarım, Sakarya endüstriyel yazılım, Sakarya üretim takip programı, Sakarya OSB web sitesi, Hendek OSB yazılım, fabrika ERP Sakarya, makine imalat web tasarımı">
    
    <link rel="canonical" href="{SITE_URL}/isletme-yazilimlari-web/">
    <meta property="og:title" content="Sakarya Sanayi Web Tasarım & Endüstriyel Yazılım | GKM Mühendislik">
    <meta property="og:description" content="Fabrikanız ve makineleriniz için anahtar teslim kurumsal web siteleri, üretim takip panelleri ve saha yazılımları.">
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
      "name": "GKM Elektrik & Mühendislik - Sanayi Yazılım ve Web Çözümleri",
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
      "areaServed": ["Sakarya", "Adapazarı", "Serdivan", "Erenler", "Hendek", "Akyazı", "Kocaeli", "Bursa"]
    }}
    </script>
</head>
<body class="bg-slate-50 text-slate-900 font-sans antialiased selection:bg-indigo-600 selection:text-white">

    {header}

    <!-- 1. Hero Section (High-End Industrial Tech Presentation) -->
    <section class="relative bg-gradient-to-br from-slate-950 via-[#001c30] to-slate-900 text-white py-20 lg:py-28 overflow-hidden border-b border-slate-800">
        <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-indigo-900/25 via-transparent to-transparent"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 relative z-10">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
                
                <div class="lg:col-span-7">
                    <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-indigo-500/10 border border-indigo-400/20 text-indigo-300 text-xs font-bold uppercase tracking-wider mb-6">
                        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                        Sakarya & Marmara Sanayi Yazılım Merkezi
                    </div>
                    <h1 class="text-3xl sm:text-5xl lg:text-6xl font-black tracking-tight leading-tight mb-6">
                        Makinelerinizi ve Fabrikanızı Bilen <span class="text-transparent bg-clip-text bg-gradient-to-r from-sky-400 via-indigo-300 to-amber-300">Endüstriyel Yazılım & Web</span>
                    </h1>
                    <p class="text-slate-300 text-base sm:text-lg leading-relaxed mb-8 max-w-2xl font-normal">
                        Klasik tasarım ajanslarından farklıyız. Sakarya sanayisindeki fabrikanızı, PLC ve otomasyon panolarınızı, üretim hatlarınızı yerinde analiz ediyor; hem ihracat odaklı prestijli web siteleri hem de sahaya tam entegre üretim yönetim yazılımları geliştiriyoruz.
                    </p>
                    
                    <div class="flex flex-wrap items-center gap-4">
                        <a href="https://wa.me/{WHATSAPP_PHONE}?text={wa_msg}" target="_blank" rel="noopener" class="bg-[#25D366] hover:bg-[#20ba5c] text-white font-black px-7 py-4 rounded-xl shadow-xl shadow-emerald-500/20 transition flex items-center gap-2.5 text-sm sm:text-base">
                            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
                            <span>Yerinde Keşif & Proje Danışın</span>
                        </a>
                        <a href="#cozumler" class="bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold px-6 py-4 rounded-xl border border-slate-700 transition text-sm">
                            Çözümlerimizi İnceleyin ↓
                        </a>
                    </div>

                    <div class="mt-10 pt-8 border-t border-slate-800/80 flex flex-wrap items-center gap-6 text-xs text-slate-400">
                        <span class="flex items-center gap-2">✓ <span>Sahada Ücretsiz Keşif</span></span>
                        <span class="flex items-center gap-2">✓ <span>Endüstriyel PLC/Sensör Entegrasyonu</span></span>
                        <span class="flex items-center gap-2">✓ <span>%100 Mobil & İhracat Uyumlu</span></span>
                    </div>
                </div>

                <!-- Hero Graphic: Sleek Modern Industrial Dashboard Mockup -->
                <div class="lg:col-span-5 relative">
                    <div class="relative mx-auto max-w-lg lg:max-w-none">
                        <div class="rounded-2xl bg-gradient-to-tr from-indigo-500/20 to-sky-500/20 p-2 shadow-2xl backdrop-blur-xl border border-slate-700/60">
                            <div class="rounded-xl bg-slate-900 border border-slate-800 overflow-hidden shadow-2xl">
                                <!-- Window Frame Top -->
                                <div class="bg-slate-950 px-4 py-3 flex items-center justify-between border-b border-slate-800">
                                    <div class="flex items-center gap-2">
                                        <div class="w-3 h-3 rounded-full bg-red-500/80"></div>
                                        <div class="w-3 h-3 rounded-full bg-yellow-500/80"></div>
                                        <div class="w-3 h-3 rounded-full bg-emerald-500/80"></div>
                                        <span class="text-[11px] font-mono text-slate-400 ml-2">gkm-industrial-cloud.local</span>
                                    </div>
                                    <span class="bg-emerald-500/10 text-emerald-400 text-[10px] font-bold px-2 py-0.5 rounded border border-emerald-500/30">ONLINE</span>
                                </div>
                                <!-- Dashboard Content Preview -->
                                <div class="p-5 space-y-4 font-sans">
                                    <div class="flex items-center justify-between">
                                        <div>
                                            <span class="text-xs font-bold text-slate-400 block uppercase tracking-wider">Tesis Yönetim Paneli</span>
                                            <span class="text-base font-black text-white">Sakarya Üretim Hattı #1</span>
                                        </div>
                                        <span class="text-xs bg-indigo-500/20 text-indigo-300 px-2.5 py-1 rounded-md font-semibold">Vardiya: Gündüz</span>
                                    </div>

                                    <!-- Key Metrics Grid -->
                                    <div class="grid grid-cols-2 gap-3">
                                        <div class="bg-slate-950/70 p-3.5 rounded-lg border border-slate-800">
                                            <span class="text-[11px] text-slate-400 block">Hat Verimliliği (OEE)</span>
                                            <span class="text-xl font-black text-emerald-400">%94.2</span>
                                            <span class="text-[10px] text-slate-400 block mt-0.5">Hedefin üzerinde</span>
                                        </div>
                                        <div class="bg-slate-950/70 p-3.5 rounded-lg border border-slate-800">
                                            <span class="text-[11px] text-slate-400 block">Anlık Üretim</span>
                                            <span class="text-xl font-black text-sky-400">4.820 Adet</span>
                                            <span class="text-[10px] text-slate-400 block mt-0.5">Otomatik Barkodlandı</span>
                                        </div>
                                    </div>

                                    <!-- Real Industrial Image Showcase inside mockup -->
                                    <div class="relative rounded-lg overflow-hidden border border-slate-800">
                                        <img src="{SITE_URL}/assets/ikizler_tekstil_kumas_kontrol_barkod.webp" alt="GKM Endüstriyel Yazılım Saha Entegrasyonu" class="w-full h-40 object-cover">
                                        <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/30 to-transparent flex items-end p-3">
                                            <span class="text-[11px] font-bold text-white flex items-center gap-1.5">
                                                <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                                                Saha Donanımı & HMI Ekranları Doğrudan Web'e Bağlı
                                            </span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- 2. Core Solutions Grid (Sektörel Hizmetlerimiz) -->
    <section id="cozumler" class="py-20 lg:py-28 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6">
            
            <div class="text-center max-w-3xl mx-auto mb-16">
                <span class="text-indigo-600 font-extrabold text-xs uppercase tracking-widest">Endüstriyel Çözüm Portföyümüz</span>
                <h2 class="text-3xl sm:text-4xl font-black text-slate-900 mt-2 mb-4 tracking-tight">
                    Fabrikanız İçin Uçtan Uca Dijital Çözümler
                </h2>
                <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
                    İster firmanızı dünya pazarına açacak modern bir kurumsal web sitesi, ister fabrikanızdaki fireyi sıfıra indirecek özel bir üretim yönetim yazılımı.
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                
                <!-- Service 1: Kurumsal Sanayi & Makine Web Siteleri -->
                <div class="bg-slate-50 border border-slate-200 rounded-3xl p-8 hover:shadow-xl hover:border-indigo-400 transition-all duration-300 flex flex-col justify-between group">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-indigo-600/10 text-indigo-600 flex items-center justify-center font-black text-xl mb-6">
                            🌐
                        </div>
                        <h3 class="text-2xl font-black text-slate-900 mb-3 group-hover:text-indigo-600 transition">
                            Kurumsal Sanayi & Fabrika Web Siteleri
                        </h3>
                        <p class="text-slate-600 text-sm leading-relaxed mb-6">
                            Yurtiçi ve yurtdışı müşterilerinizin güven duyacağı, makine parkurunuzu, teknik kapasitenizi ve referanslarınızı en yüksek kalitede sergileyen profesyonel web platformları.
                        </p>
                        <ul class="text-xs sm:text-sm text-slate-700 space-y-2.5 mb-8">
                            <li class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> Çok Dilli Altyapı (İngilizce, Almanca, Rusça, Arapça İhracat Desteği)</li>
                            <li class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> Makine Katalogları & Teknik PDF İndirme Modülleri</li>
                            <li class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> Mobil, Tablet ve Masaüstü Cihazlara %100 Duyarlı (Responsive)</li>
                            <li class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> Google Arama Motoru (SEO) & Kurumsal E-Posta Yapılandırması</li>
                        </ul>
                    </div>
                    <div class="pt-6 border-t border-slate-200 flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-500">Teslim Süresi: Hızlı & Anahtar Teslim</span>
                        <a href="https://wa.me/{WHATSAPP_PHONE}?text={urllib.parse.quote('Merhaba GKM Mühendislik, kurumsal sanayi web sitesi projemiz için görüşmek istiyoruz.')}" target="_blank" class="text-indigo-600 hover:text-indigo-800 font-black text-xs sm:text-sm flex items-center gap-1">
                            Teklif Alın ➔
                        </a>
                    </div>
                </div>

                <!-- Service 2: Özel Üretim & Vardiya Takip Yazılımları (MES) -->
                <div class="bg-slate-50 border border-slate-200 rounded-3xl p-8 hover:shadow-xl hover:border-indigo-400 transition-all duration-300 flex flex-col justify-between group">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-sky-600/10 text-sky-600 flex items-center justify-center font-black text-xl mb-6">
                            ⚙️
                        </div>
                        <h3 class="text-2xl font-black text-slate-900 mb-3 group-hover:text-sky-600 transition">
                            Özel Üretim Takip & Vardiya Yazılımları (MES)
                        </h3>
                        <p class="text-slate-600 text-sm leading-relaxed mb-6">
                            Makinelerinizden enstantane veri toplayıp hangi operatörün kaç adet ürettiğini, ne kadar duruş yapıldığını ve anlık hat verimini ekranınıza getiren terzi işi yazılımlar.
                        </p>
                        <ul class="text-xs sm:text-sm text-slate-700 space-y-2.5 mb-8">
                            <li class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> PLC ve Enkoderler ile Donanımsal Haberleşme</li>
                            <li class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> Vardiya Sonu Otomatik Excel, PDF ve WhatsApp Üretim Raporu</li>
                            <li class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> Duruş Sebebi Analizi & Operatör Performans Takibi</li>
                            <li class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> Fabrika Yerel Ağında (LAN) Güvenli ve Kesintisiz Çalışma</li>
                        </ul>
                    </div>
                    <div class="pt-6 border-t border-slate-200 flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-500">Makinelerinize Özel Mühendislik</span>
                        <a href="https://wa.me/{WHATSAPP_PHONE}?text={urllib.parse.quote('Merhaba GKM Mühendislik, üretim ve vardiya takip yazılımı projemiz için bilgi almak istiyoruz.')}" target="_blank" class="text-sky-600 hover:text-sky-800 font-black text-xs sm:text-sm flex items-center gap-1">
                            Keşif İsteyin ➔
                        </a>
                    </div>
                </div>

                <!-- Service 3: Barkodlu Depo & Tartım Otomasyonu -->
                <div class="bg-slate-50 border border-slate-200 rounded-3xl p-8 hover:shadow-xl hover:border-indigo-400 transition-all duration-300 flex flex-col justify-between group">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-amber-600/10 text-amber-600 flex items-center justify-center font-black text-xl mb-6">
                            🏷️
                        </div>
                        <h3 class="text-2xl font-black text-slate-900 mb-3 group-hover:text-amber-600 transition">
                            Barkodlu Depo, Terazi & Sevkiyat Yazılımları
                        </h3>
                        <p class="text-slate-600 text-sm leading-relaxed mb-6">
                            Endüstriyel terazi, barkod yazıcı ve el terminallerini tek bir merkezde birleştiren; hammadde girişinden nihai sevk irsaliyesine kadar hatasız stok yönetimi.
                        </p>
                        <ul class="text-xs sm:text-sm text-slate-700 space-y-2.5 mb-8">
                            <li class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> Otomatik Tartım ve Canlı Kilo/Metraj Barkod Basımı</li>
                            <li class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> QR Kod & EAN-13 Standartlarında Etiketleme</li>
                            <li class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> El Terminali İle Hızlı Sevkiyat Doğrulama</li>
                            <li class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> Logo, Mikro vb. Mevcut Muhasebe Programlarıyla Entegrasyon</li>
                        </ul>
                    </div>
                    <div class="pt-6 border-t border-slate-200 flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-500">Saha Donanımı Dahil Proje</span>
                        <a href="https://wa.me/{WHATSAPP_PHONE}?text={urllib.parse.quote('Merhaba GKM Mühendislik, barkodlu terazi ve depo yazılımı için görüşmek istiyoruz.')}" target="_blank" class="text-amber-600 hover:text-amber-800 font-black text-xs sm:text-sm flex items-center gap-1">
                            Detaylı Bilgi ➔
                        </a>
                    </div>
                </div>

                <!-- Service 4: Web SCADA & Uzaktan Tesis İzleme -->
                <div class="bg-slate-50 border border-slate-200 rounded-3xl p-8 hover:shadow-xl hover:border-indigo-400 transition-all duration-300 flex flex-col justify-between group">
                    <div>
                        <div class="w-12 h-12 rounded-2xl bg-emerald-600/10 text-emerald-600 flex items-center justify-center font-black text-xl mb-6">
                            📊
                        </div>
                        <h3 class="text-2xl font-black text-slate-900 mb-3 group-hover:text-emerald-600 transition">
                            Web Tabanlı SCADA & Uzaktan Tesis İzleme
                        </h3>
                        <p class="text-slate-600 text-sm leading-relaxed mb-6">
                            Soğuk hava depoları, kompresör odaları, arıtma tesisleri ve enerji analizörlerinizi dünyanın neresinde olursanız olun tarayıcınızdan ve telefonunuzdan canlı izleyin.
                        </p>
                        <ul class="text-xs sm:text-sm text-slate-700 space-y-2.5 mb-8">
                            <li class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> Sıcaklık, Nem, Basınç ve Elektrik Tüketimi Canlı Grafikleri</li>
                            <li class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> Kritik Eşik Değerlerinde SMS & WhatsApp Acil Alarm Uyarısı</li>
                            <li class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> Tarayıcı Üzerinden Yetkili Kullanıcı Girişi & Güvenlik</li>
                            <li class="flex items-center gap-2"><span class="text-emerald-500 font-bold">✓</span> Geçmişe Dönük Sıcaklık ve Tüketim Arşivi (HACCP Uyumluluğu)</li>
                        </ul>
                    </div>
                    <div class="pt-6 border-t border-slate-200 flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-500">7/24 Kesintisiz Veri İzleme</span>
                        <a href="https://wa.me/{WHATSAPP_PHONE}?text={urllib.parse.quote('Merhaba GKM Mühendislik, web tabanlı SCADA ve uzaktan tesis izleme projemiz hakkında görüşmek istiyoruz.')}" target="_blank" class="text-emerald-600 hover:text-emerald-800 font-black text-xs sm:text-sm flex items-center gap-1">
                            Sistemi Danışın ➔
                        </a>
                    </div>
                </div>

            </div>

        </div>
    </section>

    <!-- 3. Real Engineering Showcase Visuals Gallery -->
    <section class="py-20 bg-slate-900 text-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <span class="text-sky-400 font-extrabold text-xs uppercase tracking-widest">Sahadaki Gerçek Mühendislik</span>
                <h2 class="text-3xl sm:text-4xl font-black mt-2 mb-4">Saha ve Donanımla Bütünleşen Yazılımlar</h2>
                <p class="text-slate-400 text-sm sm:text-base">Projelerimizi sadece ofiste masa başında değil, doğrudan fabrikanızın panoları ve makineleri başında test edip teslim ediyoruz.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- Project Visual 1 -->
                <div class="rounded-2xl overflow-hidden bg-slate-950 border border-slate-800 group hover:border-sky-500 transition duration-300">
                    <div class="h-56 overflow-hidden">
                        <img src="{SITE_URL}/assets/ikizler_tekstil_kumas_kontrol_barkod.webp" alt="Kumaş Kontrol ve Barkodlu Yazılım" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                    </div>
                    <div class="p-6">
                        <span class="text-[10px] font-bold text-sky-400 uppercase tracking-wider block mb-1">Tekstil & Sarım Hatları</span>
                        <h4 class="text-lg font-black text-white mb-2">Barkodlu Metraj & Tartım Yazılımı</h4>
                        <p class="text-xs text-slate-400 leading-relaxed">
                            Makinadan PLC ile gelen metre bilgisini terazi kilosuyla eşleştirip otomatik barkod etiketi basan saha yazılımımız.
                        </p>
                    </div>
                </div>

                <!-- Project Visual 2 -->
                <div class="rounded-2xl overflow-hidden bg-slate-950 border border-slate-800 group hover:border-sky-500 transition duration-300">
                    <div class="h-56 overflow-hidden">
                        <img src="{SITE_URL}/assets/ots_soguk_hava_deposu_otomasyonu.webp" alt="Soğuk Hava Deposu SCADA İzleme" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                    </div>
                    <div class="p-6">
                        <span class="text-[10px] font-bold text-emerald-400 uppercase tracking-wider block mb-1">Gıda & Depolama</span>
                        <h4 class="text-lg font-black text-white mb-2">Merkezi SCADA & Sıcaklık Takip Portalı</h4>
                        <p class="text-xs text-slate-400 leading-relaxed">
                            Odalardaki sensörleri tek ekranda toplayan, limit aşımlarında yetkililere anında acil bildirim ileten izleme sistemi.
                        </p>
                    </div>
                </div>

                <!-- Project Visual 3 -->
                <div class="rounded-2xl overflow-hidden bg-slate-950 border border-slate-800 group hover:border-sky-500 transition duration-300">
                    <div class="h-56 overflow-hidden">
                        <img src="{SITE_URL}/assets/gkm_otomatik_boy_kesim_hmi.webp" alt="Makine HMI ve Web Raporlama" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                    </div>
                    <div class="p-6">
                        <span class="text-[10px] font-bold text-amber-400 uppercase tracking-wider block mb-1">Özel Makine İmalatı</span>
                        <h4 class="text-lg font-black text-white mb-2">Makine Operatör Arayüzü & Web Bağlantısı</h4>
                        <p class="text-xs text-slate-400 leading-relaxed">
                            Dokunmatik operatör panelleriyle fabrika veri tabanını senkronize ederek parça başı süreyi ve verimi ölçen mimari.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. Why GKM Engineering Comparison (Farkımız) -->
    <section class="py-20 bg-slate-50 border-t border-slate-200">
        <div class="max-w-5xl mx-auto px-4 sm:px-6">
            <div class="text-center mb-16">
                <span class="text-indigo-600 font-extrabold text-xs uppercase tracking-widest">Neden Birlikte Çalışmalıyız?</span>
                <h2 class="text-3xl sm:text-4xl font-black text-slate-900 mt-2">Klasik Web Ajansı vs. GKM Mühendislik</h2>
            </div>

            <div class="bg-white rounded-3xl border border-slate-200 shadow-xl overflow-hidden">
                <div class="grid grid-cols-1 md:grid-cols-2 divide-y md:divide-y-0 md:divide-x divide-slate-200">
                    
                    <div class="p-8 sm:p-10 bg-slate-50/50">
                        <span class="text-red-500 font-black text-xs uppercase tracking-wider block mb-2">✕ Klasik Web / Yazılım Ajansları</span>
                        <h3 class="text-xl font-bold text-slate-900 mb-4">Fabrika Kokusunu Bilmeyenler</h3>
                        <ul class="space-y-4 text-xs sm:text-sm text-slate-600">
                            <li class="flex items-start gap-2">
                                <span class="text-red-500 font-bold">✕</span>
                                <span>PLC, pano, enversör, servo sürücü gibi kavramları bilmezler; teknik ürünlerinizi doğru ifade edemezler.</span>
                            </li>
                            <li class="flex items-start gap-2">
                                <span class="text-red-500 font-bold">✕</span>
                                <span>Fabrikanın gürültülü ve tozlu sahasına inip makinelerinize doğrudan veri kablosu bağlayamazlar.</span>
                            </li>
                            <li class="flex items-start gap-2">
                                <span class="text-red-500 font-bold">✕</span>
                                <span>Standart hazır şablonları kopyalayıp teslim ederler; özel üretim akışınıza uyum sağlayamazlar.</span>
                            </li>
                        </ul>
                    </div>

                    <div class="p-8 sm:p-10 bg-indigo-50/30">
                        <span class="text-emerald-600 font-black text-xs uppercase tracking-wider block mb-2">✓ GKM Elektrik & Mühendislik</span>
                        <h3 class="text-xl font-black text-indigo-950 mb-4">Mühendislik ve Saha Tecrübesi</h3>
                        <ul class="space-y-4 text-xs sm:text-sm text-slate-700 font-medium">
                            <li class="flex items-start gap-2">
                                <span class="text-emerald-600 font-bold text-base">✓</span>
                                <span>Hem elektrik-otomasyon panosunu üreten hem de yazılımını yazan entegre mühendislik ekibiyiz.</span>
                            </li>
                            <li class="flex items-start gap-2">
                                <span class="text-emerald-600 font-bold text-base">✓</span>
                                <span>Sakarya'da yerel olarak tesisinize gelip ihtiyacınızı bizzat operatörleriniz ve müdürlerinizle görüşürüz.</span>
                            </li>
                            <li class="flex items-start gap-2">
                                <span class="text-emerald-600 font-bold text-base">✓</span>
                                <span>İhracat standartlarında hızlı, modern, kurumsal ve işletmenize değer katan kalıcı çözümler sunarız.</span>
                            </li>
                        </ul>
                    </div>

                </div>
            </div>
        </div>
    </section>

    <!-- 5. Sakarya Districts & Industrial Zones -->
    <section class="py-16 bg-white border-t border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6">
            <div class="text-center max-w-2xl mx-auto mb-10">
                <h3 class="text-xl sm:text-2xl font-black text-slate-900">Bölge Sanayisine Birebir Hizmet Ağı</h3>
                <p class="text-slate-600 text-xs sm:text-sm mt-1.5">Tesisinize bir telefon kadar yakınız. Keşif ve teknik analiz için yerinde ziyaret ediyoruz.</p>
            </div>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3.5 text-center font-bold text-xs text-slate-700">
                <div class="bg-slate-50 border border-slate-200 p-3.5 rounded-xl">📍 Sakarya 1. OSB</div>
                <div class="bg-slate-50 border border-slate-200 p-3.5 rounded-xl">📍 Hendek 2. OSB</div>
                <div class="bg-slate-50 border border-slate-200 p-3.5 rounded-xl">📍 Söğütlü 3. OSB</div>
                <div class="bg-slate-50 border border-slate-200 p-3.5 rounded-xl">📍 Adapazarı Sanayi</div>
                <div class="bg-slate-50 border border-slate-200 p-3.5 rounded-xl">📍 Serdivan & Erenler</div>
                <div class="bg-slate-50 border border-slate-200 p-3.5 rounded-xl">📍 Akyazı Sanayi</div>
                <div class="bg-slate-50 border border-slate-200 p-3.5 rounded-xl">📍 Karasu Liman Bölgesi</div>
                <div class="bg-slate-50 border border-slate-200 p-3.5 rounded-xl">📍 Kocaeli & Dilovası</div>
            </div>
        </div>
    </section>

    <!-- 6. Bottom Conversion CTA (Direct Meeting & Discovery) -->
    <section class="py-16 bg-[#001c30] text-white text-center border-t border-slate-800">
        <div class="max-w-4xl mx-auto px-4 sm:px-6">
            <span class="text-amber-400 font-extrabold text-xs uppercase tracking-widest block mb-3">Teknik Görüşme & Ücretsiz Keşif</span>
            <h2 class="text-2xl sm:text-4xl font-black mb-4">Fabrikanız İçin Doğru Yazılımı Birlikte Belirleyelim</h2>
            <p class="text-slate-300 text-sm sm:text-base mb-8 max-w-2xl mx-auto leading-relaxed">
                İster yeni bir kurumsal web sitesi, ister üretim takip sistemi. İhtiyacınızı yerinde dinleyelim, mühendislik ekibimizle işletmenize en uygun çözümü projelendirelim.
            </p>
            <div class="flex flex-wrap items-center justify-center gap-4">
                <a href="https://wa.me/{WHATSAPP_PHONE}?text={wa_msg}" target="_blank" rel="noopener" class="bg-[#25D366] hover:bg-[#20ba5c] text-white font-black px-8 py-4 rounded-xl shadow-xl shadow-emerald-500/25 transition flex items-center gap-2.5 text-sm sm:text-base">
                    <span>💬 WhatsApp İle Projenizi Danışın</span>
                </a>
                <a href="tel:{WHATSAPP_PHONE}" class="bg-slate-800 hover:bg-slate-700 text-white font-bold px-7 py-4 rounded-xl border border-slate-700 transition text-sm sm:text-base flex items-center gap-2">
                    <span>📞 {PHONE_DISPLAY}</span>
                </a>
            </div>
        </div>
    </section>

    {footer}

</body>
</html>
"""
    return html
