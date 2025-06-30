# DocuMind AI

Kurumsal PDF dokümanlarından anlam çıkaran, kullanıcıların bu dokümanlara doğal dilde soru sorup yanıt alabileceği LLM tabanlı bir soru-cevap sistemidir.

## Özellikler
- PDF yükleme ve metin çıkarımı
- 500-700 tokenlık parçalara bölme
- Google Gemini API ile vektörleştirme (embedding)
- ChromaDB ile vektör saklama ve arama
- Google Gemini Pro ile doğal dilde yanıt üretimi
- Streamlit tabanlı sade kullanıcı arayüzü
- Modüler Python 3.10+ kod yapısı

## Kurulum
1. Depoyu klonlayın veya indirin.
2. Gerekli Python paketlerini yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
3. `.env` dosyasını oluşturun ve Gemini API anahtarınızı girin:
   ```env
   GEMINI_API_KEY=your_gemini_api_key
   CHROMA_DB_PATH=./chroma_db
   ```
   Gemini API anahtarınızı almak için: https://aistudio.google.com/app/apikey

## Kullanım
1. `app.py` dosyasını çalıştırın:
   ```bash
   streamlit run app.py
   ```
2. PDF dosyanızı yükleyin.
3. Sormak istediğiniz soruyu girin ve yanıtı bekleyin.

## Dosya Yapısı
- `app.py` : Streamlit arayüzü ve entegrasyon
- `pdf_parser.py` : PDF okuma ve parçalara ayırma
- `vector_store.py` : Embedding ve ChromaDB işlemleri (Gemini API ile)
- `qa_engine.py` : Prompt oluşturma ve yanıt üretimi (Gemini API ile)
- `requirements.txt` : Bağımlılıklar
- `README.md` : Proje açıklaması

## Geliştirici
Kübra Keskin  
E-posta: kubrakeskin.2209@gmail.com 