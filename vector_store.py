import os
import google.generativeai as genai
import chromadb
from chromadb.config import Settings
from dotenv import load_dotenv

load_dotenv()

# Ortam değişkenlerinden ayarları al
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "./chroma_db")

# Gemini API anahtarını yapılandır
genai.configure(api_key=GEMINI_API_KEY)

# ChromaDB istemcisi oluştur
chroma_client = chromadb.Client(Settings(persist_directory=CHROMA_DB_PATH))
collection = chroma_client.get_or_create_collection("doc_chunks")

# Chunk'ları embed edip ChromaDB'ye kaydet
def embed_chunks(chunks):
    embeddings = []
    for chunk in chunks:
        response = genai.embed_content(
            model="models/embedding-001",
            content=chunk,
            task_type="retrieval_document"
        )
        emb = response["embedding"]
        embeddings.append(emb)
        collection.add(documents=[chunk], embeddings=[emb], ids=[str(hash(chunk))])
    return embeddings

# Sorguyu embed edip en yakın chunk'ları bul
def query_similar_chunks(query, top_k=3):
    response = genai.embed_content(
        model="models/embedding-001",
        content=query,
        task_type="retrieval_query"
    )
    query_emb = response["embedding"]
    results = collection.query(query_embeddings=[query_emb], n_results=top_k)
    return results["documents"][0] if results["documents"] else [] 