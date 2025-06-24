# DocuMind AI

Kurumsal PDF dokümanlarından anlam çıkaran, kullanıcıların bu dokümanlara doğal dilde soru sorup yanıt alabileceği LLM tabanlı bir soru-cevap sistemidir.

## Özellikler
- PDF yükleme ve metin çıkarımı
- 500-700 tokenlık parçalara bölme
- OpenAI Embedding API ile vektörleştirme
- ChromaDB ile vektör saklama ve arama
- OpenAI GPT-4 (veya yerel model) ile doğal dilde yanıt üretimi
- Streamlit tabanlı sade kullanıcı arayüzü
- Modüler Python 3.10+ kod yapısı

## Kurulum
1. Depoyu klonlayın veya indirin.
2. Gerekli Python paketlerini yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
3. `.env` dosyasını oluşturun ve OpenAI API anahtarınızı, model adını vb. girin:
   ```env
   OPENAI_API_KEY=your_openai_key
   OPENAI_EMBEDDING_MODEL=text-embedding-ada-002
   OPENAI_LLM_MODEL=gpt-4
   CHROMA_DB_PATH=./chroma_db
   ```

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
- `vector_store.py` : Embedding ve ChromaDB işlemleri
- `qa_engine.py` : Prompt oluşturma ve yanıt üretimi
- `requirements.txt` : Bağımlılıklar
- `README.md` : Proje açıklaması

## Geliştirici
Kübra Keskin  
E-posta: kubrakeskin.2209@gmail.com 