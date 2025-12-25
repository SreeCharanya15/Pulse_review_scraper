
#Pulse Coding Assignment – SaaS Review Scraper

#Project Overview

This project is a Python-based review scraping tool that collects product reviews for SaaS companies from popular review platforms and outputs them in a structured JSON format.

#Tech Stack

Language: Python 3

Libraries:
-requests
-beautifulsoup4
-lxml
-pandas

Tools:
-Command Prompt (CMD)
-VS Code

Environment: Python Virtual Environment (venv)

#Setup Instructions

1. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate.bat

2. Install dependencies
pip install -r requirements.txt

#How to Run the Script

-G2 Reviews
python main.py --company zoom --start_date 2024-01-01 --end_date 2024-03-31 --source g2

-Capterra Reviews
python main.py --company slack --start_date 2024-01-01 --end_date 2024-03-31 --source capterra

-Trustpilot Reviews
python main.py --company slack --start_date 2024-01-01 --end_date 2024-03-31 --source trustpilot

#Important Note on G2 & Capterra

G2 and Capterra load reviews dynamically using JavaScript.

Since this project uses a lightweight static scraping approach (requests + BeautifulSoup),
reviews from these platforms may return zero results without browser automation tools like Selenium.

This limitation is:

-Clearly handled in the code
-Logged transparently in the terminal
-Documented to reflect real-world constraints


To demonstrate end-to-end functionality, Trustpilot was integrated as an additional SaaS review source where reviews are accessible via static HTML.
