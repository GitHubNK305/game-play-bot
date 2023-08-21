from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# chrome_driver_path = "C:/Users/35850/Downloads/chromedriver-win64/chromedriver-win64.exe"
# service = Service(executable_path=chrome_driver_path)
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# for event_time in event_times:
#     print(event_time.get_attribute("datetime").split("T")[0])

event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# for event in event_names:
#     print(event.text)

events = {}
for n in range(len(event_times)):
    events[n] = {
        "name": event_times[n].get_attribute("datetime").split("T")[0],
        "event": event_names[n].text
    }

print(events)

# event_names = driver.find_elements(By.CSS_SELECTOR,
#                               "#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li")
# events_list = []
# events_dic_list = []
# events_dic = {}
# for event in event_names:
#     # print(event.text)
#     # print(event.text.split("/n")[1])
#     # dict = {event.text.split("/n")[0] : event.text.split("/n")[0]}
#     events_list.append(event.text)
#
# for event in events_list:
#     new_dic = {event.split("\n")[0]: event.split("\n")[1]}
#     events_dic_list.append(new_dic)
# # print(events_dic_list)
#
# keys = list(range(len(events_dic_list)))
# # print(keys)
# # for event in events_list:
# #     events_dic
# events_dic = {key: value for (key, value) in zip(keys, events_dic_list)}
# print(events_dic)

driver.quit()
