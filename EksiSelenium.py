from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


with open('eksisozluk.csv', 'w') as f:
    f.write("Yorum , Yazar, Tarih \n")

USER = 'USERNAME' //can be anything
PASS = 'PASSWORD'  //can be anything
searchitem = 'koronavirüs'

driver_path = '/home/faik/chromedriver_linux64/chromedriver'

driver = webdriver.Chrome(driver_path)

driver.get('https://eksisozluk.com/')

LoginXpath = "//a[@id='top-login-link']"
UsernameXpath = "//input[@id='username']"
PasswordXpath = "//input[@id='password']"
ButtonXpath = "//button[@class='btn btn-primary btn-lg btn-block']"
SearchXpath = "//input[@id='search-textbox']"
SearchButtonXpath = "//form[@id='search-form']//button"
NextPageCSS = '.next'

LoginElement = WebDriverWait(driver, 60).until(lambda driver: driver.find_element_by_xpath(LoginXpath))
LoginElement.click()

UsernameElement = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, UsernameXpath)))
UsernameElement.click()
UsernameElement.send_keys(USER)

PasswordElement = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, PasswordXpath)))
PasswordElement.send_keys(PASS)

ButtonElement = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, ButtonXpath)))
ButtonElement.click()

SearchElement = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, SearchXpath)))
SearchElement.send_keys(searchitem)

SearchButtonElement = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, SearchButtonXpath)))
SearchButtonElement.click()

max_page_num = 153
for i in range(1, max_page_num + 1):
    url = "https://eksisozluk.com/koronavirus--6335395?p=" + str(i) + "/"
    driver.get(url)

    yorum = driver.find_elements_by_css_selector('.content')
    yazar = driver.find_elements_by_css_selector('.entry-author')
    tarih = driver.find_elements_by_css_selector('.permalink')

    num_yorum = len(yorum)
    with open('eksisozluk.csv', 'a') as f:
        for i in range(num_yorum):
            f.write(yorum[i].text + ", " + yazar[i].text + ", " + tarih[i].text + "\n")


sleep(15)
driver.close()

