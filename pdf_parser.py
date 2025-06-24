import fitz  # PyMuPDF
import tiktoken
from typing import List

# PDF dosyasını oku ve metni döndür
def load_pdf(file_path: str) -> str:
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Metni token bazlı parçalara ayır
def chunk_text(text: str, chunk_size: int = 600) -> List[str]:
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)
    chunks = []
    for i in range(0, len(tokens), chunk_size):
        chunk = enc.decode(tokens[i:i+chunk_size])
        chunks.append(chunk)
    return chunks 