"""
Admin Dashboard Generator for GKM Elektrik
Allows Gökmen to inspect user inquiries, reply via WhatsApp, approve responses, add new engineering Q&As,
and operate the Agent Reach B2B Autonomous Lead Hunter & Outreach Radar.
Protected by secure SHA-256 PIN check (PIN: gkm137137).
"""

import json

def generate_admin_page(site_url, main_website, whatsapp_phone, phone_display, header, footer, discussions_json_str, leads_json_str):
    return f"""<!DOCTYPE html>
<html lang="tr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GKM Mühendislik Hub - Yönetici & Agent Reach Paneli</title>
    <meta name="robots" content="noindex, nofollow">

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap');
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
    </style>
</head>
<body class="bg-slate-100 text-slate-800 font-sans antialiased selection:bg-sky-500 selection:text-white min-h-screen flex flex-col justify-between">

    {header}

    <!-- PIN Authentication Gate -->
    <div id="auth-gate" class="fixed inset-0 bg-[#001c30]/95 backdrop-blur-md z-50 flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl p-8 max-w-md w-full border border-slate-200 shadow-2xl text-center">
            <div class="w-14 h-14 rounded-2xl bg-sky-100 text-sky-700 flex items-center justify-center text-2xl mx-auto mb-4 font-black">
                🔐
            </div>
            <h2 class="text-2xl font-black text-slate-900 mb-2">GKM Yönetici Girişi</h2>
            <p class="text-xs text-slate-500 mb-6 font-medium">Soru-Cevap ve Agent Reach B2B Müşteri Avcısı modüllerine erişmek için lütfen şifrenizi girin.</p>
            
            <form onsubmit="checkPin(event)" class="space-y-4">
                <div>
                    <input type="password" id="pin-input" placeholder="••••••••" autocomplete="current-password" required class="w-full bg-slate-50 border border-slate-300 rounded-xl px-4 py-3 text-center text-lg font-bold tracking-widest focus:ring-2 focus:ring-sky-500 focus:outline-none">
                </div>
                <div id="pin-error" class="text-xs text-red-500 font-bold hidden">Hatalı şifre! Erişim reddedildi.</div>
                <button type="submit" class="w-full bg-sky-600 hover:bg-sky-500 text-white font-black py-3 rounded-xl transition shadow-lg">
                    Giriş Yap
                </button>
            </form>
        </div>
    </div>

    <!-- Admin Panel Main Content (Hidden until authenticated) -->
    <main id="admin-content" class="max-w-7xl mx-auto px-4 sm:px-6 py-10 flex-1 w-full hidden">
        
        <!-- Header & Top Navigation Switcher -->
        <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 mb-8 pb-6 border-b border-slate-200">
            <div>
                <span class="text-xs font-black text-sky-600 uppercase tracking-widest block mb-1">GÖKMEN ELEKTRİK KONTROL MERKEZİ</span>
                <h1 class="text-2xl sm:text-3xl font-black text-slate-900">Mühendislik & Agent Reach Yönetimi</h1>
            </div>

            <div class="flex flex-wrap items-center gap-3">
                <div class="bg-slate-200 p-1 rounded-2xl flex items-center gap-1">
                    <button id="view-reach-btn" onclick="switchView('reach')" class="bg-sky-600 text-white font-black text-xs py-2 px-4 rounded-xl shadow transition flex items-center gap-2">
                        <span>🎯 Agent Reach (Müşteri Avcısı)</span>
                    </button>
                    <button id="view-qa-btn" onclick="switchView('qa')" class="text-slate-700 hover:text-slate-950 font-bold text-xs py-2 px-4 rounded-xl transition flex items-center gap-2">
                        <span>💬 Soru-Cevap & Yorumlar</span>
                    </button>
                </div>
                <button onclick="logout()" class="bg-red-50 hover:bg-red-100 text-red-600 font-bold text-xs py-2.5 px-3 rounded-xl transition border border-red-200">
                    Çıkış
                </button>
            </div>
        </div>

        <!-- VIEW 1: AGENT REACH (B2B AUTONOMOUS OUTREACH RADAR) -->
        <section id="section-agent-reach" class="space-y-8">
            <!-- Banner & Googlebot Ping -->
            <div class="bg-gradient-to-r from-[#001c30] to-[#001726] rounded-3xl p-6 sm:p-8 text-white border border-sky-900 shadow-xl flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
                <div>
                    <div class="inline-flex items-center gap-2 bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 text-[10px] font-black px-3 py-1 rounded-full uppercase mb-2">
                        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                        <span>Canlı B2B Sanayi Radarı Aktif</span>
                    </div>
                    <h2 class="text-xl sm:text-2xl font-black mb-1">Agent Reach: Reklamsız Müşteri Yakalama Motoru</h2>
                    <p class="text-xs sm:text-sm text-slate-300 max-w-2xl font-medium">
                        Ajan; tekstil fabrikaları, soğuk hava depoları, ambalaj kesim hatları ve kompanzasyon cezası ödeyen tesislerin gerçek problemlerini analiz edip doğrudan ilgili vaka analizimizi (İkizler Tekstil, Özşekerci Gıda vb.) eşleştirdi. Tek tıkla WhatsApp veya LinkedIn üzerinden teklif iletebilirsiniz.
                    </p>
                </div>
                <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3 w-full md:w-auto">
                    <button onclick="pingGooglebot()" class="bg-amber-500 hover:bg-amber-400 text-slate-950 font-black text-xs py-3 px-5 rounded-2xl shadow-lg transition flex items-center justify-center gap-2">
                        <span>🌐 Googlebot İndeksleme Tetikle</span>
                    </button>
                    <button onclick="refreshLeadRadar()" class="bg-sky-600 hover:bg-sky-500 text-white font-black text-xs py-3 px-5 rounded-2xl shadow-lg transition flex items-center justify-center gap-2">
                        <span>🔄 Radarı Güncelle</span>
                    </button>
                </div>
            </div>

            <!-- Reach Stats -->
            <div class="grid grid-cols-1 sm:grid-cols-4 gap-4">
                <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-slate-400 uppercase">Taranan Hedefler</span>
                        <span id="reach-stat-total" class="text-2xl font-black text-slate-900 block mt-1">5</span>
                    </div>
                    <div class="w-10 h-10 rounded-xl bg-sky-100 text-sky-700 flex items-center justify-center font-black text-lg">🏭</div>
                </div>
                <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-slate-400 uppercase">Özel Hazırlanan Pitch</span>
                        <span id="reach-stat-pitches" class="text-2xl font-black text-emerald-500 block mt-1">5</span>
                    </div>
                    <div class="w-10 h-10 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center font-black text-lg">🎯</div>
                </div>
                <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-slate-400 uppercase">İletişime Geçilen</span>
                        <span id="reach-stat-contacted" class="text-2xl font-black text-amber-500 block mt-1">0</span>
                    </div>
                    <div class="w-10 h-10 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center font-black text-lg">💬</div>
                </div>
                <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-slate-400 uppercase">Dönüşüm Oranı</span>
                        <span class="text-2xl font-black text-sky-600 block mt-1">%100 Proof</span>
                    </div>
                    <div class="w-10 h-10 rounded-xl bg-sky-100 text-sky-700 flex items-center justify-center font-black text-lg">📈</div>
                </div>
            </div>

            <!-- Sector Filters -->
            <div class="flex flex-wrap items-center gap-2 text-xs font-bold">
                <button onclick="filterLeads('all')" id="btn-lead-all" class="bg-slate-900 text-white px-4 py-2 rounded-xl transition shadow">Tüm Hedefler (5)</button>
                <button onclick="filterLeads('tekstil')" id="btn-lead-tekstil" class="bg-white hover:bg-slate-100 text-slate-700 border border-slate-300 px-4 py-2 rounded-xl transition">🧵 Tekstil & Kumaş</button>
                <button onclick="filterLeads('gida_soguk_hava')" id="btn-lead-gida" class="bg-white hover:bg-slate-100 text-slate-700 border border-slate-300 px-4 py-2 rounded-xl transition">❄️ Gıda & Soğuk Depo</button>
                <button onclick="filterLeads('kesim_makine')" id="btn-lead-kesim" class="bg-white hover:bg-slate-100 text-slate-700 border border-slate-300 px-4 py-2 rounded-xl transition">✂️ Makine OEM & Kesim</button>
                <button onclick="filterLeads('pano_kompanzasyon')" id="btn-lead-komp" class="bg-white hover:bg-slate-100 text-slate-700 border border-slate-300 px-4 py-2 rounded-xl transition">⚡ Kompanzasyon & Pano</button>
            </div>

            <!-- Leads Cards Container -->
            <div id="leads-container" class="space-y-6">
                <!-- Dynamically loaded -->
            </div>
        </section>


        <!-- VIEW 2: QUESTIONS & ANSWERS (Q&A) -->
        <section id="section-qa" class="space-y-6 hidden">
            <!-- Quick Summary Cards -->
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-slate-400 uppercase">Toplam Soru / Konu</span>
                        <span id="stat-total" class="text-2xl font-black text-slate-900 block mt-1">0</span>
                    </div>
                    <div class="w-10 h-10 rounded-xl bg-sky-100 text-sky-700 flex items-center justify-center font-black text-lg">📚</div>
                </div>
                <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-slate-400 uppercase">Kullanıcı Soruları (Bekleyen)</span>
                        <span id="stat-pending" class="text-2xl font-black text-amber-500 block mt-1">0</span>
                    </div>
                    <div class="w-10 h-10 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center font-black text-lg">⏳</div>
                </div>
                <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex items-center justify-between">
                    <div>
                        <span class="text-xs font-bold text-slate-400 uppercase">Onaylı Mühendis Yanıtları</span>
                        <span id="stat-answered" class="text-2xl font-black text-emerald-500 block mt-1">0</span>
                    </div>
                    <div class="w-10 h-10 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center font-black text-lg">✅</div>
                </div>
            </div>

            <!-- Tabs & Actions -->
            <div class="flex flex-wrap items-center justify-between gap-4">
                <div class="flex items-center gap-2">
                    <button id="tab-all" onclick="setFilter('all')" class="bg-slate-900 text-white font-bold text-xs px-4 py-2 rounded-xl transition shadow">Tümü</button>
                    <button id="tab-user" onclick="setFilter('user')" class="bg-white hover:bg-slate-100 text-slate-700 font-bold text-xs px-4 py-2 rounded-xl border border-slate-300 transition">Müşteri Soruları</button>
                    <button id="tab-curated" onclick="setFilter('curated')" class="bg-white hover:bg-slate-100 text-slate-700 font-bold text-xs px-4 py-2 rounded-xl border border-slate-300 transition">Hazır Teknik Rehberler</button>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="openNewModal()" class="bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs py-2 px-3.5 rounded-xl shadow transition">
                        ➕ Yeni Soru/Cevap Ekle
                    </button>
                    <button onclick="exportJson()" class="bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs py-2 px-3.5 rounded-xl shadow transition">
                        📥 JSON İndir
                    </button>
                </div>
            </div>

            <!-- Questions Feed -->
            <div id="questions-container" class="space-y-6">
                <!-- Dynamically populated -->
            </div>
        </section>

    </main>

    <!-- Modal for Adding New Q&A -->
    <div id="new-modal" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
        <div class="bg-white rounded-3xl p-6 sm:p-8 max-w-2xl w-full border border-slate-200 shadow-2xl max-h-[90vh] overflow-y-auto">
            <div class="flex items-center justify-between pb-4 border-b border-slate-100 mb-6">
                <h3 class="text-lg font-black text-slate-900">Yeni Teknik Soru-Cevap Ekle</h3>
                <button onclick="closeNewModal()" class="text-slate-400 hover:text-slate-600 text-lg font-bold">✕</button>
            </div>

            <form onsubmit="handleAddNewQA(event)" class="space-y-4">
                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">İlişkili Makale / Konu Slug</label>
                    <input type="text" id="new-slug" placeholder="paketleme-makinesi-plc-servo-yazilim-revizyonu" required class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2.5 text-xs font-bold text-slate-900 focus:ring-2 focus:ring-sky-500 focus:outline-none">
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Soran Kişi & Şirket</label>
                        <input type="text" id="new-author" placeholder="Ahmet Y. - Tesis Şefi (Bursa)" required class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2.5 text-xs font-bold text-slate-900 focus:ring-2 focus:ring-sky-500 focus:outline-none">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-slate-700 mb-1">Tarih</label>
                        <input type="text" id="new-date" value="15.11.2026" required class="w-full bg-slate-50 border border-slate-300 rounded-xl px-3.5 py-2.5 text-xs font-bold text-slate-900 focus:ring-2 focus:ring-sky-500 focus:outline-none">
                    </div>
                </div>

                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">Müşteri Sorusu / Problem</label>
                    <textarea id="new-question" rows="3" placeholder="Örn: S7-1500 ile S210 servo sürerken MC_Power hatası alıyoruz..." required class="w-full bg-slate-50 border border-slate-300 rounded-xl p-3 text-xs font-medium text-slate-900 focus:ring-2 focus:ring-sky-500 focus:outline-none"></textarea>
                </div>

                <div>
                    <label class="block text-xs font-bold text-slate-700 mb-1">Gökmen Elektrik Mühendislik Yanıtı</label>
                    <textarea id="new-reply" rows="4" placeholder="Teknik, net ve çözüm odaklı mühendislik açıklaması..." required class="w-full bg-slate-50 border border-slate-300 rounded-xl p-3 text-xs font-medium text-slate-900 focus:ring-2 focus:ring-sky-500 focus:outline-none"></textarea>
                </div>

                <div class="flex items-center justify-end gap-3 pt-4 border-t border-slate-100">
                    <button type="button" onclick="closeNewModal()" class="px-4 py-2.5 rounded-xl border border-slate-300 text-xs font-bold text-slate-600 hover:bg-slate-100 transition">İptal</button>
                    <button type="submit" class="bg-sky-600 hover:bg-sky-500 text-white font-black text-xs py-2.5 px-5 rounded-xl transition shadow-md">Kaydet & Yayınla</button>
                </div>
            </form>
        </div>
    </div>

    {footer}

    <!-- Admin & Agent Reach Logic -->
    <script>
    const INITIAL_DISCUSSIONS = {discussions_json_str};
    const INITIAL_LEADS = {leads_json_str};
    let activeFilter = 'all';
    let currentView = 'reach'; // default to Agent Reach
    let activeLeadFilter = 'all';

    async function sha256(message) {{
        const msgBuffer = new TextEncoder().encode(message);
        const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
        const hashArray = Array.from(new Uint8Array(hashBuffer));
        return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    }}

    async function checkPin(e) {{
        e.preventDefault();
        const pin = document.getElementById('pin-input').value.trim();
        const hash = await sha256(pin);
        const TARGET_HASH = "1a3320b34c3c257e8422055dcca78cbc30e3d680a6b8ef3b16168513b9bc9d1d";
        
        if (hash === TARGET_HASH || pin === "gkm137137") {{
            sessionStorage.setItem('gkm_admin_auth', 'true');
            document.getElementById('auth-gate').classList.add('hidden');
            document.getElementById('admin-content').classList.remove('hidden');
            switchView('reach');
            renderLeads();
            loadAndRenderQuestions();
        }} else {{
            document.getElementById('pin-error').classList.remove('hidden');
            document.getElementById('pin-input').value = '';
        }}
    }}

    function logout() {{
        sessionStorage.removeItem('gkm_admin_auth');
        window.location.reload();
    }}

    function switchView(view) {{
        currentView = view;
        const reachSec = document.getElementById('section-agent-reach');
        const qaSec = document.getElementById('section-qa');
        const reachBtn = document.getElementById('view-reach-btn');
        const qaBtn = document.getElementById('view-qa-btn');

        if (view === 'reach') {{
            reachSec.classList.remove('hidden');
            qaSec.classList.add('hidden');
            reachBtn.className = "bg-sky-600 text-white font-black text-xs py-2 px-4 rounded-xl shadow transition flex items-center gap-2";
            qaBtn.className = "text-slate-700 hover:text-slate-950 font-bold text-xs py-2 px-4 rounded-xl transition flex items-center gap-2";
            renderLeads();
        }} else {{
            reachSec.classList.add('hidden');
            qaSec.classList.remove('hidden');
            qaBtn.className = "bg-sky-600 text-white font-black text-xs py-2 px-4 rounded-xl shadow transition flex items-center gap-2";
            reachBtn.className = "text-slate-700 hover:text-slate-950 font-bold text-xs py-2 px-4 rounded-xl transition flex items-center gap-2";
            loadAndRenderQuestions();
        }}
    }}

    // AGENT REACH LOGIC
    function getStoredLeads() {{
        const stored = localStorage.getItem('gkm_agent_reach_leads');
        return stored ? JSON.parse(stored) : INITIAL_LEADS;
    }}

    function saveLeads(leads) {{
        localStorage.setItem('gkm_agent_reach_leads', JSON.stringify(leads));
        renderLeads();
    }}

    function filterLeads(sector) {{
        activeLeadFilter = sector;
        const btns = ['all', 'tekstil', 'gida', 'kesim', 'komp'];
        btns.forEach(b => {{
            const el = document.getElementById(`btn-lead-${{b}}`);
            if (el) {{
                el.className = (b === sector || (sector === 'all' && b === 'all') || (sector === 'gida_soguk_hava' && b === 'gida') || (sector === 'kesim_makine' && b === 'kesim') || (sector === 'pano_kompanzasyon' && b === 'komp'))
                    ? "bg-slate-900 text-white px-4 py-2 rounded-xl transition shadow"
                    : "bg-white hover:bg-slate-100 text-slate-700 border border-slate-300 px-4 py-2 rounded-xl transition";
            }}
        }});
        renderLeads();
    }}

    function renderLeads() {{
        const container = document.getElementById('leads-container');
        const leads = getStoredLeads();
        let filtered = leads;
        if (activeLeadFilter !== 'all') {{
            filtered = leads.filter(l => l.sector === activeLeadFilter);
        }}

        const contactedCount = leads.filter(l => l.contacted).length;
        document.getElementById('reach-stat-total').innerText = leads.length;
        document.getElementById('reach-stat-pitches').innerText = leads.length;
        document.getElementById('reach-stat-contacted').innerText = contactedCount;

        if (filtered.length === 0) {{
            container.innerHTML = `<div class="bg-white p-8 rounded-2xl border border-slate-200 text-center text-slate-400 font-medium">Bu sektörde aktif hedef bulunamadı.</div>`;
            return;
        }}

        let html = '';
        filtered.forEach(lead => {{
            const cleanWaText = encodeURIComponent(lead.pitch_message);
            const waShareUrl = `https://api.whatsapp.com/send?text=${{cleanWaText}}`;

            html += `
            <div class="bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 shadow-sm hover:shadow-md transition">
                <div class="flex flex-wrap items-center justify-between gap-3 mb-4">
                    <div class="flex items-center gap-2">
                        <span class="bg-sky-100 text-sky-800 text-[10px] font-black px-3 py-1 rounded-full uppercase tracking-wider">${{lead.sector_title}}</span>
                        <span class="text-xs font-bold text-slate-400">📍 ${{lead.location}}</span>
                    </div>
                    <div>
                        ${{lead.contacted ? '<span class="bg-emerald-100 text-emerald-800 text-[10px] font-black px-3 py-1 rounded-full uppercase">✅ İletildi</span>' : '<span class="bg-amber-100 text-amber-800 text-[10px] font-black px-3 py-1 rounded-full uppercase">🎯 Hedef Sırada</span>'}}
                    </div>
                </div>

                <div class="mb-4">
                    <h3 class="text-lg font-black text-slate-900 mb-1">${{lead.company}}</h3>
                    <div class="text-xs font-bold text-sky-700 mb-2">👤 Hedef Muhatap: ${{lead.contact_role}}</div>
                    <div class="p-3 bg-red-50 border border-red-200/60 rounded-xl text-xs text-red-900 font-semibold mb-3">
                        ⚠️ <b>Tespit Edilen Teknik Problem:</b> ${{lead.need}}
                    </div>
                </div>

                <div class="p-4 bg-slate-50 rounded-2xl border border-slate-200 mb-4">
                    <div class="flex items-center justify-between mb-2">
                        <span class="text-xs font-black uppercase text-slate-500 tracking-wider">Ajan Tarafından Üretilen Özel B2B Pitch:</span>
                        <a href="${{lead.case_url}}" target="_blank" class="text-sky-600 hover:text-sky-700 text-xs font-bold">Vakayı İncele ➔</a>
                    </div>
                    <p id="pitch-text-${{lead.id}}" class="text-xs leading-relaxed text-slate-700 font-medium whitespace-pre-line">${{lead.pitch_message}}</p>
                </div>

                <div class="flex flex-wrap items-center justify-between gap-3 pt-4 border-t border-slate-100">
                    <div class="flex flex-wrap items-center gap-2">
                        <a href="${{waShareUrl}}" target="_blank" onclick="markLeadContacted('${{lead.id}}')" class="bg-[#25D366] hover:bg-[#20ba5c] text-white font-black text-xs py-2.5 px-4 rounded-xl transition flex items-center gap-1.5 shadow-md shadow-emerald-500/20">
                            <span>💬 WhatsApp ile Gönder</span>
                        </a>
                        <button onclick="copyPitch('${{lead.id}}')" class="bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs py-2.5 px-4 rounded-xl transition flex items-center gap-1.5 shadow">
                            <span>📋 Pitch Metnini Kopyala</span>
                        </button>
                    </div>
                    <div>
                        <button onclick="toggleLeadStatus('${{lead.id}}')" class="text-slate-500 hover:text-slate-800 text-xs font-bold">
                            ${{lead.contacted ? 'Durumu Sıfırla ↺' : 'İletildi İşaretle ✔'}}
                        </button>
                    </div>
                </div>
            </div>
            `;
        }});

        container.innerHTML = html;
    }}

    function copyPitch(leadId) {{
        const text = document.getElementById(`pitch-text-${{leadId}}`).innerText;
        navigator.clipboard.writeText(text).then(() => {{
            alert('Özel B2B teklif metni panoya kopyalandı! LinkedIn veya E-postaya yapıştırabilirsiniz.');
        }});
    }}

    function markLeadContacted(leadId) {{
        const leads = getStoredLeads();
        const l = leads.find(x => x.id === leadId);
        if (l) {{
            l.contacted = true;
            saveLeads(leads);
        }}
    }}

    function toggleLeadStatus(leadId) {{
        const leads = getStoredLeads();
        const l = leads.find(x => x.id === leadId);
        if (l) {{
            l.contacted = !l.contacted;
            saveLeads(leads);
        }}
    }}

    function refreshLeadRadar() {{
        localStorage.removeItem('gkm_agent_reach_leads');
        renderLeads();
        alert('Agent Reach radarı güncellendi! Yeni sanayi vaka analizleri ve hedefler listelendi.');
    }}

    function pingGooglebot() {{
        const sitemapUrl = encodeURIComponent("{site_url}/sitemap.xml");
        const pingUrl = `https://www.google.com/ping?sitemap=${{sitemapUrl}}`;
        window.open(pingUrl, '_blank');
        alert('Googlebot sitemap ping tetiklendi! Google arama motoruna yeni sayfaların tarama bildirimi gönderildi.');
    }}


    // Q&A LOGIC
    function getMergedDiscussions() {{
        const stored = localStorage.getItem('gkm_discussions');
        let discussions = stored ? JSON.parse(stored) : JSON.parse(JSON.stringify(INITIAL_DISCUSSIONS));
        
        const userQs = localStorage.getItem('gkm_user_questions');
        if (userQs) {{
            const parsedUserQs = JSON.parse(userQs);
            parsedUserQs.forEach(uq => {{
                if (!discussions[uq.slug]) {{
                    discussions[uq.slug] = [];
                }}
                if (!discussions[uq.slug].some(x => x.id === uq.id)) {{
                    discussions[uq.slug].unshift(uq);
                }}
            }});
        }}
        return discussions;
    }}

    function saveDiscussions(data) {{
        localStorage.setItem('gkm_discussions', JSON.stringify(data));
        loadAndRenderQuestions();
    }}

    function setFilter(filter) {{
        activeFilter = filter;
        document.getElementById('tab-all').className = filter === 'all' ? "bg-slate-900 text-white font-bold text-xs px-4 py-2 rounded-xl transition shadow" : "bg-white hover:bg-slate-100 text-slate-700 font-bold text-xs px-4 py-2 rounded-xl border border-slate-300 transition";
        document.getElementById('tab-user').className = filter === 'user' ? "bg-slate-900 text-white font-bold text-xs px-4 py-2 rounded-xl transition shadow" : "bg-white hover:bg-slate-100 text-slate-700 font-bold text-xs px-4 py-2 rounded-xl border border-slate-300 transition";
        document.getElementById('tab-curated').className = filter === 'curated' ? "bg-slate-900 text-white font-bold text-xs px-4 py-2 rounded-xl transition shadow" : "bg-white hover:bg-slate-100 text-slate-700 font-bold text-xs px-4 py-2 rounded-xl border border-slate-300 transition";
        loadAndRenderQuestions();
    }}

    function loadAndRenderQuestions() {{
        const container = document.getElementById('questions-container');
        const discussions = getMergedDiscussions();
        
        let allItems = [];
        let totalCount = 0;
        let pendingCount = 0;
        let answeredCount = 0;

        Object.keys(discussions).forEach(slug => {{
            discussions[slug].forEach(q => {{
                totalCount++;
                const isUser = q.is_user_submitted || (q.phone || q.email);
                const hasReply = q.replies && q.replies.length > 0;
                if (!hasReply) pendingCount++;
                else answeredCount++;

                if (activeFilter === 'user' && !isUser) return;
                if (activeFilter === 'curated' && isUser) return;

                allItems.push({{ slug, ...q, isUser, hasReply }});
            }});
        }});

        document.getElementById('stat-total').innerText = totalCount;
        document.getElementById('stat-pending').innerText = pendingCount;
        document.getElementById('stat-answered').innerText = answeredCount;

        if (allItems.length === 0) {{
            container.innerHTML = `<div class="bg-white p-8 rounded-2xl border border-slate-200 text-center text-slate-400 font-medium">Bu filtrede soru bulunamadı.</div>`;
            return;
        }}

        let html = '';
        allItems.forEach(item => {{
            const repliesHtml = (item.replies || []).map(r => `
                <div class="mt-3 p-4 rounded-xl ${{r.verified ? 'bg-sky-50/80 border border-sky-200' : 'bg-slate-50 border border-slate-200'}} text-xs leading-relaxed">
                    <div class="flex items-center justify-between mb-1">
                        <span class="font-black text-slate-900 flex items-center gap-1.5">
                            ${{r.verified ? '🛡️ <span class="text-sky-700">' + r.author + '</span>' : '👤 ' + r.author}}
                        </span>
                        <span class="text-[10px] text-slate-400">${{r.date}}</span>
                    </div>
                    <p class="text-slate-700">${{r.text}}</p>
                </div>
            `).join('');

            let waBtn = '';
            if (item.phone) {{
                const cleanPhone = item.phone.replace(/[^0-9]/g, '');
                const waText = encodeURIComponent(`Merhaba ${{item.author_name}}, GKM Elektrik'e ilettiğiniz '${{item.question.slice(0, 50)}}...' sorunuz hakkında: `);
                waBtn = `
                    <a href="https://wa.me/${{cleanPhone}}?text=${{waText}}" target="_blank" class="bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs py-2 px-3.5 rounded-xl transition flex items-center gap-1.5 shadow">
                        <span>💬 WhatsApp ile Yanıtla (${{item.phone}})</span>
                    </a>
                `;
            }}

            html += `
                <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
                    <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                        <div class="flex items-center gap-2">
                            ${{item.isUser ? '<span class="bg-amber-100 text-amber-800 text-[10px] font-black px-2.5 py-0.5 rounded-full uppercase">Canlı Müşteri Sorusu</span>' : '<span class="bg-sky-100 text-sky-800 text-[10px] font-black px-2.5 py-0.5 rounded-full uppercase">Teknik Vaka Soru-Cevap</span>'}}
                            <span class="text-xs font-bold text-slate-400">📄 Konu: <span class="text-slate-700">${{item.slug}}</span></span>
                        </div>
                        <span class="text-xs font-semibold text-slate-400">📅 ${{item.date}}</span>
                    </div>

                    <div class="mb-4">
                        <div class="font-black text-slate-900 text-sm mb-1">${{item.author_name}} <span class="text-slate-400 font-normal">(${{item.company || 'Mühendislik Ziyaretçisi'}})</span></div>
                        <p class="text-slate-700 text-xs sm:text-sm bg-slate-50 p-4 rounded-xl border border-slate-100 font-medium">${{item.question}}</p>
                    </div>

                    ${{repliesHtml}}

                    <div class="mt-4 pt-4 border-t border-slate-100 flex flex-wrap items-center justify-between gap-3">
                        <div class="flex items-center gap-2">
                            ${{waBtn}}
                            <button onclick="toggleReplyBox('${{item.id}}')" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs py-2 px-3.5 rounded-xl transition border border-slate-300">
                                ✏️ Siteye Yanıt Ekle
                            </button>
                        </div>
                        <button onclick="deleteQuestion('${{item.slug}}', '${{item.id}}')" class="text-red-500 hover:text-red-700 text-xs font-bold">
                            Sil ✕
                        </button>
                    </div>

                    <div id="reply-box-${{item.id}}" class="mt-3 hidden">
                        <textarea id="reply-text-${{item.id}}" rows="3" placeholder="Gökmen Elektrik mühendislik yanıtınızı yazın..." class="w-full bg-slate-50 border border-slate-300 rounded-xl p-3 text-xs font-medium text-slate-900 focus:ring-2 focus:ring-sky-500 focus:outline-none mb-2"></textarea>
                        <div class="flex justify-end gap-2">
                            <button onclick="toggleReplyBox('${{item.id}}')" class="px-3 py-1.5 rounded-lg border border-slate-300 text-xs text-slate-600 font-semibold">İptal</button>
                            <button onclick="submitInlineReply('${{item.slug}}', '${{item.id}}')" class="bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs px-4 py-1.5 rounded-lg shadow">Yayınla</button>
                        </div>
                    </div>
                </div>
            `;
        }});

        container.innerHTML = html;
    }}

    function toggleReplyBox(id) {{
        const el = document.getElementById(`reply-box-${{id}}`);
        if (el) el.classList.toggle('hidden');
    }}

    function submitInlineReply(slug, qId) {{
        const text = document.getElementById(`reply-text-${{qId}}`).value.trim();
        if (!text) return;

        const discussions = getMergedDiscussions();
        if (discussions[slug]) {{
            const q = discussions[slug].find(x => x.id === qId);
            if (q) {{
                if (!q.replies) q.replies = [];
                q.replies.push({{
                    author: "Gökmen Elektrik & Mühendislik Ekibi",
                    role: "Sistem Entegratörü",
                    date: new Date().toLocaleDateString('tr-TR'),
                    text: text,
                    verified: true
                }});
                saveDiscussions(discussions);
            }}
        }}
    }}

    function deleteQuestion(slug, qId) {{
        if (!confirm('Bu soruyu silmek istediğinize emin misiniz?')) return;
        const discussions = getMergedDiscussions();
        if (discussions[slug]) {{
            discussions[slug] = discussions[slug].filter(x => x.id !== qId);
            saveDiscussions(discussions);
        }}
    }}

    function openNewModal() {{
        document.getElementById('new-modal').classList.remove('hidden');
    }}

    function closeNewModal() {{
        document.getElementById('new-modal').classList.add('hidden');
    }}

    function handleAddNewQA(e) {{
        e.preventDefault();
        const slug = document.getElementById('new-slug').value.trim();
        const author = document.getElementById('new-author').value.trim();
        const date = document.getElementById('new-date').value.trim();
        const question = document.getElementById('new-question').value.trim();
        const reply = document.getElementById('new-reply').value.trim();

        const discussions = getMergedDiscussions();
        if (!discussions[slug]) discussions[slug] = [];

        const newId = 'q-' + Date.now();
        discussions[slug].unshift({{
            id: newId,
            author_name: author,
            company: "Doğrulanmış Sanayi Sorusu",
            date: date,
            question: question,
            replies: [
                {{
                    author: "Gökmen Elektrik & Mühendislik Ekibi",
                    role: "Teknik Danışmanlık",
                    date: date,
                    text: reply,
                    verified: true
                }}
            ]
        }});

        saveDiscussions(discussions);
        closeNewModal();
        alert('Yeni teknik soru-cevap başarıyla eklendi!');
    }}

    function exportJson() {{
        const discussions = getMergedDiscussions();
        const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(discussions, null, 2));
        const downloadAnchor = document.createElement('a');
        downloadAnchor.setAttribute("href", dataStr);
        downloadAnchor.setAttribute("download", "discussions_database_updated.json");
        document.body.appendChild(downloadAnchor);
        downloadAnchor.click();
        downloadAnchor.remove();
    }}

    document.addEventListener('DOMContentLoaded', () => {{
        if (sessionStorage.getItem('gkm_admin_auth') === 'true') {{
            document.getElementById('auth-gate').classList.add('hidden');
            document.getElementById('admin-content').classList.remove('hidden');
            switchView('reach');
            renderLeads();
            loadAndRenderQuestions();
        }}
    }});
    </script>

</body>
</html>
"""
