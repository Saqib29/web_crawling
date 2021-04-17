import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




class crawledArticle():
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Bot:
    def article(self, name):
        count = 1
        page = 1
        pageIncrement = 10
        maxRetrieves = 10

        a = []
        chromedriver = "/home/saqib/work/selenium/chromedriver/chromedriver"

        url = "https://www.amazon.com/s?k="+ name + "&page=" + str(page)

        options = Options()
        options.headless = False
        options.add_experimental_option("detach", True)

        browser = webdriver.chrome(chromedriver)
        browser.maximize_window()
        browser.get(url)
        browser.set_page_load_timeout(10)


        while True:
            try:
                if pageIncrement*page > maxRetrieves:
                    break

                if count > pageIncrement:
                    count = 1
                    page += 1
                
                # GetTitle
                xPathTitle = '//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div['+ str(count) +']/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span'
                title = browser.find_element_by_xpath(xPathTitle)
                titleText = title.get_attribute("innerHTML").splitlines()[0]
                title.click()


                xPathPrice = '//*[@id="price_inside_buybox"]'
                price = browser.find_element_by_xpath(xPathPrice)
                priceText = price.get_attribute("innerHTML")

                url = "https://www.amazon.com/s?k="+ name + "&page=" + str(page)
                browser.get(url)
                browser.set_page_load_timeout(10)

                info = crawledArticle(titleText, priceText)

                a.append(info)

                count += 1

            except Exception as e:
                print("Exception", e)
                count += 1

                if pageIncrement*page > maxRetrieves:
                    break

                if count > pageIncrement:
                    count = 1
                    page += 1
                
                url = "https://www.amazon.com/s?k="+ name + "&page=" + str(page)
                browser.get(url)
                browser.set_page_load_timeout(10)


        browser.close()

        return a


fetcher = Bot()


# with open('result.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     articlewriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for article in fetcher.article("iphone 11"):
#         articlewriter.writerow([article.title, article.price])

with open('pro.csv', 'w', newline='', encoding='utf-8') as csvfile:
    articlewriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for article in fetcher.article("iphone 11"):
        articlewriter.writerow([article.title,article.price])
