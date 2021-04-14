import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time
import wget


load_dotenv()


driver = webdriver.Chrome("../chromedriver/chromedriver")
driver.get("https://www.instagram.com/")


username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()

username.send_keys(os.environ.get('NAME'))
password.send_keys(os.environ.get('PASSWORD'))


log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

search_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
search_box.clear()
keyword = "#cat"
search_box.send_keys(keyword)

time.sleep(3)
search_box.send_keys(Keys.ENTER)


searc_enter = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
search_box.send_keys(Keys.ENTER)

time.sleep(3)

driver.execute_script("window.scrollTo(0,4000);")

images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]

# print(images)

path = os.getcwd()
path = os.path.join(path, keyword[1:]+"s")
os.mkdir(path)
# print(path)


counter = 0
for image in images[:5]:
    save_as = os.path.join(path, keyword[1:]+str(counter)+".jpg")
    wget.download(image, save_as)
    counter += 1
    

driver.quit()
