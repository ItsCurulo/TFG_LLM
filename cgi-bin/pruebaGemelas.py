from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
#probamos Github Actions
# Configura el navegador para usar Chrome
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)

ruta=os.path.dirname(os.path.abspath(__file__))

ruta_pagina_principal = os.path.join(ruta, '../paginaGemela1.html')
# Abre la primera página en una nueva ventana del navegador.

if not os.path.exists(ruta_pagina_principal):
    print("File not found:", ruta_pagina_principal)
    exit

driver.get('file://'+ ruta_pagina_principal)

# Abre la primera página y introduce un nombre
nombreInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "nombre")))
nombreInput.send_keys("Ejemplo de nombre")
submitButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Enviar']")))
submitButton.click()
time.sleep(2)

# Abre la segunda página y comprueba el mensaje de bienvenida
bienvenida = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[contains(., '¡Hola,')]")))
assert "Ejemplo de nombre" in bienvenida.text
print("El mensaje de bienvenida contiene el nombre introducido")

# Cierra el navegador
driver.quit()