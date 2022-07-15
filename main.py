from selenium.webdriver.common.by import By
from google_page import GooglePage

from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.Chrome(executable_path='./chromedriver')
    browser.get(GooglePage.url)
    browser.find_element(By.XPATH, GooglePage.input).send_keys('test')
    browser.find_element(By.XPATH, GooglePage.btn_search).click()
    assert browser.find_element(By.XPATH, GooglePage.input_after_search).get_attribute('value') == 'test'
    browser.close()
