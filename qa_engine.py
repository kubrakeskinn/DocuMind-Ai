import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# Prompt template ve yanıt üretimi
PROMPT_TEMPLATE = """
Aşağıda bir PDF dokümanından alınmış ilgili parçalar bulunmaktadır:

{context}

Kullanıcı sorusu: {question}

Yalnızca yukarıdaki içerikten faydalanarak, Türkçe ve detaylı bir yanıt ver.
"""

def generate_answer(question, relevant_chunks):
    context = "\n\n".join(relevant_chunks)
    prompt = PROMPT_TEMPLATE.format(context=context, question=question)
    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    return response.text.strip()

if __name__ == "__main__":
    # Anahtarı test etmek için küçük bir kod
    try:
        test_client = genai.GenerativeModel("gemini-pro")
        models = test_client.list_models()
        print("API anahtarınız çalışıyor! Mevcut modeller:")
        for model in models.data:
            print(model.id)
    except Exception as e:
        print("API anahtarınız çalışmıyor veya erişim yok!")
        print(e)

    print("Erişebildiğiniz Gemini modelleri:")
    for m in genai.list_models():
        print(m.name) 