import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
#wait=WebDriverWait(driver,50)

# 1- Se connecter au site : https://videotron.com/
driver.get("https://videotron.com/")

time.sleep(4)
print("---------------------------------------------------------------------------------------")

# 2-Trouver le nombre d’images sur le site et l’afficher dans la console de votre éditeur de code.
image=driver.find_elements(By.TAG_NAME, "img")
print("le nombre d'images est égale à : ", len(image))
print()

# 3- Afficher la valeur de l’attribut « alt » des images du site dans la console.
j=1
for i in image:
    #driver.find_element(By.XPATH, "//img[@alt]")
    alt = i.get_attribute("alt")
    if alt=="":
        print( "Image no", j ,"n'a pas de alt")
    else:
        print( "Image no", j ,"======== alt : ", alt)
    j+=1
print()
print("---------------------------------------------------------------------------------------")
print()
# 4- Trouver le nombre de liens sur le site et l’afficher dans la console.

liste_liens=driver.find_elements(By.TAG_NAME,"a")
print("le nombre de liens sur toute la page est égale à : ", len(liste_liens))

# 5- Trouver le nombre de liens dans la section « footer » du site et l’afficher dans la console.

footer=driver.find_element(By.TAG_NAME,"footer")
liens_footer=footer.find_elements(By.TAG_NAME,"a")
print("le nombre de liens dans le footer est égale à : ", len(liens_footer))
print()
# 6- Récupérer la valeur de l’attribut « href » de chaque lien dans la section « footer » du site et l’afficher dans la console.
j=1
for i in liens_footer:
    #driver.find_element(By.XPATH, "//img[@alt]")
    href = i.get_attribute("href")
    print( "Le lien no", j ,"--------- href : ", href)
    j += 1


driver.quit()