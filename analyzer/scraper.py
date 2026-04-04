from urllib.parse import urlencode
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright


INDEED_URL = "https://it.indeed.com/jobs"
INDEED_UL_CLASS = "css-pygyny eu4oa1w0"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Referer": "https://www.google.com/",
}

class Scraper():
    def __init__(self):
        pass
    
    
    def _getIndeed_url(self, job, location):
        params = {
            'q': job,
            'l': location
        }
        query_string = urlencode(params)
        return f"{INDEED_URL}?{query_string}"
    
    def scrapeIndeed(self, job, location):
        url = self._getIndeed_url(job, location)
        print(url)

        
        # Getting the raw html
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            html = page.content()
            browser.close()

        
        print(html)
        soup = BeautifulSoup(html, "html.parser")


scraper = Scraper()

scraper.scrapeIndeed("COMPUTER SCIENCE", "Mestre, Venezia")