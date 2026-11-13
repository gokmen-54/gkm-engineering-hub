"""
GKM Elektrik & Mühendislik - Autonomous Daily Industrial Content Machine
Generates high-intent technical engineering guides, schematics, and updates sitemap.
100% autonomous, zero human intervention required.
"""

import os
import json
import random
from datetime import datetime
import engine

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOPICS_FILE = os.path.join(BASE_DIR, "generator", "topics_database.json")
CONTENT_DIR = os.path.join(BASE_DIR, "content")

# High-Intent Industrial Topics Matrix (Captures Real Factory & Machine Projects)
CURATED_TOPICS = [
    {
        "slug": "iso-13849-1-makine-emniyet-devresi-tasarimi-sil-pl-hesabi",
        "category": "makine-otomasyonu",
        "category_title": "Makine Otomasyonu",
        "title": "ISO 13849-1 Standardına Göre Makine Emniyet Devresi Tasarımı: Performance Level (PLr) ve SIL Hesabı",
        "summary": "Pres, robot hücresi ve ambalaj hatlarında acil stop, ışık bariyeri ve çift kanal emniyet rölesi mimarisi ile SISTEMA üzerinde PL ve SIL doğrulama rehberi.",
        "target_audience": "Makine İmalatçıları & İş Güvenliği Mühendisleri",
        "reading_time": "8 dk okuma",
        "diagram_type": "default",
        "cta_headline": "Makinanızın CE ve Emniyet Uyumluluğu İçin Destek mi Gerekiyor?",
        "cta_text": "GKM Elektrik ISO 13849-1 standartlarına uygun emniyet devresi projelendirmesi ve SISTEMA hesaplamalarını anahtar teslim yapar. Projenizi danışın."
    },
    {
        "slug": "modbus-rtu-ve-modbus-tcp-haberlesme-sorunlari-ve-cozumleri",
        "category": "plc-scada-yazilim",
        "category_title": "PLC & SCADA Yazılım",
        "title": "Endüstriyel Sahalarda Modbus RTU & Modbus TCP Haberleşme Sorunları, Zaman Aşımı (Timeout) ve Çözümleri",
        "summary": "RS-485 hatlarında yansıma (termination resistor), baud rate uyumsuzluğu, GND potansiyel farkları ve PLC Modbus sorgu kuyruk optimizasyonu.",
        "target_audience": "Otomasyon Şefleri & Saha Bakım Mühendisleri",
        "reading_time": "7 dk okuma",
        "diagram_type": "scada_iot",
        "cta_headline": "Haberleşme Kopmaları Üretiminizi mi Durduruyor?",
        "cta_text": "RS-485 veya endüstriyel Ethernet ağınızdaki paket kayıplarını analizörlerimizle yerinde tespit edip çözüyoruz. Bize ulaşın."
    },
    {
        "slug": "altium-designer-ile-yuksek-akim-ve-sicaklik-yonetimi-pcb",
        "category": "pcb-elektronik-tasarim",
        "category_title": "PCB & Elektronik Tasarım",
        "title": "Güç Elektroniği Kartlarında Termal Yönetim: Altium Designer ile Thermal Via ve Yüksek Akım Bakır Yolu Hesabı",
        "summary": "Motor sürücü ve batarya yönetim (BMS) kartlarında 20A+ akım taşıma kapasitesi (IPC-2152), thermal via dikişi ve alüminyum tabanlı PCB (IMS) tasarım kriterleri.",
        "target_audience": "Donanım Tasarımcıları & Güç Elektroniği Mühendisleri",
        "reading_time": "9 dk okuma",
        "diagram_type": "pcb_stackup",
        "cta_headline": "Aşırı Isınan veya Yanan Güç Kartlarınız mı Var?",
        "cta_text": "Gerber dosyalarınızı iletin; termal simülasyon ve bakır kalınlığı optimizasyonu ile kartınızı endüstriyel standartlara getirelim."
    },
    {
        "slug": "mcc-motor-kontrol-panosu-soft-starter-ve-vfd-secim-rehberi",
        "category": "elektrik-panosu-salt",
        "category_title": "Elektrik Panosu & Şalt",
        "title": "MCC Panolarında Sürücü (VFD) vs Soft Starter Seçimi: Ağır Şart Kalkış ve Enerji Verimliliği Karşılaştırması",
        "summary": "Pompa, fan, kırıcı ve konveyör uygulamalarında demeraj akımını sınırlama, şebeke harmonik etkisi ve pano içi havalandırma debisi hesaplama metodolojisi.",
        "target_audience": "Elektrik Bakım Mühendisleri & Tesis Yöneticileri",
        "reading_time": "8 dk okuma",
        "diagram_type": "default",
        "cta_headline": "Tesisiniz İçin MCC Motor Kontrol Panosu İhtiyacı mı Var?",
        "cta_text": "Motor güç listenizi ve kalkış gereksinimlerinizi gönderin; tip testli ve iklimlendirmeli MCC pano teklifimizi 24 saatte sunalım."
    },
    {
        "slug": "plastik-enjeksiyon-makinesi-plc-ve-hidrolik-servo-revizyonu",
        "category": "makine-otomasyonu",
        "category_title": "Makine Otomasyonu",
        "title": "Plastik Enjeksiyon Makinelerinde PLC ve Hidrolik Servo Pompa Revizyonu ile %40 Enerji Tasarrufu",
        "summary": "Eski oransal valfli hidrolik makinelerin servo motor ve sürücü tahrikli kapalı çevrim basınç-debi kontrolüne dönüştürülmesi ve PLC ekran modernizasyonu.",
        "target_audience": "Plastik İmalatçıları & Makine Revizyon Şefleri",
        "reading_time": "9 dk okuma",
        "diagram_type": "servo_sync",
        "cta_headline": "Enjeksiyon Makinelerinizin Elektrik Tüketimini Düşürün",
        "cta_text": "GKM Elektrik anahtar teslim hidrolik servo dönüşüm ve PLC revizyonu ile enerji faturanızı %40 azaltır. Teklif alın."
    },
    {
        "slug": "soguk-hava-deposu-merkezi-plc-ve-scada-sicaklik-takip-otomasyonu",
        "category": "plc-scada-yazilim",
        "category_title": "PLC & SCADA Yazılım",
        "title": "Endüstriyel Soğuk Hava Depolarında Merkezi PLC & SCADA Otomasyonu: Enerji Optimizasyonu ve Defrost Kontrolü",
        "summary": "Kompresör kaskad kontrolü, elektronik genleşme vanası yönetimi, akıllı defrost döngüleri ve bulut tabanlı HACCP sıcaklık kayıt altyapısı.",
        "target_audience": "Gıda Fabrikası Yöneticileri & Soğutma Mühendisleri",
        "reading_time": "8 dk okuma",
        "diagram_type": "scada_iot",
        "cta_headline": "Soğuk Depo Tesisiniz İçin Otomasyon ve SCADA Çözümü",
        "cta_text": "HACCP uyumlu, uzaktan SMS/alarm bildirimli ve enerji tasarruflu soğuk hava otomasyonu için bize danışın."
    },
    {
        "slug": "stm32-ve-can-bus-tabanli-endustriyel-kontrol-karti-tasarimi",
        "category": "pcb-elektronik-tasarim",
        "category_title": "PCB & Elektronik Tasarım",
        "title": "STM32 Mikrodenetleyici ve İzole CAN Bus (CANopen) Tabanlı Endüstriyel Makine Kontrol Kartı Geliştirme",
        "summary": "Otomotiv ve ağır sanayi ortamları için diferansiyel sinyal koruması, TVS diyot seçimi, optoizole alıcı-verici mimarisi ve FreeRTOS firmware kurgusu.",
        "target_audience": "Elektronik Ar-Ge Mühendisleri & Donanım Geliştiriciler",
        "reading_time": "10 dk okuma",
        "diagram_type": "pcb_stackup",
        "cta_headline": "Özel Elektronik Kart ve Gömülü Yazılım Projeniz mi Var?",
        "cta_text": "STM32 mimarisinde şematik, çok katmanlı PCB ve firmware yazılımını endüstriyel kalitede geliştirip teslim ediyoruz."
    },
    {
        "slug": "reaktif-guc-cezasi-nasil-onlenir-hizli-tristorlu-kompanzasyon",
        "category": "elektrik-panosu-salt",
        "category_title": "Elektrik Panosu & Şalt",
        "title": "Fabrikalarda Reaktif Güç Cezasını Sıfırlama Yöntemi: Hızlı Tristörlü Kompanzasyon ve Rezonans Koruması",
        "summary": "Punta kaynağı, vinç ve asansör gibi dinamik yüklerde klasik kontaktörlerin yetersizliği; sıfır geçişli tristör anahtarlama ve indüktif/kapasitif ceza önleme rehberi.",
        "target_audience": "Tesis Müdürleri & Enerji Yöneticileri",
        "reading_time": "7 dk okuma",
        "diagram_type": "detuned_reactor",
        "cta_headline": "Faturanıza Yansıyan Reaktif Ceza Bedelini Sıfırlayın",
        "cta_text": "Tesisinizde harmonik ve güç analizi yapıp, ceza garantili tristörlü kompanzasyon panosu projelendiriyoruz."
    },
    {
        "slug": "beckhoff-twincat-3-ile-ethercat-cok-eksenli-hareket-kontrolu",
        "category": "plc-scada-yazilim",
        "category_title": "PLC & SCADA Yazılım",
        "title": "Beckhoff TwinCAT 3 & EtherCAT ile Çok Eksenli Yüksek Hızlı Hareket Kontrolü (NC/CNC ve Robotik)",
        "summary": "1 ms altı çevrim süresi, distributed clock (DC) senkronizasyonu, PLCopen Motion Control blokları ve kartezyen robot kinematik yazılımı.",
        "target_audience": "Makine Tasarımcıları & Hareket Kontrol Mühendisleri",
        "reading_time": "9 dk okuma",
        "diagram_type": "servo_sync",
        "cta_headline": "Makinanızda Mikrosaniye Düzeyinde Hassasiyet İstiyor Musunuz?",
        "cta_text": "GKM Elektrik Beckhoff TwinCAT ve EtherCAT servo sistemlerinde uzman yazılım ve devreye alma desteği sağlar."
    },
    {
        "slug": "iec-61439-form-4b-cekmeceli-mcc-panosu-tasarim-standartlari",
        "category": "elektrik-panosu-salt",
        "category_title": "Elektrik Panosu & Şalt",
        "title": "IEC 61439-2 Form 4b Standardında Çekmeceli MCC Panosu Tasarım ve İmalat Kriterleri",
        "summary": "Kesintisiz üretim yapan çimento, cam ve kimya tesislerinde enerjiyi kesmeden çekmece modülü değiştirme, dahili ark koruması ve bara boyutlandırma.",
        "target_audience": "Elektrik Proje Mühendisleri & Ağır Sanayi Tesis Şefleri",
        "reading_time": "8 dk okuma",
        "diagram_type": "default",
        "cta_headline": "Tip Testli Çekmeceli Pano İmalatında Çözüm Ortağınız",
        "cta_text": "Uluslararası tip testli pano karkaslarımız ve orijinal şalt ekipmanlarımızla projenizi anahtar teslim üretiyoruz."
    }
]


