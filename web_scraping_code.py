import csv
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

def get_url(search_term):
    '''Generate a url from search term'''
    template = "https://www.amazon.com/s?k={}&ref=nb_sb_noss_2"
    search_term = search_term.replace(' ', '+')
    
    # add term query to url
    url = template.format(search_term)
    
    return url

def extract_record(item):
    '''Extract and return data from a single record'''
    
    atag = item.h2.a
    description = atag.text.strip()
    
    try:
        price_parent = item.find('span', 'a-price')
        price = price_parent.find('span', 'a-offscreen').text
    except AttributeError:
        return
    
    try:
        rating = item.i.text
    except AttributeError:
        rating = ''
    
    result = (description, price, rating)
    
    return result

def main(search_term):
    '''Run main program routine'''
    # startup the web driver
    driver = webdriver.Chrome('/home/soham/pypypy/chromedriver')
    
    records = []
    url = get_url(search_term)

    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = soup.find_all('div', {'data-component-type': 's-search-result'})

    for item in results:
        record = extract_record(item)
        if record:
            records.append(record)
    driver.close()

    #save the data

    with open('results.csv', 'w', newline = '', encoding = 'utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Description', 'Price', 'Rating'])
        writer.writerows(records)
        
    df = pd.read_csv('results.csv')
    print (df) 
        
n = input("Enter search query: ")
main(n)
