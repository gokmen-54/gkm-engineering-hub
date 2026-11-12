---
title: "Yüksek Hızlı Makinelerde Servo Sürücü Kazanç Ayarı (Tuning) ve Notch Filtre ile Mekanik Rezonans Giderme"
summary: "Makine şasesindeki titreşim ve çınlama seslerini (chatter) ortadan kaldıran otomatik/manuel servo kazanç optimizasyonu, feedforward kontrolü ve notch filtre uygulaması."
category: "makine-otomasyonu"
category_title: "Makine Otomasyonu"
slug: "servo-motor-surucu-parametre-ayari-ve-rezonans-filtreleme"
date: "2026-11-05"
reading_time: "6 dk okuma"
target_audience: "Mekanik Tasarımcılar, Makine Kurulum Ekipleri & İmalatçılar"
diagram_type: "servo_tuning"
cta_headline: "Makinanız Titriyor veya Konum Kaçırıyor mu?"
cta_text: "Saha mühendislerimiz servo sürücü tuning ve mekanik eksen kalibrasyonunu yerinde veya uzaktan çözer. Hemen iletişime geçin."
---


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