# Algorithmic Procedural Generator for Infinite Content
INDUSTRIES = [
    ("Ambalaj ve Paketleme Hatlarında", "paketleme", "makine-otomasyonu", "Makine Otomasyonu", "servo_sync"),
    ("Gıda ve İçecek Üretim Tesislerinde", "gida", "plc-scada-yazilim", "PLC & SCADA Yazılım", "scada_iot"),
    ("Plastik ve Kauçuk Enjeksiyon Preslerinde", "plastik", "makine-otomasyonu", "Makine Otomasyonu", "servo_sync"),
    ("Ağır Sanayi ve Metal Şekillendirme Fabrikalarında", "metal", "elektrik-panosu-salt", "Elektrik Panosu & Şalt", "detuned_reactor"),
    ("Kimya ve Proses Tesislerinde", "kimya", "plc-scada-yazilim", "PLC & SCADA Yazılım", "scada_iot"),
    ("Otomotiv Yan Sanayi Üretim Hatlarında", "otomotiv", "pcb-elektronik-tasarim", "PCB & Elektronik Tasarım", "pcb_stackup"),
    ("Lojistik ve Konveyör Sıralama Merkezlerinde", "konveyor", "makine-otomasyonu", "Makine Otomasyonu", "servo_sync")
]

TECH_TOPICS = [
    ("Hassas Servo Senkronizasyonu ve Elektronik Kam (Camming) Revizyonu", "servo-kam-revizyonu"),
    ("Siemens S7-1500 ve WinCC Unified ile Merkezi SCADA Entegrasyonu", "siemens-scada-entegrasyonu"),
    ("Endüstriyel Ortamlar İçin 4-Katmanlı EMC Korumalı Kontrol Kartı Geliştirme", "emc-kontrol-karti"),
    ("189 Hz %7 De-Tuned Reaktörlü Harmonik Kompanzasyon Panosu İmalatı", "harmonik-kompanzasyon-panosu"),
    ("Modbus TCP ve Profinet Üzerinden Gerçek Zamanlı Veri Toplama ve IoT İzleme", "iot-veri-toplama"),
    ("IEC 61439 Tip Testli Ana Dağıtım (ADP) ve MCC Pano Projelendirmesi", "adp-mcc-pano-projesi"),
    ("STM32 Tabanlı Optoizole Sayısal ve Analog I/O Modül Tasarımı", "optoizole-io-modul")
]


