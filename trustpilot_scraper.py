import requests
from bs4 import BeautifulSoup

def scrape_trustpilot(company):
    url = f"https://www.trustpilot.com/review/{company}.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    reviews = []

    for r in soup.select("article"):
        title = r.select_one("h2")
        body = r.select_one("p")

        if title and body:
            reviews.append({
                "title": title.text.strip(),
                "review": body.text.strip(),
                "source": "Trustpilot"
            })

    return reviews
