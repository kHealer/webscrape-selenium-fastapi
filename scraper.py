from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

class GettingDataFrom:
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        def get_data(self,tag):
            self.driver.get(f"http://quotes.toscrape.com/tag/{tag}")
            WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME,"quote")))
            WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME,"text")))
            findquote = self.driver.find_elements(By.CLASS_NAME,"text")
            WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME,"author")))
            findauthor = self.driver.find_elements(By.CLASS_NAME,"author")


            texts = []
            authors = []
            for i in findquote:
                texts.append(i.text)
            for i in findauthor:
                authors.append(i.text)
            qlist = []
            
            for text, author in zip(texts, authors):
                items = {
                        'quote':text,
                        'Author':author,
                        }      
                qlist.append(items)
            return qlist
            # print(len(texts))


testArea = GettingDataFrom()
testArea.get_data('life')