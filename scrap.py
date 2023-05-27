from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

MIN_ELEMENTS = 10

def format_price(price_string: str):
    price_string = price_string.replace(u'\xa0', u' ')
    num = ""
    for c in price_string:
        if c == ",":
            num += f"."
            continue
        if c == " ":
            break
        num += f'{c}'
    return num

search_phrase = "bandaze+hurtowo"
driver = webdriver.Chrome()
driver.get(f"https://www.google.com/search?q={search_phrase}")
driver.fullscreen_window()
button = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div")
button.click()

elements = driver.find_elements(By.CLASS_NAME, "pla-unit")
while len(elements) < MIN_ELEMENTS:
    driver.close()
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/search?q=bandaze+hurtowo")
    driver.fullscreen_window()
    button = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div")
    button.click()
    elements = driver.find_elements(By.CLASS_NAME, "pla-unit")

prices = []
links = []
names = []
for e in elements:
    try:
        price = format_price(e.find_element(By.CLASS_NAME, "qptdjc").get_attribute("innerText"))
        name = e.find_element(By.CLASS_NAME, "LnPkof").get_attribute("innerText")
        link = e.find_element(By.CLASS_NAME, "plantl").get_attribute("href")
        prices.append(price), names.append(name), links.append(link)
    except:
        break
data = []
for i in range(len(prices)):
    if float(prices[i]) < 5:
        data.append([prices[i], names[i], links[i]])

print(data)
dataframe = {"data": data,
             "len": len(data),
             "search_phrase": search_phrase}

requests.post("http")