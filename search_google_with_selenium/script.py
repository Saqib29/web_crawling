from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 



chromedriver = "../chromedriver/chromedriver"
driver = webdriver.Chrome(chromedriver)

driver.set_page_load_timeout("10")
driver.get("http://google.com")

driver.find_element_by_name("q").send_keys("Birthday cake")
driver.execute_script("arguments[0].click();", driver.find_element_by_name("btnK"))

driver.maximize_window()
driver.refresh()


image = driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')

image.click()


# imgs = WebDriverWait(driver, 10).until(EC.element_located_to_be_selected((By.XPATH, '//*[@id="islrg"]/div[1]/div[3]/a[1]/div[1]/img')))
time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(10)

imgs = driver.find_elements_by_tag_name('img')

images = [img.get_attribute('src') for img in imgs]

for image in images:
    if image is None:
        continue
    if "http" not in image:
        continue
    print(image)


time.sleep(4)
driver.quit()