from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

firefoxProfile = webdriver.FirefoxProfile()
firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
firefoxProfile.set_preference("dom.webnotifications.enabled", False)
driver = webdriver.Firefox(
    firefox_profile=firefoxProfile, executable_path=r"C:\Users\ACER\OneDrive\Documentos\MeusProjetos\insta-bot\geckodriver.exe"
)
driver.get('https://www.instagram.com')
time.sleep(3)


def login(username, password):
    username_input = driver.find_element_by_xpath(
            "//input[@name='username']")
    username_input.clear()
    username_input.send_keys(username)
    time.sleep(3)
    password_input = driver.find_element_by_xpath(
        "//input[@name='password']")
    password_input.clear()
    password_input.send_keys(password)
    time.sleep(3)
    password_input.send_keys(Keys.RETURN)
    time.sleep(3)
    

def like_pics_of(ig):
    driver.get("https://www.instagram.com/"+ ig +"/")
    time.sleep(3)
    followers = driver.find_element_by_class_name('-nal3 ')
    time.sleep(1)
    followers.click()


login('usuario', 'senha')
like_pics_of('perfil que deseja analisar')
