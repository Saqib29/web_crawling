from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


chromedriver = "../chromedriver/chromedriver"
driver = webdriver.Chrome(chromedriver)

driver.set_page_load_timeout("10")
driver.get("http://google.com")

driver.find_element_by_name("q").send_keys("Birthday cake")
driver.execute_script("arguments[0].click();", driver.find_element_by_name("btnK"))

driver.maximize_window()
driver.refresh()

print("run completed")

time.sleep(4)
driver.quit()