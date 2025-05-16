from serpapi import GoogleSearch
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
SERPAPI_KEY = os.getenv('SERPAPI_KEY')

def search_google(query, num_results=10):
    try:
        params = {
            "engine": "google",
            "q": query,
            "api_key": SERPAPI_KEY,
            "num": num_results
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        return [(result.get("title", ""), result.get("link", "")) 
                for result in results.get("organic_results", [])]
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

if __name__ == "__main__":
    topic = input("Enter a topic to search: ")
    results = search_google(topic)
    
    if results is None:
        print("\nError occurred while searching. Please check your API key.")
    elif not results:
        print("\nNo results found.")
    else:
        print("\nResults related to your topic:")
        for i, (title, link) in enumerate(results, 1):
            print(f"\n{i}. {title}")
            print(f"   {link}")