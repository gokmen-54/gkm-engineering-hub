"""
Content Builder & Generator for GKM Elektrik Engineering Hub
Generates in-depth, authoritative, high-ranking programmatic technical articles.
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOPICS_FILE = os.path.join(BASE_DIR, "generator", "topics_database.json")
CONTENT_DIR = os.path.join(BASE_DIR, "content")


def generate_article_body(topic):
    slug = topic["slug"]
    title = topic["title"]
    category = topic["category"]
    
    if "servo" in slug or "paketleme" in slug:
        return f"""
## Giriş: Mekanik Kam Sistemlerinin Sınırları ve Servo Dönüşümü

Geleneksel ambalaj, dikey/yatay dolum (VFFS/HFFS) ve termoform makinelerinde hareket kontrolü uzun yıllar boyunca mekanik kam milleri ve dişli kutuları ile sağlanmıştır. Ancak farklı paket boylarına geçişte yaşanan mekanik ayar süreleri (downtime), mekanik aşınmalar ve hız limitleri günümüz esnek üretim bantlarında ciddi bir verimsizlik yaratmaktadır.

**GKM Elektrik & Mühendislik** olarak gerçekleştirdiğimiz hat revizyonlarında, mekanik kam milleri yerine **Elektronik Kam (Electronic Camming)** ve **Sanal Master (Virtual Master)** mimarisine geçiş yaparak dakikadaki paket sayısını (PPM) %40 ila %65 oranında artırıyoruz.

---

## Elektronik Kam (Camming) Mimarisi Nasıl Çalışır?

Siemens S7-1500T (Technology CPU) veya Beckhoff TwinCAT NC Motion denetleyicileri üzerinde tanımlanan kam tabloları (5. dereceden polinom veya Spline eğrileri), master eksenin (örneğin film çekici rulo veya ana konveyör) enkoder pozisyonunu referans alır.

```scl
// Siemens TIA Portal SCL Örneği: Kam Senkronizasyon Bloğu
FUNCTION_BLOCK "GKM_CamSync_Control"
VAR_INPUT
    EnableSync : BOOL;
    MasterAxis : DB_ANY;
    SlaveAxis  : DB_ANY;
    CamProfile : DB_ANY;
END_VAR
VAR_OUTPUT
    InSync : BOOL;
    Busy   : BOOL;
    Error  : BOOL;
END_VAR
BEGIN
    IF EnableSync THEN
        MC_CamIn(Master := MasterAxis,
                 Slave  := SlaveAxis,
                 Cam    := CamProfile,
                 Execute := TRUE);
        InSync := SlaveAxis.StatusBits.Synchronized;
    END_IF;
END_FUNCTION_BLOCK
```

### Temel Mühendislik Kriterleri:
1. **Jerk (Sarsıntı) Sınırlaması:** Yüksek hızlarda ani ivmelenme değişimleri film yırtılmalarına ve mekanik titreşime yol açar. S-rampa (S-Curve) jerk filtreleme zorunludur.
2. **Kayıpsız Renk Fotoseli Düzeltmesi (Mark Registration):** Baskılı ambalaj filmlerinde baskı kaymalarını önlemek için yüksek hızlı dijital giriş (Fast Input - sub-millisecond) ile film pozisyonu anlık kompanze edilir.
3. **Emniyet (Safety Integrated - ISO 13849-1):** Acil stop ve kapı açılma durumlarında STO (Safe Torque Off) ve SLS (Safely-Limited Speed) devreye girmelidir.

---

## Proje Adımları ve Saha Devreye Alma

1. **Mekanik & Atalet (Inertia) Analizi:** Motor miline yansıyan atalet oranının (J_load / J_motor) 5:1 seviyesinin altında tutulması sağlanır.
2. **EPLAN P8 Pano Projelendirmesi:** Siemens S120 / V90 sürücü güç dağıtımı, hat filtreleri ve frenleme dirençleri standartlara uygun boyutlandırılır.
3. **Saha Entegrasyonu ve Test:** PLC, HMI ve servo haberleşmesi PROFINET IRT (Isochronous Real-Time) protokolü ile 1 ms altında çevrim zamanında test edilir.
"""

    elif "pcb" in slug or "4-katman" in slug:
        return f"""
## Endüstriyel PCB Tasarımında Gürültü ve EMC/EMI Gerçeği

Tüketici elektroniğinin aksine, fabrika sahalarında çalışan elektronik kontrol kartları ağır şartlar altındadır:
- Yüksek frekanslı PWM gürültüsü yayan AC motor sürücüleri (Inverter/VFD),
- Şebeke kaynaklı transients (EFT/Burst testleri - IEC 61000-4-4),
- İndüktif yüklerin (kontaktör ve selenoid valf bobinleri) açılıp kapanmasıyla oluşan arklar,
- Statik elektrik boşalmaları (ESD - IEC 61000-4-2).

