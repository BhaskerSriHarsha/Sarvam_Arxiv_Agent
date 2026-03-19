from ddgs import DDGS
from langchain_core.tools import tool

@tool
def web_search(query: str) -> str:
    """
    Searches the web for current events, scientific literature, or general knowledge. 
    Use this tool when you need up-to-date information that you do not already know.
    """
    try:
        # Initialize the search and grab the top 3 results
        results = DDGS().text(query, max_results=3)
        
        if not results:
            return "No results found for this query."
            
        # Format the results into a clean, readable string for the LLM
        formatted_results = []
        for i, res in enumerate(results):
            formatted_results.append(
                f"Result {i+1}:\n"
                f"Title: {res['title']}\n"
                f"Snippet: {res['body']}\n"
                f"Source: {res['href']}\n"
            )
            
        return "\n".join(formatted_results)
        
    except Exception as e:
        return f"An error occurred during the web search: {str(e)}" 
    

@tool
def write_report(report: str) -> str:
    """Tool to write the final synthesized academic report to disk."""
    try:
        # Changed the extension from .txt to .md
        with open("report.md", "w", encoding="utf-8") as f:
            f.write(report)
        return "Success: Report written to report.md"
    except Exception as e:
        return f"Error writing to disk: {e}"