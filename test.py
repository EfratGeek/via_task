from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.remote.webelement import WebElement


class product:
    def __init__(self, idp, name, price):
        self.name = name
        self.price = price
        self.id = idp


def find_nexus(driver):
    driver.get("https://www.demoblaze.com/index.html")
    login = driver.find_element(By.XPATH, "//li/a[@id='login2']")
    sleep(5)
    login.click()
    na = driver.find_element(By.XPATH, "//input[@id='loginusername']")
    sleep(2)
    na.send_keys('Efrat0000')
    sleep(3)
    password = driver.find_element(By.XPATH, "//input[@id='loginpassword']")
    password.send_keys('123456789')
    click_login = driver.find_element(By.XPATH, "//div/button[@onclick='logIn()']")
    click_login.click()
    sleep(5)
    # find the product to add to the cart
    products = driver.find_elements(By.XPATH, "//div/div/div/div[@id='tbodyid']/div/div/div/h4/a")
    for i in products:
        sleep(1)
        if i.text == 'Nexus 6':
            # idp_in_link = i.get_property('href')
            i.click()
            break
    sleep(5)
    id_ = driver.current_url.split('=')[1]
    add_nex = driver.find_element(By.XPATH, '//a[@onclick="addToCart(3)"]')
    sleep(0.5)
    add_nex.click()
    sleep(5)
    driver.switch_to.alert.dismiss()
    sleep(2)
    move_cart = driver.find_element(By.ID, "cartur")
    move_cart.click()
    sleep(5)
    # driver.close()


def add_prod_to_cart(driver, link):
    sleep(10)
    # driver.get(link)


if __name__ == '__main__':
    driver: WebDriver = webdriver.Chrome(executable_path="C:\\Users\\User\pythonProject\driver\chromedriver.exe")
    find_nexus(driver)

    # l_ = driver.current_url
    # print(l_)
    # driver.close()