def generate_algorithmic_topic():
    ind_name, ind_slug, cat_key, cat_title, diag = random.choice(INDUSTRIES)
    tech_title, tech_slug = random.choice(TECH_TOPICS)

    slug = f"{ind_slug}-{tech_slug}-{random.randint(10, 99)}"
    title = f"{ind_name} {tech_title}"
    summary = f"{ind_name} üretim verimliliğini artıran, duruş sürelerini sıfıra indiren ve uluslararası endüstriyel normlara uygun teknik mühendislik ve otomasyon çözümleri."

    return {
        "slug": slug,
        "category": cat_key,
        "category_title": cat_title,
        "title": title,
        "summary": summary,
        "target_audience": "Tesis Müdürleri, Fabrika Bakım Şefleri ve Makine İmalatçıları",
        "reading_time": "8 dk okuma",
        "diagram_type": diag,
        "cta_headline": f"{ind_name} Otomasyon veya Pano Projeniz mi Var?",
        "cta_text": "GKM Elektrik uzman mühendis kadrosuyla projenizin elektrik şeması, pano imalatı ve yazılım devreye alma süreçlerini anahtar teslim üstlenir. WhatsApp'tan danışın."
    }


def get_next_topic(existing_slugs):
    # 1. First check curated list
    for item in CURATED_TOPICS:
        if item["slug"] not in existing_slugs:
            return item

    # 2. If curated exhausted, generate algorithmically (infinite topics)
    for _ in range(50):
        cand = generate_algorithmic_topic()
        if cand["slug"] not in existing_slugs:
            return cand

    return None


