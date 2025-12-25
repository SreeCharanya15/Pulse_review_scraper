import requests
import json
import os
from bs4 import BeautifulSoup

def scrape_capterra(company):
    """
    Scrapes reviews from Capterra.
    NOTE:
    Capterra loads reviews dynamically via JavaScript.
    Static scraping may return 0 reviews.
    """

    print("⚠️ Attempting to scrape Capterra reviews (static HTML)...")
    print("⚠️ Capterra reviews are dynamically loaded. Results may be empty.")

    url = f"https://www.capterra.com/p/{company}/reviews/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "lxml")
    except Exception as e:
        print("❌ Error while fetching Capterra page:", e)
        return []

    reviews = []

    # Static HTML usually does not contain actual reviews
    for review in soup.select(".review"):
        title = review.select_one("h3")
        body = review.select_one(".review-comment")
        rating = review.select_one(".star-rating")

        if title and body:
            reviews.append({
                "title": title.text.strip(),
                "review": body.text.strip(),
                "rating": rating.text.strip() if rating else None,
                "source": "Capterra"
            })

    # Always write output file
    os.makedirs("output", exist_ok=True)
    with open("output/sample_reviews.json", "w", encoding="utf-8") as f:
        json.dump(reviews, f, indent=4, ensure_ascii=False)

    print(f"📊 Capterra reviews scraped: {len(reviews)}")
    return reviews
