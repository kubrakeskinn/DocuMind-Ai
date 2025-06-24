import os
import openai
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LLM_MODEL = os.getenv("OPENAI_LLM_MODEL", "gpt-4")
openai.api_key = OPENAI_API_KEY

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
    response = openai.ChatCompletion.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=512
    )
    return response["choices"][0]["message"]["content"].strip() 