Bu ortamda kararlı çalışan bir elektronik kart üretmek için **şematik tasarım kadar PCB katman yapısı (Layer Stackup) ve Ground Plane stratejisi** hayati önem taşır.

---

## 4 Katmanlı Endüstriyel Stackup Konfigürasyonu (SIG - GND - PWR - SIG)

En yüksek elektromanyetik uyumluluk için standart 4 katmanlı endüstriyel stackup şu şekilde düzenlenir:

| Katman | Tip | Fonksiyon ve Tasarım Kriteri | Bakır Kalınlığı |
|---|---|---|---|
| **Layer 1 (Top)** | Sinyal (SIG) | MCU, kristal, sensör ve haberleşme yolları | 35 µm (1 oz) |
| **Layer 2 (Inner 1)** | Solid Ground (GND) | Kesintisiz 0V referans düzlemi, EMI kalkanı | 35 µm (1 oz) |
| **Layer 3 (Inner 2)** | Güç (PWR) | +24V, +5V, +3.3V ada/poligon dağıtımı | 35 µm (1 oz) |
| **Layer 4 (Bottom)** | Sinyal (SIG) | Güç elemanları, filtreler ve konnektör hatları | 35 µm (1 oz) |

### Neden Kesintisiz Solid GND Plane?
Yüksek frekanslı sinyallerin geri dönüş akımı (Return Path), en düşük direnç yolunu değil, **en düşük endüktans yolunu** (doğrudan sinyal yolunun altındaki GND yüzeyini) takip eder. Eğer Ground Plane yarıklarla bölünürse, geri dönüş akımı döngü (loop area) oluşturur ve PCB dev bir anten gibi hem EMI yayar hem de dış gürültüyü toplar.

---

## Giriş/Çıkış (I/O) Koruması ve İzolasyon

1. **Galvanik İzolasyon:** 24V fabrika saha sinyalleri ile hassas 3.3V mikrodenetleyici (MCU) çekirdeği arasında optokuplörler (örn: PC817, TLP291) veya dijital izolatörler (örn: ISO7741) kullanılır.
2. **TVS Diyot ve Ferrit Boncuk:** RS-485 veya CAN Bus haberleşme hatlarında SM712 veya benzeri çift yönlü TVS diyotlar kullanılır.
3. **Ayrık Toprak Mimarisi:** Şase/Kutu toprağı (EARTH) ile dijital devre toprağı (GND), 1nF 2kV yüksek gerilim kondansatörü ve paralel 1MΩ direnç üzerinden bağlanarak ESD enerjisi güvenle tahliye edilir.
"""

    elif "scada" in slug or "iot" in slug:
        return f"""
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
"""

    elif "harmonik" in slug or "kompanzasyon" in slug:
        return f"""
## Reaktif Güç ve Harmonik Rezonansın Tehlikeleri

Modern fabrikalarda inverterler (VFD motor sürücüleri), indüksiyon ocakları, UPS kesintisiz güç kaynakları ve LED aydınlatmalar gibi non-lineer yükler şebekeden saf sinüs şeklinde akım çekmez. Bu durum şebekede **3., 5., 7., 11. ve 13. harmonik akımlarının** oluşmasına sebep olur.

Klasik (filtresiz) kompanzasyon panolarında kullanılan kondansatörler, şebeke trafosunun endüktansı ile belirli bir harmonik frekansında (çoğunlukla 5. harmonik olan 250 Hz civarında) **paralel rezonansa** girer. Rezonans anında:
- Gerilim dalgası aşırı bozulur,
- Kondansatörler aşırı ısınır, şişer veya patlar,
- Elektronik kartlar, PLC'ler ve sensörler arızalanır,
- Faturada yüksek endüktif/kapasitif cezalar yazılır.

---

## De-Tuned (Harmonik Filtreli) Kompanzasyon Çözümü

GKM Elektrik olarak ürettiğimiz kompanzasyon panolarında, her kondansatör kademesinin önüne seri olarak **De-Tuned Harmonik Filtre Reaktörü** yerleştirilir.

### Neden %7 (189 Hz) Reaktör?
- Şebeke temel frekansı: 50 Hz.
- Şebekede en tehlikeli harmonik: 5. harmonik (250 Hz).
- Rezonans frekansı: fr = 50 / sqrt(p) = 50 / sqrt(0.07) ≈ 189 Hz.

