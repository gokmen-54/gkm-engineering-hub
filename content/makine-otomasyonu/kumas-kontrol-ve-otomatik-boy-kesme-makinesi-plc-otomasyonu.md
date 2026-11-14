---
title: "Kumaş Kontrol, Metraj Sarım & Barkodlu Tartım Makinesi PLC Otomasyonu: İkizler Tekstil Vaka Analizi"
summary: "Tekstil ve dokuma sanayisinde kumaş kalite kontrol, optik enkoderli metraj ölçümü, HANA dijital terazi (RS232) ve Argox barkod yazıcı ile otomatik kupon basımı mühendislik çözümü."
category: "makine-otomasyonu"
category_title: "Makine Otomasyonu"
slug: "kumas-kontrol-ve-otomatik-boy-kesme-makinesi-plc-otomasyonu"
date: "2026-11-14"
reading_time: "8 dk okuma"
target_audience: "Tekstil Fabrika Müdürleri & Özel Makine İmalatçıları"
diagram_type: "servo_sync"
cta_headline: "Kumaş Kontrol veya Boy Kesme Makineniz İçin Otomasyon mu Gerekiyor?"
cta_text: "Terazi, barkod yazıcı ve hassas metraj enkoderini tek bir PLC panelinde birleştiriyoruz. İkizler Tekstil referans projemizi inceleyin; makineniz için WhatsApp'tan hemen keşif isteyin."
---


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

