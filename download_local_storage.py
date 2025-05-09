import requests
from playwright.sync_api import sync_playwright
import os
from tenacity import retry, stop_after_attempt, wait_fixed


save_dir = "./data/active_travel/"
os.makedirs(save_dir, exist_ok=True)

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def download_file(url, path):
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()
        with open(path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded: {path} ({response.headers.get('content-length', 'unknown')} bytes)")
        return True
    except Exception as e:
        print(f"Failed: {url} - {e}")
        return False

def get_csv_urls():
    csv_urls = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print(f"Navigating to https://cycling.data.tfl.gov.uk/...")
        page.goto("https://cycling.data.tfl.gov.uk/", timeout=60000)
        page.wait_for_load_state("networkidle") 
        
        tables = page.query_selector_all("table")
        if not tables:
            print("No tables found on the page.")
            browser.close()
            return []
        
        print(f"Found {len(tables)} tables. Searching for CSV links...")
        
        for table in tables:
            rows = table.query_selector_all("tr")
            for row in rows:
                link = row.query_selector("a")
                if link:
                    href = link.get_attribute("href")
                    if href:
                        full_url = href if href.startswith("http") else f"https://cycling.data.tfl.gov.uk{href}"
                        print(f"Found link: {full_url}")
                        if ("activetravelcountsprogramme" in full_url.lower() and 
                            full_url.lower().endswith(".csv")):
                            csv_urls.append(full_url)
        
        browser.close()
    return csv_urls

print("Scraping https://cycling.data.tfl.gov.uk/ for ActiveTravelCountsProgramme CSVs...")
csv_urls = get_csv_urls()
if not csv_urls:
    print("No CSVs found. Possible issues:")
    print("- Table structure changed (no table with ActiveTravelCountsProgramme links).")
    print("- Links do not contain 'ActiveTravelCountsProgramme' or '.csv'.")
    print("- Data moved to another URL.")
else:
    print(f"Found {len(csv_urls)} CSV files:")
    for url in csv_urls:
        print(url)

for url in csv_urls:
    filename = url.split("/")[-1].replace("%20", "_")
    file_path = os.path.join(save_dir, filename)
    download_file(url, file_path)

print(f"Finished downloading {len(csv_urls)} CSVs to {save_dir}")