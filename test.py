from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep


def find_nexus(driver):
    driver.get("https://www.demoblaze.com/index.html")
    # login with user
    login = driver.find_element(By.XPATH, "//li/a[@id='login2']")
    sleep(5)
    login.click()
    na = driver.find_element(By.XPATH, "//input[@id='loginusername']")
    sleep(2)
    na.send_keys('Efrat0000') # send name user
    sleep(3)
    password = driver.find_element(By.XPATH, "//input[@id='loginpassword']")
    password.send_keys('123456789')  # send password of user
    click_login = driver.find_element(By.XPATH, "//div/button[@onclick='logIn()']")
    click_login.click()  # login
    sleep(5)
    # find the product to add to the cart
    products = driver.find_elements(By.XPATH, "//div/div/div/div[@id='tbodyid']/div/div/div/h4/a")
    for i in products:
        sleep(1)
        # if find the Nexus, going to the page
        if i.text == 'Nexus 6':
            i.click()
            break
    sleep(5)
    # find the Id if the product
    id_ = driver.current_url.split('=')[1]
    # find the button that addToCart
    add_nex = driver.find_element(By.XPATH, '//a[@onclick="addToCart(3)"]')
    sleep(0.5)
    add_nex.click()
    sleep(5)
    # Blows the message
    driver.switch_to.alert.dismiss()
    sleep(2)
    # move to cart
    move_cart = driver.find_element(By.ID, "cartur")
    move_cart.click()
    sleep(5)
    # find all product
    rows = driver.find_elements(By.XPATH, '//div/table/tbody/tr')
    # if have some product section e' don't met
    if len(rows) > 1:
        return False
    prod = rows[0].find_elements(By.XPATH, '//td')
    # if every got in the wagon right
    if (id_ == '3') & (prod[1].text == 'Nexus 6') & (prod[2].text == '650'):
        return True
    return False


if __name__ == '__main__':
    driver: WebDriver = webdriver.Chrome(executable_path="C:\\Users\\User\pythonProject\driver\chromedriver.exe")
    print('If section e\' is met?')
    res = find_nexus(driver)
    print(res)
    driver.close()
