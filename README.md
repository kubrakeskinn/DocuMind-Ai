# DocuMind AI: Kurumsal PDF Soru-Cevap Platformu

## Proje Hakkında

DocuMind AI, PDF formatındaki kurumsal dokümanlardan anlamlı bilgi çıkarmayı ve bu dokümanlara doğal dilde soru sorarak yanıt almayı mümkün kılan bir yapay zeka uygulamasıdır. Sistem, Google Gemini API altyapısı ile çalışmakta olup, metin vektörleştirme ve semantik arama işlemlerini ChromaDB ile gerçekleştirmektedir. Uygulama, kullanıcı dostu bir arayüz ile etkileşimli ve hızlı bir deneyim sunar.

## Temel Özellikler

- PDF dosyalarından metin çıkarımı
- Metni anlamlı parçalara (chunk) bölme
- Google Gemini API ile vektörleştirme ve doğal dilde yanıt üretimi
- ChromaDB ile hızlı ve etkili vektör arama
- Türkçe dil desteği ve detaylı cevaplar
- Streamlit tabanlı modern arayüz
- Güvenli API anahtarı yönetimi

## Kurulum ve Kullanım

1. **Projeyi klonlayın:**
   ```bash
   git clone https://github.com/kullanici/DocuMind-Ai.git
   cd DocuMind-Ai
   ```

2. **Gereksinimleri yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

3. **.env dosyasını oluşturun ve API anahtarınızı ekleyin:**
   ```env
   GEMINI_API_KEY=buraya_gemini_api_anahtarınızı_yapıştırın
   CHROMA_DB_PATH=./chroma_db
   ```
   > Gemini API anahtarınızı almak için: https://aistudio.google.com/app/apikey

4. **Uygulamayı başlatın:**
   ```bash
   streamlit run app.py
   ```

5. **PDF dosyanızı yükleyin, sorunuzu yazın ve yanıtı alın.**

## API Anahtarı ve Kota Yönetimi

- `.env` dosyanızda **GEMINI_API_KEY** mutlaka bulunmalıdır.
- API anahtarınızın süresi dolduğunda veya kota sınırına ulaşıldığında, Google AI Studio üzerinden yeni bir anahtar oluşturabilirsiniz.
- Ücretsiz kullanım kotası dolduğunda, faturalandırma ekleyerek daha yüksek limitlere erişebilirsiniz.
- API anahtarınızı güvenli bir şekilde saklayınız ve kimseyle paylaşmayınız.

## Sık Karşılaşılan Hatalar ve Çözümleri

| Hata Kodu | Açıklama | Çözüm |
|-----------|----------|-------|
| 401 Unauthorized | API anahtarınız yanlış veya süresi dolmuş olabilir. | Yeni bir anahtar oluşturun ve .env dosyanıza ekleyin. |

---

**DocuMind AI, kurumsal dokümanlarınızı daha erişilebilir ve anlamlı kılmak için geliştirilmiştir. Projeyi kullanırken veya geliştirirken karşılaştığınız her türlü sorunda iletişime geçebilirsiniz.** 