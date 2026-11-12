# GKM Elektrik & Mühendislik // Programmatic Engineering Hub

Bu depo, **GKM Elektrik & Mühendislik** (`gkmelektrik.com`) için geliştirilmiş; arama motorlarında (Google) yerel sanayicileri, makine imalatçılarını ve Türkiye genelindeki Ar-Ge projelerini yakalayıp WhatsApp ve ana siteye yönlendiren **Otomatik SEO, Teknik Rehber ve Müşteri Yakalama Motoru**dur.

---

## 🚀 Kapsam ve Hizmet Alanları
1. **Makine Otomasyonu:** Özel makine otomasyon yazılımları, elektronik kamlama (camming), servo/step motor senkronizasyonu, hat revizyonu.
2. **Endüstriyel Yazılım & SCADA:** Siemens (TIA Portal SCL), Schneider, Beckhoff PLC programlama, SCADA mimarileri, Endüstriyel IoT (MQTT, Modbus TCP).
3. **PCB Tasarımı & Elektronik:** Çok katmanlı endüstriyel kart tasarımı, Altium/KiCad şematiği, STM32/ESP32 gömülü yazılım, optokuplörlü izole sensör kartları.
4. **Elektrik Panosu & Şalt:** IEC 61439 tip testli Ana Dağıtım (ADP), MCC motor kontrol, %7 de-tuned harmonik filtreli kompanzasyon ve toptan şalt tedariği.

---

## ⚡ Sistem Mimarisi & 0 TL Masraf
- **Mimarisi:** Python tabanlı bağımsız Statik Site Üreteci (SSG) + Tailwind CSS.
- **Performans:** Google PageSpeed 100/100, sıfır harici hantal kütüphane, anında yüklenme.
- **SEO & Google İndeksi:**
  - Her makalede Schema.org `TechArticle`, `BreadcrumbList`, `Organization` ve `FAQPage` etiketleri.
  - Vektörel teknik şemalar (SVG formatında retina keskinliğinde).
  - Otomatik güncellenen `sitemap.xml` ve `robots.txt`.
- **Dönüşüm Hunisi:**
  - Doğrudan WhatsApp hattına (`0537 702 99 54`) önceden doldurulmuş şablonlarla yönlendirme.
  - Resmi kurumsal siteye (`gkmelektrik.com`) yönlendirme bağlantıları.
  - Mobilde sabit duran "Hemen Proje Danış" ve "WhatsApp'tan Şema Gönder" aksiyon çubuğu.

---

## 🤖 Günlük Otomasyon (GitHub Actions)
`.github/workflows/daily-content.yml` her sabah otomatik olarak:
1. Yüksek arama hacmine sahip yeni bir teknik makale üretir.
2. Özel teknik SVG şemasını çizer.
3. Statik siteyi ve `sitemap.xml` dosyasını baştan derler.
4. Değişiklikleri repoya push eder.

---

## 🌐 0 TL Barındırma Kurulumu (Cloudflare Pages veya GitHub Pages)

### Seçenek 1: Cloudflare Pages (Önerilen - Saniyeler İçinde Kurulum)
1. [dash.cloudflare.com](https://dash.cloudflare.com) adresine gidin.
2. **Workers & Pages** ➔ **Create Application** ➔ **Pages** ➔ **Connect to Git** seçin.
3. Bu depoyu (`gkm-engineering-hub`) seçin.
4. Derleme Ayarları:
   - **Framework Preset:** None
   - **Build command:** `python build.py`
   - **Build output directory:** `dist`
5. **Save and Deploy** butonuna basın. Siteniz 15 saniyede dünya çapında 300+ CDN noktasında yayına girer. İsterseniz `hub.gkmelektrik.com` alt alan adını tek tıkla bağlayabilirsiniz!

### Seçenek 2: GitHub Pages
1. Repo Ayarları (Settings) ➔ **Pages** sekmesine gidin.
2. Kaynak olarak `Deploy from a branch` seçin, `main` dalı ve `/dist` (veya `gh-pages`) klasörünü seçip kaydedin.
