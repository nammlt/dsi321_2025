from duckduckgo_search import DDGS

with DDGS() as ddgs:
    results = ddgs.text("alternative materials for construction", max_results=5)
    for r in results:
        print(f"Title: {r['title']}")
        print(f"URL: {r['href']}")
        print(f"Snippet: {r['body']}\n")
