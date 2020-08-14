from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random



class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"C:\Users\ACER\OneDrive\Documentos\MeusProjetos\insta-bot\geckodriver.exe"
        )
        
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(3)
        self.curtir_fotos_de('astronomiaeciencia')


        def curtir_fotos_de(self, perfil):
            driver = self.driver
            driver.get("https://www.instagram.com/"+ perfil +"/")
            followers = driver.find_element_by_class_name('-nal3 ')
            followers.click()


        



# Entre com o usuário e senha aqui
instaBot = InstagramBot("usuario", "senha")
instaBot.login()
