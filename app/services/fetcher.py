import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
CHROME_BINARY_PATH = os.getenv("CHROME_BINARY_PATH")
WAIT_SECONDS = int(os.getenv("WAIT_SECONDS", 3))

def fetch_votes(poll_id):
    url = f"{BASE_URL}?pollName={poll_id}"
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = CHROME_BINARY_PATH

    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        time.sleep(WAIT_SECONDS)
        html = driver.page_source
    finally:
        driver.quit()

    soup = BeautifulSoup(html, "html.parser")
    rows = soup.select("table tr")

    results = []
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 2 and cols[0].text.strip().isdigit():
            results.append({
                "number": cols[0].text.strip(),
                "votes": cols[1].text.strip()
            })
    return results
