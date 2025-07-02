import os
import logging
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def ask_llm(question: str, context: str) -> str:
    """
    Sends a prompt to Groq's LLaMA3 model using OpenAI client syntax.
    """
    prompt = f"""Use the context below to answer the user's question as accurately and clearly as possible.

Context:
{context}

Question:
{question}

Answer:"""

    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        logger.error("LLM API call failed", exc_info=True)
        return "Sorry, an error occurred while generating the answer from the LLM."
