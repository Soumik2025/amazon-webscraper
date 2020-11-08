from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import datetime


PATH = ".\chromedriver.exe" # the seleniun webdriver
URL = "The Amazon URL" # the url you want to to 

driver = webdriver.Chrome(PATH)
driver.maximize_window()

def get_amazon_data(url):
    driver.get(url)
    body_el = driver.find_element_by_css_selector("body")
    html_obj = body_el.get_attribute("innerHTML")
    return html_obj


def remove(string): 
    return "".join(string.split()) 

title_lookup = "productTitle"
price_lookup = "priceblock_ourprice"
html_str = get_amazon_data(URL)

soup = BeautifulSoup(html_str, 'html.parser')

product_title_soup = soup.find(id=title_lookup).text
product_price_soup = soup.find(id=price_lookup).text

scrape_time = datetime.datetime.now()
product_title = remove(product_title_soup)
product_price = remove(product_price_soup)

print(f"Scraped Data")
print(f"Scraped At: {scrape_time}")
print(f"Product Name: {product_title}")
print(f"Product Price: {product_price}")


driver.quit()
