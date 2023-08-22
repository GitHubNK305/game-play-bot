from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookies to click on
cookie = driver.find_element(By.ID, "cookie")

# Get price dic of afforded items
price_names = []
price_values = []
price_dic = {}

prices = driver.find_elements(By.CSS_SELECTOR, "#store b")

for price in prices[:-1]:
    price_names.append(price.text.split("-")[0].strip())
    price_values.append(int(price.text.split("-")[1].strip().replace(",", "")))

for n in range(len(price_names)):
    price_dic[price_names[n]] = price_values[n]

timeout = time.time() + 5  # 5 seconds to check items to buy
time_min = time.time() + 60 * 5  # 5 mins break

while True:
    cookie.click()

    # Every 5 seconds to check
    if time.time() > timeout:
        total_money = driver.find_element(By.ID, "money").text
        if "," in total_money:
            total_money = total_money.replace(",", "")

        items = []
        for price in price_values:
            if int(total_money) >= price:
                items.append(price_names[price_values.index(price)])
        # print(f"You can buy {items}")
        if len(items) >= 1:
            buy_item = driver.find_element(By.ID, f"buy{items[-1]}")
            buy_item.click()
            print(f"You have bought {items[-1]}")

        timeout = time.time() + 5

    if time.time() > time_min:
        cookie_per_second = driver.find_element(By.ID, "cps")
        print(cookie_per_second.text)

        break