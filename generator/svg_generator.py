"""
Industrial Technical Diagram & Schematic Generator (Vector SVG)
Generates high-tech engineering schematics with dark theme, cyber cyan (#00e5ff),
neon emerald (#10b981), and electric amber (#f59e0b) accents.
"""

def generate_svg_diagram(diagram_type, title):
    if diagram_type == "servo_sync":
        return f"""
        <svg viewBox="0 0 800 360" class="w-full h-auto rounded-2xl bg-slate-950 border border-slate-800 shadow-2xl p-4" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="cyanGrad" x1="0" y1="0" x2="1" y2="0">
              <stop offset="0%" stop-color="#00e5ff" stop-opacity="0.2"/>
              <stop offset="100%" stop-color="#00e5ff" stop-opacity="0.9"/>
            </linearGradient>
            <linearGradient id="amberGrad" x1="0" y1="0" x2="1" y2="0">
              <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.2"/>
              <stop offset="100%" stop-color="#f59e0b" stop-opacity="0.9"/>
            </linearGradient>
          </defs>
          <!-- Grid Lines -->
          <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1e293b" stroke-width="1"/>
          </pattern>
          <rect width="100%" height="100%" fill="url(#grid)" />

          <text x="30" y="40" fill="#94a3b8" font-family="monospace" font-size="12" font-weight="bold">GKM MÜHENDİSLİK // TEKNİK ŞEMA: SERVO ELEKTRONİK KAM (CAMMING) SENKRONİZASYONU</text>

          <!-- Master Axis -->
          <rect x="50" y="80" width="180" height="70" rx="8" fill="#0f172a" stroke="#00e5ff" stroke-width="2"/>
          <text x="140" y="112" fill="#00e5ff" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">MASTER EKSEN</text>
          <text x="140" y="132" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="middle">Ana Çekici / Encoder</text>

          <!-- Arrow -->
          <path d="M 230 115 L 320 115" stroke="#00e5ff" stroke-width="2" marker-end="url(#arrow)" stroke-dasharray="4"/>
          <text x="275" y="105" fill="#38bdf8" font-family="monospace" font-size="10" text-anchor="middle">PROFINET IRT</text>

          <!-- Motion Controller -->
          <rect x="330" y="65" width="200" height="100" rx="10" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
          <text x="430" y="102" fill="#c7d2fe" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">SIEMENS S7-1500T</text>
          <text x="430" y="122" fill="#a5b4fc" font-family="monospace" font-size="11" text-anchor="middle">Motion Control CPU</text>
          <text x="430" y="142" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">Elektronik Kam Tablosu</text>

          <!-- Slave Axes -->
          <path d="M 530 95 L 610 95" stroke="#f59e0b" stroke-width="2"/>
          <rect x="610" y="65" width="160" height="60" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
          <text x="690" y="95" fill="#f59e0b" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">SLAVE 1: BESLEME</text>
          <text x="690" y="113" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="middle">V90 1.5kW Servo</text>

          <path d="M 430 165 L 430 220 L 610 220" stroke="#10b981" stroke-width="2" fill="none"/>
          <rect x="610" y="190" width="160" height="60" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
          <text x="690" y="220" fill="#10b981" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">SLAVE 2: KESİCİ BIÇAK</text>
          <text x="690" y="238" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="middle">Rotary Knife 3.0kW</text>

          <!-- Performance Metric Banner -->
          <rect x="50" y="280" width="720" height="50" rx="8" fill="#090d16" stroke="#334155" stroke-width="1"/>
          <text x="70" y="310" fill="#10b981" font-family="sans-serif" font-size="12" font-weight="bold">✓ KAPASİTE KAZANCI:</text>
          <text x="210" y="310" fill="#f1f5f9" font-family="sans-serif" font-size="12">Mekanik kam yerine interpolasyonlu servo kamlama ile dakikada 80 -> 145 paket kapasitesi.</text>
        </svg>
        """

    elif diagram_type == "pcb_stackup":
        return f"""
        <svg viewBox="0 0 800 360" class="w-full h-auto rounded-2xl bg-slate-950 border border-slate-800 shadow-2xl p-4" xmlns="http://www.w3.org/2000/svg">
          <text x="30" y="35" fill="#94a3b8" font-family="monospace" font-size="12" font-weight="bold">GKM MÜHENDİSLİK // 4-KATMAN ENDÜSTRİYEL PCB STACKUP & İZOLASYON ŞEMASI</text>

          <!-- Layer 1 -->
          <rect x="60" y="60" width="680" height="40" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
          <text x="80" y="85" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="bold">LAYER 1: TOP SIGNAL (High Speed Bus & MCU Traces - 1oz Bakır)</text>
          <text x="650" y="85" fill="#bae6fd" font-family="monospace" font-size="11">35 µm</text>

          <!-- Prepreg -->
          <rect x="60" y="105" width="680" height="25" fill="#334155" stroke="#475569" stroke-width="1"/>
          <text x="400" y="122" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">DIELECTRIC PREPREG (FR4 Core - 0.2mm)</text>

          <!-- Layer 2 -->
          <rect x="60" y="135" width="680" height="40" rx="4" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
          <text x="80" y="160" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="bold">LAYER 2: SOLID GROUND PLANE (GND - 0V EMI Kalkanlama Referansı)</text>
          <text x="650" y="160" fill="#bbf7d0" font-family="monospace" font-size="11">35 µm</text>

          <!-- Core -->
          <rect x="60" y="180" width="680" height="35" fill="#1e293b" stroke="#334155" stroke-width="1"/>
          <text x="400" y="202" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="middle">CORE DIELECTRIC ISOLATION (1.0mm Yüksek Gerilim İzolasyonu)</text>

          <!-- Layer 3 -->
          <rect x="60" y="220" width="680" height="40" rx="4" fill="#b45309" stroke="#f59e0b" stroke-width="2"/>
          <text x="80" y="245" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="bold">LAYER 3: POWER PLANE (+24V, +5V, +3.3V Dağıtım Alanı)</text>
          <text x="650" y="245" fill="#fef08a" font-family="monospace" font-size="11">35 µm</text>

          <!-- Prepreg -->
          <rect x="60" y="265" width="680" height="25" fill="#334155" stroke="#475569" stroke-width="1"/>
          <text x="400" y="282" fill="#cbd5e1" font-family="monospace" font-size="11" text-anchor="middle">DIELECTRIC PREPREG (FR4 - 0.2mm)</text>

          <!-- Layer 4 -->
          <rect x="60" y="295" width="680" height="40" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
          <text x="80" y="320" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="bold">LAYER 4: BOTTOM SIGNAL (Sensör Girişleri & Röle Çıkışları)</text>
          <text x="650" y="320" fill="#bae6fd" font-family="monospace" font-size="11">35 µm</text>
        </svg>
        """

    elif diagram_type == "scada_iot":
        return f"""
        <svg viewBox="0 0 800 360" class="w-full h-auto rounded-2xl bg-slate-950 border border-slate-800 shadow-2xl p-4" xmlns="http://www.w3.org/2000/svg">
          <text x="30" y="35" fill="#94a3b8" font-family="monospace" font-size="12" font-weight="bold">GKM MÜHENDİSLİK // FABRİKA SCADA & ENDÜSTRİYEL IoT HABERLEŞME TOPOLOJİSİ</text>

          <!-- Saha Katmanı -->
          <rect x="40" y="70" width="200" height="240" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1"/>
          <text x="140" y="95" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">SAHA KATMANI</text>
          
          <rect x="55" y="115" width="170" height="45" rx="6" fill="#1e293b" stroke="#00e5ff" stroke-width="1"/>
          <text x="140" y="142" fill="#f8fafc" font-family="sans-serif" font-size="11" text-anchor="middle">Trafo Enerji Analizörleri</text>

          <rect x="55" y="175" width="170" height="45" rx="6" fill="#1e293b" stroke="#00e5ff" stroke-width="1"/>
          <text x="140" y="202" fill="#f8fafc" font-family="sans-serif" font-size="11" text-anchor="middle">Motor Sürücüleri (VFD)</text>

          <rect x="55" y="235" width="170" height="45" rx="6" fill="#1e293b" stroke="#00e5ff" stroke-width="1"/>
          <text x="140" y="262" fill="#f8fafc" font-family="sans-serif" font-size="11" text-anchor="middle">PLC & Üretim Sayaçları</text>

          <!-- Gateway -->
          <path d="M 240 190 L 320 190" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4"/>
          <text x="280" y="180" fill="#f59e0b" font-family="monospace" font-size="10" text-anchor="middle">RS485 / Modbus</text>

          <rect x="320" y="115" width="160" height="150" rx="10" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
          <text x="400" y="150" fill="#c084fc" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">IoT EDGE</text>
          <text x="400" y="170" fill="#c084fc" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">GATEWAY</text>
          <text x="400" y="200" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="middle">GKM Smart Box</text>
          <text x="400" y="225" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">MQTT / OPC-UA</text>

          <!-- Server & Cloud -->
          <path d="M 480 190 L 560 190" stroke="#10b981" stroke-width="3"/>
          <text x="520" y="180" fill="#10b981" font-family="monospace" font-size="10" text-anchor="middle">Ethernet / WiFi</text>

          <rect x="560" y="70" width="200" height="240" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
          <text x="660" y="95" fill="#10b981" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">İZLEME & SCADA</text>

          <rect x="575" y="115" width="170" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
          <text x="660" y="142" fill="#f8fafc" font-family="sans-serif" font-size="11" text-anchor="middle">Merkezi SCADA Ekranı</text>

          <rect x="575" y="175" width="170" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
          <text x="660" y="202" fill="#f8fafc" font-family="sans-serif" font-size="11" text-anchor="middle">Mobil Anlık Alarm / Telegram</text>

          <rect x="575" y="235" width="170" height="45" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
          <text x="660" y="262" fill="#f8fafc" font-family="sans-serif" font-size="11" text-anchor="middle">Reaktif Ceza Erken Uyarı</text>
        </svg>
        """

    elif diagram_type == "detuned_reactor":
        return f"""
        <svg viewBox="0 0 800 360" class="w-full h-auto rounded-2xl bg-slate-950 border border-slate-800 shadow-2xl p-4" xmlns="http://www.w3.org/2000/svg">
          <text x="30" y="35" fill="#94a3b8" font-family="monospace" font-size="12" font-weight="bold">GKM MÜHENDİSLİK // HARMONİK FİLTRELİ (DE-TUNED %7) KOMPANZASYON HÜCRESİ</text>

          <!-- 3-Phase Busbar -->
          <line x1="80" y1="70" x2="720" y2="70" stroke="#ef4444" stroke-width="3"/>
          <text x="735" y="75" fill="#ef4444" font-family="monospace" font-size="11">L1 (R)</text>
          <line x1="80" y1="95" x2="720" y2="95" stroke="#eab308" stroke-width="3"/>
          <text x="735" y="100" fill="#eab308" font-family="monospace" font-size="11">L2 (S)</text>
          <line x1="80" y1="120" x2="720" y2="120" stroke="#3b82f6" stroke-width="3"/>
          <text x="735" y="125" fill="#3b82f6" font-family="monospace" font-size="11">L3 (T)</text>

          <!-- Switching Device -->
          <rect x="180" y="150" width="180" height="60" rx="8" fill="#1e293b" stroke="#00e5ff" stroke-width="2"/>
          <text x="270" y="178" fill="#00e5ff" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">ANAHTARLAMA</text>
          <text x="270" y="196" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="middle">Tristör Modülü / Kontaktör</text>

          <!-- De-Tuned Reactor -->
          <rect x="420" y="150" width="180" height="60" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
          <text x="510" y="178" fill="#f59e0b" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">HARMONİK FİLTRE</text>
          <text x="510" y="196" fill="#fef08a" font-family="monospace" font-size="10" text-anchor="middle">%7 p Faktörü • 189 Hz</text>

          <!-- Capacitor Bank -->
          <rect x="300" y="245" width="200" height="60" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
          <text x="400" y="273" fill="#10b981" font-family="sans-serif" font-size="13" font-weight="bold" text-anchor="middle">AĞIR HİZMET KONDANSATÖR</text>
          <text x="400" y="291" fill="#94a3b8" font-family="monospace" font-size="10" text-anchor="middle">440V - 525V Kuru Tip</text>

          <path d="M 270 210 L 270 275 L 300 275" stroke="#00e5ff" stroke-width="2" fill="none"/>
          <path d="M 510 210 L 510 275 L 500 275" stroke="#f59e0b" stroke-width="2" fill="none"/>

          <text x="400" y="335" fill="#94a3b8" font-family="sans-serif" font-size="11" text-anchor="middle">
            Rezonans Riski Önlenir • Harmonik Akımları Sönümlenir • Kondansatör Ömrü 5 Kat Uzar
          </text>
        </svg>
        """

    else:
        # Default Engineering Architecture
        return f"""
        <svg viewBox="0 0 800 260" class="w-full h-auto rounded-2xl bg-slate-950 border border-slate-800 shadow-2xl p-4" xmlns="http://www.w3.org/2000/svg">
          <text x="30" y="35" fill="#94a3b8" font-family="monospace" font-size="12" font-weight="bold">GKM MÜHENDİSLİK // ENDÜSTRİYEL SİSTEM MİMARİSİ</text>
          <rect x="60" y="70" width="200" height="120" rx="10" fill="#0f172a" stroke="#00e5ff" stroke-width="2"/>
          <text x="160" y="115" fill="#00e5ff" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">ANALİZ & ŞEMA</text>
          <text x="160" y="140" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="middle">EPLAN P8 & Altium</text>

          <path d="M 260 130 L 300 130" stroke="#64748b" stroke-width="3"/>

          <rect x="300" y="70" width="200" height="120" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
          <text x="400" y="115" fill="#f59e0b" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">ÜRETİM & YAZILIM</text>
          <text x="400" y="140" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="middle">PLC, SCL & PCB İmalatı</text>

          <path d="M 500 130 L 540 130" stroke="#64748b" stroke-width="3"/>

          <rect x="540" y="70" width="200" height="120" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="2"/>
          <text x="640" y="115" fill="#10b981" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">TEST & DEVREYE ALMA</text>
          <text x="640" y="140" fill="#94a3b8" font-family="monospace" font-size="11" text-anchor="middle">Saha Kurulumu 7/24</text>

          <text x="400" y="225" fill="#cbd5e1" font-family="sans-serif" font-size="12" text-anchor="middle">
            GKM Elektrik & Mühendislik • Endüstriyel Donanım ve Yazılım Çözümleri
          </text>
        </svg>
        """
