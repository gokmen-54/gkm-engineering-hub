---
title: "OTS Soğuk Hava Deposu Otomasyonu: Çoklu Oda Sıcaklık/Nem SCADA & WhatsApp Alarm Takip Sistemi"
summary: "Gıda muhafaza, donuk depo ve yaş meyve/sebze tesislerinde HACCP uyumlu 8+ oda sıcaklık, nem, O2/CO2 gaz izleme, dış ortam IP65 HMI ve 4G LTE WhatsApp acil durum bildirim mimarisi."
category: "plc-scada-yazilim"
category_title: "PLC & SCADA Yazılım"
slug: "soguk-hava-deposu-scada-ve-uzaktan-sicaklik-takip-sistemi-ots"
date: "2026-11-14"
reading_time: "7 dk okuma"
target_audience: "Gıda Fabrika Müdürleri, Soğuk Depo İşletmecileri & Bakım Şefleri"
diagram_type: "scada_flow"
cta_headline: "Soğuk Deponuzda Ürün Bozulma Riskine Son Verin"
cta_text: "Gökmen Elektrik OTS (Otomatik Takip Sistemi) ile tesisinizi 7/24 telefonunuzdan izleyin; sıcaklık yükseldiğinde WhatsApp alarmı anında cebinize gelsin. Tesisiniz için ücretsiz keşif isteyin."
---


## Fabrikalarda Enerji Maliyetleri ve Dijitalleşme İhtiyacı

Sanayi tesislerinde elektrik faturalarının en büyük kalemini motorlar, kompresörler, fırınlar ve soğutma grupları oluşturur. Tesislerde yaşanan görünmeyen enerji kayıpları, hatalı reaktif güç kompanzasyonu ve tepe güç (demant) aşımları yüz binlerce liralık ek cezalara yol açmaktadır.

**GKM Elektrik Endüstriyel IoT ve SCADA çözümleri**, tesisteki tüm trafoları, ana panoları, dağıtım hatlarını ve makineleri tek ekranda toplayarak enerji verimliliğini gerçek zamanlı olarak yönetilebilir hale getirir.

---

## Modbus TCP ve MQTT ile Uçtan Uca Veri Mimarisi

Modern bir endüstriyel veri toplama mimarisinde şu katmanlar bulunur:

1. **Saha Seviyesi (Field Level):**
   - Ray tipi enerji analizörleri (Akım, Gerilim, Cos φ, THD-I, THD-V, Aktif/Reaktif Güç)
   - RS-485 2 telli Twisted Pair kablolama üzerinden Modbus RTU protokolü (9600-115200 baud).

2. **Kenar Ağ Geçidi (Edge Gateway - GKM Smart Box):**
   - Modbus RTU verilerini toplayıp yerel ağda Modbus TCP veya hafif JSON formatında MQTT protokolüne çeviren endüstriyel gateway.
   - İnternet kesintilerine karşı yerel SQLite hafızasında 30 güne kadar veri saklama (Store and Forward).

3. **Merkezi SCADA ve Bulut İzleme:**
   - Ignition SCADA, Siemens WinCC veya lokal Node-RED panelleri.
   - Otomatik SMS ve Telegram botu: Reaktif oran (endüktif %20, kapasitif %15 sınırlarına yaklaştığında) anında bakım şefine alarm iletilir.

---

## Yatırımın Geri Dönüşü (ROI)

Tesis genelinde devreye aldığımız SCADA ve enerji takip sistemleri ortalama **3 ila 6 ay** içerisinde kendini amorti etmektedir:
- Reaktif ceza riskinin %100 ortadan kalkması,
- Mesai dışı boşta çalışan kompresör ve hatların anında tespiti,
- Trafo harmonik yüklenmelerinin izlenerek trafo ömrünün korunması.

