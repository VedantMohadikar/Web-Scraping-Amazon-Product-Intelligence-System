# Web-Scraping-Amazon-Product-Intelligence-System
A Python-based web scraping tool that extracts **product details from Amazon search results**, including:

- 📦 Product Title
- 💰 Price
- ⭐ Rating

The extracted data is saved into a CSV file and displayed using Pandas.

---

## 🚀 Features

- 🔍 Search Amazon products dynamically
- 📊 Extract product details (title, price, rating)
- 💾 Save results to CSV (`results.csv`)
- 🧾 Display structured output using Pandas
- ⚡ Uses Selenium for dynamic content loading

---

## 🧠 How It Works

1. User inputs a search query  
2. Script generates Amazon search URL  
3. Selenium loads the webpage  
4. BeautifulSoup parses HTML  
5. Extracts product details  
6. Saves results to CSV  
7. Displays data as a DataFrame  

---

## 📦 Tech Stack

- Python
- Selenium
- BeautifulSoup (bs4)
- Pandas
- CSV

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install selenium beautifulsoup4 pandas
