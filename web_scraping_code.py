from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

PRODUCT_URL = "https://www.amazon.in/VAYA-Hautechef-Pre-Seasoned-Cast-Kadhai/dp/B0F44BLP6X/"
PRICE_ALERT_THRESHOLD = 3000  
CSV_FILE = "amazon_product.csv"


# Setup Selenium
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

def get_text(soup, selector):
    element = soup.select_one(selector)
    return element.text.strip() if element else "N/A"

print("Opening Amazon product page...")
driver.get(PRODUCT_URL)
time.sleep(4)  # wait for page rendering

soup = BeautifulSoup(driver.page_source, "html.parser")

# Scrape product info
title = get_text(soup, "#productTitle")
price_text = get_text(soup, ".a-price-whole").replace(",", "")
rating = get_text(soup, ".a-icon-alt")

# Convert price to int (if possible)
try:
    price = int(price_text)
except:
    price = None

driver.quit()

# Prepare data
data = [{
    "Product Title": title,
    "Price (INR)": price,
    "Rating": rating,
    "Product URL": PRODUCT_URL
}]

# Save to CSV
df = pd.DataFrame(data)
df.to_csv(CSV_FILE, index=False)
print(f"\n✅ Data saved to CSV: {CSV_FILE}")

# Price alert
print("\nChecking for price drops...")
if price and price < PRICE_ALERT_THRESHOLD:
    print(f"🚨 PRICE DROP ALERT! {title} is now ₹{price}")
else:
    print("No price drop detected.")

print("\nScraping completed.")
