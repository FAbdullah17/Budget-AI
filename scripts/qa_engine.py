import logging
from typing import Optional
from dotenv import load_dotenv

from scripts.utils import summarize_transaction_file
from scripts.web_search import search_web
from scripts.llm_config import ask_llm

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def validate_query(query: str) -> bool:
    return isinstance(query, str) and len(query.strip()) >= 5


def answer_question(
    query: Optional[str] = None,
    file_path: Optional[str] = None
) -> str:
    try:
        # If user uploads a bank file
        if file_path:
            summary = summarize_transaction_file(file_path)
            if query and validate_query(query):
                prompt = f"""Use the following bank transaction summary to answer the user's question.

Transaction Summary:
{summary}

User Question:
{query}

Answer:"""
                return ask_llm(question=query, context=summary)  # FIXED keyword
            return summary

        # If user just asks a question
        elif query and validate_query(query):
            context = search_web(query)
            if not context or "No useful web content found." in context:
                return "No useful information found via web search."
            return ask_llm(question=query, context=context)  # FIXED keyword

        return "Please provide a question or upload a bank file."

    except Exception as e:
        logger.error("Failed to generate answer", exc_info=True)
        return "An unexpected error occurred while answering the query."


if __name__ == "__main__":
    print("\nBudget-AI:\n")

    query = input("Enter your question (or press Enter to skip): ").strip()
    file_path = input("Enter path to your bank statement CSV/Excel (or press Enter to skip): ").strip()

    file_path = file_path if file_path else None
    query = query if query else None

    result = answer_question(query=query, file_path=file_path)
    print("\nResult:\n")
    print(result)