Rezonans frekansı (189 Hz), sistemdeki hiçbir harmonik frekansıyla (150 Hz, 250 Hz, 350 Hz) çakışmadığı için sistem rezonansa giremez. 189 Hz'in üzerindeki tüm frekanslarda sistem **endüktif** davrandığından, kondansatörler harmonik akımlarından korunur.

---

## Tristörlü (Hızlı) Kompanzasyon Ne Zaman Gereklidir?

Punta kaynak makineleri, presler, asansörler ve vinçler gibi yüklerin saniyeler içinde devreye girip çıktığı dinamik tesislerde mekanik kontaktörler yetersiz kalır (kontaktör çekme süresi 100-200 ms, deşarj süresi ise dakikalar alır).

**Tristörlü dinamik kompanzasyon panolarımız:**
- Sıfır geçişli (Zero-Crossing) anahtarlama yapar.
- Şebekeye ark ve darbe bindirmeden **20 milisaniye (1 periyot)** içinde devreye girip çıkar.
- Sonsuz anahtarlama ömrü sunar ve reaktif cezayı kesin olarak sıfırlar.
"""

    elif "kumas" in slug or "kesim" in slug:
        return f"""
## Giriş: Kumaş Kontrol ve Boy Kesim Hatlarında Manuel Hataların Önlenmesi

Tekstil, dokuma ve ambalaj hatlarında kumaş sarım, metraj ölçümü ve tartım işlemleri geleneksel olarak operatörün manuel kayıtlarına dayanır. Bu durum kumaş topu boylarında (metre), ağırlıkta (kg) ve parti numarası etiketlerinde hatalara, sevkiyat karışıklıklarına yol açar.

**Gökmen Elektrik & Mühendislik**, **İkizler Tekstil** ve benzeri endüstriyel tesislerde uyguladığı entegre otomasyon mimarisi ile metraj ölçümünü, dijital terazi tartımını ve barkod etiket basımını tek bir PLC ve dokunmatik HMI panelinde tam otonom hale getirmiştir.

---

## Sistem Mimarisi ve Entegre Donanım Katmanı

1. **Optik Enkoder ile ±1 mm Hassasiyetle Metraj Ölçümü:** Çekici merdane üzerine monte edilen yüksek çözünürlüklü optik enkoder, PLC'nin Hızlı Sayıcı (HSC) modülüne bağlanır. Kumaş esneme ve kayma payı HMI ekranındaki 'Kalibrasyon' menüsünden kalibre edilir.
2. **HANA Digital Scale HS-80 Terazi Entegrasyonu:** Sarım bitip rulo kesildiğinde operatör topu terazinin üzerine bırakır. HANA HS-80 terazi indikatörü RS-232 portundan ASCII formatında net ağırlık verisini (örneğin 18.800 kg) PLC'ye iletir.
3. **Otomatik Gramaj Hesabı ve Argox Barkod Basımı:** PLC, kumaşın eni (160 cm), sarılan metraj (116.27 mt) ve tartılan net kiloyu (18.800 kg) formüle ederek kumaşın gramajını (180 gr/m²) otomatik hesaplar.
4. **Argox Termal Barkod Yazıcı Sürücüsü:** Hesaplanan tüm veriler (Firma: İKİZLER, Mal Cinsi: Vualbant, Parti No: 6035, Renk: Somon, Metre: 116.27 mt, Kilo: 18.800 kg) Argox yazıcıya PPLB komut dizisi olarak yollanır ve saniyeler içinde barkodlu rulo kupon etiketi basılır.

---

## Gökmen Elektrik Özel Dokunmatik HMI Arayüzü

- **Otomatik Kesim Menüsü:** Kesim boyu (500 mm), hedef adet (6) ve kesilen adet anlık takip edilir. Enkoder puls/mm kalibrasyonu ile sıfır fire elde edilir.
- **Manuel Jog & Bıçak Emniyeti:** Bıçak yönü, sol siviç ve sağ siviç limitleri arasında kontrol edilir. Bıçak inerken kumaş çekiş motoru kilitlenerek iş güvenliği sağlanır.

---

## Saha Sonuçları ve Başarı Kriterleri

- **Operatör Hataları Sıfırlandı:** Yanlış parti veya yanlış metre etiketi basılması imkansız hale geldi.
- **İşlem Süresi %70 Kısaldı:** Manuel tartım ve ofis bilgisayarından etiket yazma süresi ortadan kalktı.
- **ERP Uyumluluğu:** Basılan EAN-13 barkodlar fabrika ambar sistemine anında entegre oldu.
"""

    elif "soguk-hava" in slug or "ots" in slug:
        return f"""
