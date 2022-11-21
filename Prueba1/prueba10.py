'''
Created on 25 oct 2022

@author: zorro
'''

from sys import exit
import os
os.chdir(r"C:\Users\zorro\Desktop\experimentos")
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import wget

def buscarPersona(driver):
    print("escriba el nombre de la persona que busca")
    nombre=input()
    driver.find_element(By.XPATH, "//input[@placeholder='Search Facebook']").send_keys(nombre)
    driver.find_element(By.CSS_SELECTOR, ".x6ikm8r > strong").click()
    
    datos=driver.find_elements(By.CLASS_NAME, "x1lliihq x6ikm8r x10wlt62 x1n2onr6")
    for dato in datos:
        print(dato.find_element(By.XPATH,"//a[@role = 'presentation']"))
        
        
def bajaHastaAbajo():
    last_height = driver.execute_script("return document.body.scrollHeight")
    cont=0
    while cont<20:
        SCROLL_PAUSE_TIME = 0.5
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        cont=cont+1
        

def busca_amigos(driver):
    driver.get(driver.current_url+"/allende.camaracarrasco/friends")
    #bajaHastaAbajo()
    cont=1
    while(cont<3):
        nombre=driver.find_element(By.CSS_SELECTOR, ".x6s0dn4:nth-child({}) .x1i10hfl > .x193iq5w".format(cont)).text
        #para conseguir la foto de perfil del amigo
        #foto=driver.find_element(By.CSS_SELECTOR, ".x6s0dn4:nth-child({}) .x1lq5wgf:nth-child(2)".format(cont))
        print(nombre)
        cont=cont+1
        
def busca_fotos(driver):
    if not os.path.exists("fotos"):
            os.mkdir("fotos")
    driver.get(driver.current_url+"/martin5gomez/photos")
    driver.find_element(By.CSS_SELECTOR, ".x9f619:nth-child(1) > .xqtp20y .xzg4506").click()
    cont=0
    while(cont<5):
        foto=driver.find_element(By.CSS_SELECTOR,"img").get_attribute("src")
        wget.download(foto,"fotos")
        #driver.find_element(By.CSS_SELECTOR, ".x6s0dn4:nth-child(3) .x1b0d499").click()
        cont=cont+1
        
        
def busca_info(driver):
    
    driver.get(driver.current_url+"/joaquincasado14/about")
    print("\n")
    print("Información personal general")
    #donde trabaja
    print(driver.find_element(By.CSS_SELECTOR, ".x1hq5gj4 .x9f619 > .x9f619 > .x193iq5w").text)
    #donde estudió
    print(driver.find_element(By.CSS_SELECTOR, ".x1hq5gj4:nth-child(2) .xzsf02u > .x193iq5w").text)
    #donde vive
    print(driver.find_element(By.CSS_SELECTOR, ".x1hq5gj4:nth-child(3) .xzsf02u > .x193iq5w").text)
    #donde nació
    print(driver.find_element(By.CSS_SELECTOR, ".x1hq5gj4:nth-child(4) .xzsf02u > .x193iq5w").text)
    #tiene una relación?
    print(driver.find_element(By.CSS_SELECTOR, ".x12nagc > .xo1l8bm").text)
    
    
def login(email, password):
    """ Logging into our own profile """
   
    try:
        global driver
        options = Options()
        #  Code to disable notifications pop up of Chrome Browser
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--mute-audio")
        # options.add_argument("headless")
        try:
            driver = webdriver.Chrome(executable_path=r"C:\Users\zorro\AppData\Local\Programs\Python\Python310\Lib\site-packages\selenium\chromedriver.exe", options=options)
            print("you logged in. Let's rock")
        except:
            print("you need web driver!")
            exit()

        #driver.get("https://en-gb.facebook.com")
        driver.get("https://facebook.com")
        
        #driver.maximize_window()
        # filling the form

        driver.find_element(By.CSS_SELECTOR,"._9xo5 ._9xo7").click()
        driver.find_element(By.XPATH, "//input[@placeholder='Correo electrónico o número de teléfono']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@placeholder='Contraseña']").send_keys(password)
        # clicking on login button

        driver.find_element(By.NAME,"login").click()
        
        #buscarPersona(driver)
        #busca_amigos(driver)--ya funciona
        #busca_fotos(driver)--casi funciona
        #busca_info(driver)--falta completar
        
    except:
        print("maybe something is wrong")
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

def main():
    
    with open('credentials.txt') as f:
        email = f.readline().split('"')[1]
        password = f.readline().split('"')[1]

        if email == "" or password == "":
            print("Your email or password is missing. Kindly write them in credentials.txt")
            exit()

    ids = ["https://facebook.com/" + line.split("/")[-1] for line in open("input.txt", newline='\n')]
    if len(ids) > 0:
        print("\nStarting Scraping...")
        login(email, password)
       # time.sleep(5)
       # print(ids)
        #driver.get(ids[0])
       # driver.close()
    else:
        print("Input file is empty.")


# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------

if __name__ == '__main__':
    # Let's begin
    main()