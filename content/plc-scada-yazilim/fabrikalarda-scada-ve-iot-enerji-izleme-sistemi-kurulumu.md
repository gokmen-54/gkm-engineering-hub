---
title: "Fabrikalarda SCADA ve Endüstriyel IoT ile Enerji Takibi: Modbus TCP ve MQTT Entegrasyonu"
summary: "Tesis genelindeki enerji analizörlerinden Modbus RTU/TCP üzerinden veri toplayıp Ignition SCADA veya Node-RED/MQTT sunucusuna aktaran, reaktif ceza ve harmonik anomalilerini anlık bildiren IoT mimarisi."
category: "plc-scada-yazilim"
category_title: "PLC & SCADA Yazılım"
slug: "fabrikalarda-scada-ve-iot-enerji-izleme-sistemi-kurulumu"
date: "2026-11-10"
reading_time: "8 dk okuma"
target_audience: "Fabrika Enerji Yöneticileri, Bakım Şefleri & Tesis Müdürleri"
diagram_type: "scada_iot"
cta_headline: "Fabrikanızda Enerji Kaybı ve Reaktif Ceza Riskini Sıfırlayın"
cta_text: "Tesisinizdeki analizör ve trafo listesini bize iletin; bulut veya lokal sunuculu SCADA enerji izleme altyapısını anahtar teslim projelendirelim."
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

