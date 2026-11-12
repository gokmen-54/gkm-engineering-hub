---
title: "Endüstriyel Ortamlar İçin 4 Katmanlı PCB Tasarımı: EMC/EMI Koruması ve Ground Plane Kuralları"
summary: "Motor sürücüleri ve şalt sahalarının oluşturduğu elektriksel gürültülere (EMC/ESD) dayanıklı 4 katmanlı (SIG-GND-PWR-SIG) endüstriyel kart tasarımı, diferansiyel empedans hesabı ve izolasyon teknikleri."
category: "pcb-elektronik-tasarim"
category_title: "PCB & Elektronik Tasarım"
slug: "endustriyel-ortamlar-icin-4-katmanli-pcb-tasarim-kurallari"
date: "2026-11-11"
reading_time: "9 dk okuma"
target_audience: "Ar-Ge Departmanları, Donanım Tasarımcıları & Cihaz Üreticileri"
diagram_type: "pcb_stackup"
cta_headline: "Özel Elektronik Kart Projeniz mi Var?"
cta_text: "Şematik, blok diyagram veya gerber dosyalarınızı WhatsApp üzerinden paylaşın; DFM (Üretilebilirlik) analizi ve prototip bütçelendirmesini 24 saatte sunalım."
---


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

