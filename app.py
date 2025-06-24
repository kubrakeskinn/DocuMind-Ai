import streamlit as st
import tempfile
from pdf_parser import load_pdf, chunk_text
from vector_store import embed_chunks, query_similar_chunks
from qa_engine import generate_answer

st.set_page_config(page_title="DocuMind AI", layout="centered")
st.title("DocuMind AI - Kurumsal PDF Soru-Cevap")

# PDF yükleme alanı
uploaded_file = st.file_uploader("PDF dosyanızı yükleyin", type=["pdf"])

if uploaded_file:
    # Geçici dosyaya kaydet
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    # PDF'ten metni çıkar
    text = load_pdf(tmp_path)
    st.success("PDF başarıyla okundu.")

    # Metni chunk'lara böl
    chunks = chunk_text(text)
    st.info(f"{len(chunks)} adet parça oluşturuldu.")

    # Chunk'ları embed edip vektör veritabanına ekle
    embed_chunks(chunks)
    st.success("Vektörler oluşturuldu ve kaydedildi.")

    # Soru giriş alanı
    question = st.text_input("Sorunuzu yazın:")

    if question:
        # Soruya en yakın chunk'ları bul
        relevant_chunks = query_similar_chunks(question, top_k=3)
        # LLM ile yanıt üret
        answer = generate_answer(question, relevant_chunks)
        st.subheader("Yanıt:")
        st.write(answer) 