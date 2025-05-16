import flet as ft
from serpapi import GoogleSearch
import webbrowser
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
            "num": num_results,
            "gl": "us",  # Add country parameter
            "hl": "en"   # Add language parameter
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        if "error" in results:
            print(f"API Error: {results['error']}")
            return None
        return [(result.get("title", ""), result.get("link", "")) 
                for result in results.get("organic_results", [])]
    except Exception as e:
        print(f"Search error: {str(e)}")
        return None

def main(page: ft.Page):
    page.title = "Web Search App"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 20

    def open_url(e, url):
        webbrowser.open(url)

    def search_click(e):
        if not topic_input.value:
            topic_input.error_text = "Please enter a search topic"
            page.update()
            return

        progress_ring.visible = True
        page.update()
        
        results = search_google(topic_input.value)
        results_column.controls.clear()
        
        if results is None:
            results_column.controls.append(
                ft.Text("Error occurred while searching. Please check your API key.", 
                       color="red", size=16)
            )
        elif not results:
            results_column.controls.append(
                ft.Text("No results found.", color="red", size=16)
            )
        else:
            for title, link in results:
                results_column.controls.append(
                    ft.Container(
                        content=ft.Column([
                            ft.TextButton(
                                text=title or link,
                                on_click=lambda e, url=link: open_url(e, url),
                                style=ft.ButtonStyle(color={"hovered": ft.Colors.BLUE_700}),
                            ),
                            ft.Text(link, size=12, color="grey")
                        ]),
                        padding=10,
                        border_radius=10,
                        ink=True
                    )
                )
        
        progress_ring.visible = False
        page.update()

    topic_input = ft.TextField(
        label="Enter a topic to search",
        width=400,
        prefix_icon=ft.Icons.SEARCH,
        on_submit=search_click
    )

    progress_ring = ft.ProgressRing(visible=False)
    results_column = ft.Column(scroll=ft.ScrollMode.AUTO, spacing=10)

    page.add(
        ft.Column([
            ft.Text("Web Search", size=32, weight=ft.FontWeight.BOLD),
            ft.Row([topic_input, ft.ElevatedButton("Search", on_click=search_click)],
                  alignment=ft.MainAxisAlignment.CENTER),
            progress_ring,
            results_column
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)
    )

if __name__ == "__main__":
    ft.app(target=main)