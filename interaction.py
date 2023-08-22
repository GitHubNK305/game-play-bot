from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import threading

# game_is_on = True
time_period = 10
timeout = time.time() + time_period
# print(timeout - time.time())
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options)
# driver.maximize_window()
# time.sleep(2)
prices_dic = {}
price_names = []
price_values = []

driver.get("http://orteil.dashnet.org/experiments/cookie/")

prices = driver.find_elements(By.CSS_SELECTOR, "#store b")


for price in prices[:-1]:
    # print(price.text.split("-")[0].strip())
    # print(price.text.split("-")[1].strip().replace(",", ""))
    price_names.append(price.text.split("-")[0].strip())
    price_values.append(int(price.text.split("-")[1].strip().replace(",", "")))


# print(price_names)
# print(price_values)

for n in range(len(price_names)):
    # prices_dic[n]= {
    #     "name":price_names[n],
    #     "price": price_values[n]
    # }
    prices_dic[price_names[n]] = price_values[n]

# print(prices_dic)
def purchase_check():
    threading.Timer(5.0, purchase_check).start()
    print("Hello, World!")
    total_money = driver.find_element(By.ID, "money")
    items = []
    for price in price_values:
        if int(total_money.text) >= price:
            items.append(price_names[price_values.index(price)])
    # print(f"You can buy {items}")
    if len(items) >= 1:
        buy_item = driver.find_element(By.ID, f"buy{items[-1]}")
        buy_item.click()
        print(f"You have bought {items[-1]}")


            



purchase_check()



cookie = driver.find_element(By.ID, "cookie")
# print(time.time())
# print(time.time()+timeout)

while time.time() < timeout:
    cookie.click()

cookie_per_second = driver.find_element(By.ID, "cps")
print(cookie_per_second.text)

# Select the first name element and enter name
# first_name = driver.find_element(By.NAME, "fName")
# first_name.send_keys("Jin")
#
# last_name = driver.find_element(By.NAME, "lName")
# last_name.send_keys("Tao")
#
# email = driver.find_element(By.NAME, "email")
# email.send_keys("jin.tao@silo.ai")
#
# button = driver.find_element(By.XPATH, '''/html/body/form/button''')
# button.click()

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# number = driver.find_element(By.XPATH, '''//*[@id='articlecount']/a[1]''')
# print(number.text)
#
# view_history = driver.find_element(By.LINK_TEXT, "View history")
#
# search = driver.find_element(By.NAME, "search")
# print(search.get_attribute("placeholder"))
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
# view_history.click()

# number.click()

# driver.quit()
