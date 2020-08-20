from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import randint

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
    

def like_pics_of(hashtag):
    driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
    time.sleep(3)
    # Logo abaixo você pode costumizar quantas vezes deseja que a página role para baixo
    # Quanto mais vezes for, mais fotos o bot irá coletar
    for i in range(0, 5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        i += 1

    hrefs = driver.find_elements_by_tag_name("a")
    pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
    print(hashtag + " fotos: " + str(len(pic_hrefs)))

    for pic_href in pic_hrefs:
        driver.get(pic_href)
        time.sleep(3)
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.find_element_by_xpath(
                '//span [@class="fr66n"]').click()
            time.sleep(randint(15, 30))
        except Exception as e:
            print(e)
            time.sleep(2)


# Insira abaixo o seu usuário e senha
login('usuario', 'senha')
# Insira a hashtag que deseja
like_pics_of('hashtag')
