import os
import openai
import chromadb
from chromadb.config import Settings
from dotenv import load_dotenv

load_dotenv()

# Ortam değişkenlerinden ayarları al
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMBED_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-ada-002")
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "./chroma_db")

openai.api_key = OPENAI_API_KEY

# ChromaDB istemcisi oluştur
chroma_client = chromadb.Client(Settings(persist_directory=CHROMA_DB_PATH))
collection = chroma_client.get_or_create_collection("doc_chunks")

# Chunk'ları embed edip ChromaDB'ye kaydet
def embed_chunks(chunks):
    embeddings = []
    for chunk in chunks:
        response = openai.Embedding.create(input=chunk, model=EMBED_MODEL)
        emb = response["data"][0]["embedding"]
        embeddings.append(emb)
        collection.add(documents=[chunk], embeddings=[emb], ids=[str(hash(chunk))])
    return embeddings

# Sorguyu embed edip en yakın chunk'ları bul
def query_similar_chunks(query, top_k=3):
    response = openai.Embedding.create(input=query, model=EMBED_MODEL)
    query_emb = response["data"][0]["embedding"]
    results = collection.query(query_embeddings=[query_emb], n_results=top_k)
    return results["documents"][0] if results["documents"] else [] 