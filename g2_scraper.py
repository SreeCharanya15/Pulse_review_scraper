import requests
import json
import os
from bs4 import BeautifulSoup

def scrape_g2(company):
    """
    Scrapes reviews from G2.
    NOTE:
    G2 loads reviews dynamically using JavaScript.
    Static scraping (requests + BeautifulSoup) may return 0 reviews.
    """

    print("⚠️ Attempting to scrape G2 reviews (static HTML)...")
    print("⚠️ G2 uses JavaScript-rendered content. Results may be empty.")

    url = f"https://www.g2.com/products/{company.lower()}/reviews"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "lxml")
    except Exception as e:
        print("❌ Error while fetching G2 page:", e)
        return []

    reviews = []

    # G2 reviews are JS-rendered, so this usually finds nothing
    for review in soup.select(".paper"):
        title = review.select_one(".review-title")
        body = review.select_one(".formatted-text")

        if title and body:
            reviews.append({
                "title": title.text.strip(),
                "review": body.text.strip(),
                "source": "G2"
            })

    # Always write output file (even if empty)
    os.makedirs("output", exist_ok=True)
    with open("output/sample_reviews.json", "w", encoding="utf-8") as f:
        json.dump(reviews, f, indent=4, ensure_ascii=False)

    print(f"📊 G2 reviews scraped: {len(reviews)}")
    return reviews
