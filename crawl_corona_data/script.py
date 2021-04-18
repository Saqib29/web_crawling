from selenium import webdriver
import time 
import csv


chromedriver = '../chromedriver/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.worldometers.info/coronavirus/')

time.sleep(2)
data = driver.find_elements_by_id('maincounter-wrap')

coronavirous_cases = data[0].text.split("\n")
deaths = data[1].text.split("\n")
recovered = data[2].text.split("\n")

print(coronavirous_cases, deaths, recovered)


rows = len(driver.find_elements_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr'))
columns = len(driver.find_elements_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[7]/td'))

cases = {}

driver.execute_script("window.scrollTo(0, 4000)") 
driver.execute_script("window.scrollTo(4000, 8000)") 



for row in range(5, rows+1):
    cases[row-4] = []
    for col in range(2, columns+1):
        value = driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr['+ str(row) +']/td['+ str(col) +']')
        # print(value.text, end=" | ")
        cases[row-4].append(value.text)
    
    # if row-4 > 50:
    #     break


time.sleep(5)
driver.quit()

print("Completed")

# for key in cases:
#     print(cases[key])

name = str(time.localtime().tm_year)+"_"+str(time.localtime().tm_mon)+"_"+str(time.localtime().tm_mday)+"_"+str(time.localtime().tm_hour)+"_"+str(time.localtime().tm_min)+"_"+str(time.localtime().tm_sec)

with open(f'{name}.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Country', 'Total Cases', 'New Cases', 'Total deaths', 'New Deaths', 'Total Recovered', 'Active cases', 'Serious Cases', 'Serious', 'Top Cases', 'Total Tests', 'Tests', 'Population'])
    for key in cases:
        writer.writerow(cases[key])