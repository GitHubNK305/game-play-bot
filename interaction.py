from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# game_is_on = True
time_period = 10
timeout = time.time() + time_period
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options)
# driver.maximize_window()
# time.sleep(2)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
# print(time.time())
# print(time.time()+timeout)

while time.time() < timeout:
    cookie.click()

money = driver.find_element(By.ID, "money")

print(int(money.text)/time_period)

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