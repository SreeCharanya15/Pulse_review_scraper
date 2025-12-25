import argparse
from scraper.g2_scraper import scrape_g2
from scraper.capterra_scraper import scrape_capterra
from scraper.trustpilot_scraper import scrape_trustpilot

parser = argparse.ArgumentParser(description="SaaS Review Scraper")

parser.add_argument("--company", required=True)
parser.add_argument("--start_date", required=True)
parser.add_argument("--end_date", required=True)
parser.add_argument("--source", required=True)

args = parser.parse_args()

if args.source.lower() == "g2":
    reviews = scrape_g2(args.company)
elif args.source.lower() == "capterra":
    reviews = scrape_capterra(args.company)
elif args.source.lower() == "trustpilot":
    reviews = scrape_trustpilot(args.company)
else:
    print("Invalid source")

print(f"Scraped {len(reviews)} reviews")
