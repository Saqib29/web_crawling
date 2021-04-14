import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()


# driver = webdriver.Chrome("../chromedriver/chromedriver")
# driver.get("https://www.instagram.com/")


# username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
# password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# username.clear()
# password.clear()

# username.send_keys(os.environ.get('USERNAME'))
# password.send_keys(os.environ.get('PASSWORD'))


print(os.environ.get('USERNAME'))
print(os.environ.get('PASSWORD'))