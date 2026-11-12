"""
Daily Autonomous Content Engine for GKM Elektrik
Selects new technical engineering topics, builds high-intent markdown guides,
and recompiles the entire static multi-page catalog and sitemap.
"""

import os
import json
import random
from datetime import datetime
import engine

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOPICS_FILE = os.path.join(BASE_DIR, "generator", "topics_database.json")
CONTENT_DIR = os.path.join(BASE_DIR, "content")

# Upcoming High-Intent Topics Matrix for Daily Autonomous Publication
UPCOMING_TOPICS = [
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
        "diagram_type": "adp_panel",
        "cta_headline": "Tesisiniz İçin MCC Motor Kontrol Panosu İhtiyacı mı Var?",
        "cta_text": "Motor güç listenizi ve kalkış gereksinimlerinizi gönderin; tip testli ve iklimlendirmeli MCC pano teklifimizi 24 saatte sunalım."
    }
]


def run_daily_generation():
    today = datetime.now().strftime("%Y-%m-%d")
    with open(TOPICS_FILE, "r", encoding="utf-8") as f:
        existing_topics = json.load(f)

    existing_slugs = {t["slug"] for t in existing_topics}

    # Find next candidate
    candidate = None
    for item in UPCOMING_TOPICS:
        if item["slug"] not in existing_slugs:
            candidate = item
            break

    if not candidate:
        print("[AUTO-CONTENT] Tüm sıradaki konular zaten yayınlanmış.")
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

## Mühendislik Analizi ve Saha Standartları

Bu rehber, **GKM Elektrik & Mühendislik** saha deneyimleri ve uluslararası endüstriyel standartlar (IEC, ISO, IPC) referans alınarak sanayi işletmeleri, Ar-Ge departmanları ve makine imalatçıları için hazırlanmıştır.

### Öne Çıkan Teknik Kriterler:
1. **Güvenilirlik ve Standartlara Uyum:** Endüstriyel ortamlarda kesintisiz 7/24 çalışma garantisi.
2. **Hata Teşhis ve Modülerlik:** Sahada hızlı servis ve kolay yedek parça erişimi.
3. **Dokümantasyon:** EPLAN ve CAD şemaları ile tam şeffaflık.

---

## Detaylı Uygulama Adımları

Projenizin teknik gereksinimlerine göre en uygun kompanzasyon, sürücü veya gömülü sistem mimarisi belirlenir, şematik çizimler onaylandıktan sonra prototip ve seri devreye alma süreçleri işletilir.
"""

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"[AUTO-CONTENT] Yeni makale eklendi: {candidate['title']}")

    # Recompile entire site
    engine.compile_site()
    return True


if __name__ == "__main__":
    run_daily_generation()
