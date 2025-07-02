import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_web(query: str, max_results: int = 3) -> str:
    try:
        result = tavily.search(query=query, max_results=max_results)
        articles = result.get("results", [])
        context = "\n\n".join([item["content"] for item in articles if "content" in item])
        return context.strip() if context else "No useful web content found."
    except Exception as e:
        return f"Error while searching the web: {str(e)}"