## Giriş: Soğuk Hava Depolarında 7/24 Kesintisiz Takip ve HACCP Standartları

Gıda saklama, donuk muhafaza ve yaş meyve/sebze depolarında kompresör arızası veya kapının açık kalması nedeniyle sıcaklığın yükselmesi saatler içinde yüz binlerce liralık ürün bozulmasına neden olur.

**Gökmen Elektrik & Mühendislik** tarafından geliştirilen **OTS (Otomatik Takip Sistemi)**, **Özşekerci Gıda** başta olmak üzere çok sayıda endüstriyel soğuk hava tesisinde 8+ bağımsız odanın sıcaklık, nem ve gaz değerlerini merkezi SCADA ve cep telefonu üzerinden izlemektedir.

---

## OTS Sisteminin 4 Temel Mühendislik Bileşeni

1. **4 Telli PT100 & Nem/Gaz Transmitterleri:** Tesis genelindeki 8 odada ±0.1°C hassasiyetle sıcaklık ve %1 rH hassasiyetle nem ölçülür.
2. **Dış Ortam IP65 Renkli Dokunmatik HMI:** Saha şartlarına, yıkamaya ve neme dayanıklı IP65 korumalı operatör paneli depo girişine monte edilir.
3. **Merkezi Windows SCADA & Bulut Kayıt:** Tüm odaların verileri 5 dakikada bir veri tabanına arşivlenir. HACCP denetimlerinde tek tuşla geçmiş sıcaklık grafikleri raporlanır.
4. **4G LTE WhatsApp & SMS Acil Durum Alarmı:** Sıcaklık kritik eşiği (+4°C) aştığında veya kompresör arızaya geçtiğinde sistem tanımlı 5 personele WhatsApp ve SMS mesajı gönderir. Tesisin elektriği veya interneti kesilse bile pano içindeki 24V UPS ve 4G modem sayesinde alarm aksamadan iletilir.

---

## Kaskad Kompresör Eş Yaşlanma ve Elektrik Tasarrufu

- Kompresörlerin çalışma saatleri PLC tarafından sayılarak eşit yıpranma sağlanır.
- Gece ucuz elektrik tarifesinde derin soğutma yapılarak gündüz pik saatlerde kompresör yükü azaltılır ve **%20 ila %28 elektrik tasarrufu** elde edilir.
"""

    else:
        return f"""
## Endüstriyel Mühendislik ve Uygulama Kriterleri

Fabrika ve makine sahalarında uygulanan elektrik ve otomasyon projelerinde standartlara tam uyum, işletme güvenliği ve kesintisiz çalışma esastır. 

**GKM Elektrik & Mühendislik**, Sakarya, Kocaeli ve Marmara Bölgesi başta olmak üzere Türkiye genelinde endüstriyel tesisler, makine imalatçıları ve teknoloji firmaları için anahtar teslim projeler üretmektedir.

---

## Temel Mühendislik Standartlarımız

1. **Elektriksel Güvenlik ve Tip Testi (IEC 61439-1/2):** Panolarımızda kısa devre dayanımı, sıcaklık artış hesapları ve dielektrik izolasyon testleri eksiksiz uygulanır.
2. **Endüstriyel Yazılım Güvenilirliği (IEC 61131-3):** PLC ve SCADA yazılımlarımız temiz kod mimarisi, hata yakalama rutinleri ve kapsamlı alarm hiyerarşisi ile teslim edilir.
3. **Dokümantasyon ve EPLAN:** Her projenin EPLAN P8 elektrik projeleri, klemens planları ve malzeme listeleri müşteriye eksiksiz devredilir.
"""


def build_markdown_files():
    with open(TOPICS_FILE, "r", encoding="utf-8") as f:
        topics = json.load(f)

    for t in topics:
        cat = t["category"]
        slug = t["slug"]
        cat_dir = os.path.join(CONTENT_DIR, cat)
        os.makedirs(cat_dir, exist_ok=True)
        file_path = os.path.join(cat_dir, f"{slug}.md")

        body = generate_article_body(t)
        
        md_content = f"""---
title: "{t['title']}"
summary: "{t['summary']}"
category: "{t['category']}"
category_title: "{t['category_title']}"
slug: "{t['slug']}"
date: "{t['date']}"
reading_time: "{t['reading_time']}"
target_audience: "{t['target_audience']}"
diagram_type: "{t['diagram_type']}"
cta_headline: "{t['cta_headline']}"
cta_text: "{t['cta_text']}"
---

{body}
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(md_content)

    print(f"[CONTENT-BUILDER] {len(topics)} teknik makale content/ dizinine basıldı.")


if __name__ == "__main__":
    build_markdown_files()