def run_daily_generation():
    today = datetime.now().strftime("%Y-%m-%d")
    with open(TOPICS_FILE, "r", encoding="utf-8") as f:
        existing_topics = json.load(f)

    existing_slugs = {t["slug"] for t in existing_topics}
    candidate = get_next_topic(existing_slugs)

    if not candidate:
        print("[AUTO-CONTENT] Konu secilemedi.")
        return False

    candidate["date"] = today
    existing_topics.append(candidate)

    # Save topics database
    with open(TOPICS_FILE, "w", encoding="utf-8") as f:
        json.dump(existing_topics, f, indent=2, ensure_ascii=False)

    # Build markdown file
    cat_dir = os.path.join(CONTENT_DIR, candidate["category"])
    os.makedirs(cat_dir, exist_ok=True)
    file_path = os.path.join(cat_dir, f"{candidate['slug']}.md")

    md_content = f"""---
title: "{candidate['title']}"
summary: "{candidate['summary']}"
category: "{candidate['category']}"
category_title: "{candidate['category_title']}"
slug: "{candidate['slug']}"
date: "{candidate['date']}"
reading_time: "{candidate['reading_time']}"
target_audience: "{candidate['target_audience']}"
diagram_type: "{candidate['diagram_type']}"
cta_headline: "{candidate['cta_headline']}"
cta_text: "{candidate['cta_text']}"
---

## Endüstriyel Saha Standartları ve Mühendislik Yaklaşımı

Bu teknik rehber, **GKM Elektrik & Mühendislik** saha tecrübeleri, Türk sanayisindeki fiili fabrika uygulamaları ve uluslararası mühendislik standartları (IEC 61439, ISO 13849, IPC-A-610) doğrultusunda hazırlanmıştır.

Sanayi tesislerinde yaşanan plansız üretim duruşları, yüksek reaktif enerji faturaları ve makine yazılım kararsızlıkları doğru mühendislik analizi ve kaliteli şalt/otomasyon komponentleri ile tamamen önlenebilir.

---

### Temel Tasarım ve Uygulama Kriterleri:

1. **Uluslararası Standartlara Tam Uyum:**
   Panolarda IEC 61439 tip testli hücre yapısı, klemenslerde yay baskılı titreşime dayanıklı bağlantılar, yazılımda ise IEC 61131-3 SCL programlama disiplini.

2. **Termal ve Elektromanyetik Uyumluluk (EMC/EMI):**
   Servo sürücü ve motor kablolarında 360 derece zırh topraklaması, kontrol sinyalleri ile güç kabloları arasında minimum 20 cm ayırma mesafesi ve pano içi zorlamalı fanlı/klimalı havalandırma.

3. **Gözlemlenebilirlik ve Hızlı Arıza Teşhisi:**
   SCADA ve operatör panellerinde (HMI) operatörü doğrudan arızalı sensör ve sigortaya yönlendiren Türkçe alarm ağacı ve olay günlüğü (event logger).

---

### GKM Elektrik İle Projelendirme Süreci:

- **1. Saha ve Keşif Analizi:** Tesisinizde veya makinenizde motor güçleri, I/O listesi ve haberleşme gereksinimleri yerinde tespit edilir.
- **2. EPLAN Projelendirme & Şematik Çizim:** Tüm pano ve kablaj şemaları uluslararası normlarda çizilerek onayınıza sunulur.
- **3. Atölye İmalatı & Fabrika Kabul Testi (FAT):** Tip testli karkaslarda montajı tamamlanan panolar gerilim ve fonksiyon testlerinden geçirilir.
- **4. Saha Devreye Alma (SAT) & 7/24 Teknik Destek:** Uzman otomasyon ekibimiz hattı sahada devreye alır ve operatör eğitimlerini tamamlar.

> **Mühendislik Tavsiyesi:** Projelerinizde revizyon maliyetlerini düşürmek için mutlaka gerber, EPLAN veya tek hat şemanızı önceden mühendislerimize inceletiniz.
"""

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"[AUTO-CONTENT] Yeni teknik rehber olusturuldu: {candidate['title']}")

    # Also automatically append a realistic engineering Q&A thread for the new topic
    disc_file = os.path.join(BASE_DIR, "generator", "discussions_database.json")
    try:
        with open(disc_file, "r", encoding="utf-8") as df:
            discussions = json.load(df)
    except Exception:
        discussions = {}

    if candidate["slug"] not in discussions:
        discussions[candidate["slug"]] = [
            {
                "id": f"q-auto-{candidate['slug'][:15]}",
                "author_name": "Serkan Aydın",
                "company": "Tesis Bakım Mühendisi (Kocaeli OSB)",
                "date": today,
                "question": f"{candidate['title']} konusunda benzer bir sahada uygulama yaparken nelere en çok dikkat etmeliyiz?",
                "replies": [
                    {
                        "author": "Gökmen Elektrik & Mühendislik Ekibi",
                        "role": "Sistem Entegratörü",
                        "date": today,
                        "text": f"Serkan Bey merhaba. Bu uygulamada en kritik husus; uluslararası normlara (IEC/ISO) uygun koruma ve parazit izolasyonudur. Tesisinizin şemasını veya teknik şartnamenizi bize WhatsApp üzerinden iletirseniz, projenizi ücretsiz inceleyip en uygun komponent seçimini yapabiliriz.",
                        "verified": True
                    }
                ]
            }
        ]
        with open(disc_file, "w", encoding="utf-8") as df:
            json.dump(discussions, df, indent=2, ensure_ascii=False)

    # Recompile entire site and update sitemap
    engine.compile_site()
    return True


if __name__ == "__main__":
    run_daily_generation()
