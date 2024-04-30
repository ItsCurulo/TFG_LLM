from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

# Configuración del ChromeDriver
driver = webdriver.Chrome()

ruta=os.path.dirname(os.path.abspath(__file__))

ruta_pagina_principal = os.path.join(ruta, '../paginaPrincipal.html')
# Abre la primera página en una nueva ventana del navegador.

if not os.path.exists(ruta_pagina_principal):
    print("File not found:", ruta_pagina_principal)
    exit

driver.get('file://'+ ruta_pagina_principal)

# Espera hasta que el elemento 'nombre' esté presente en la página
nombre = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'nombre')))

# Completa el formulario con datos de prueba.
contrasena = driver.find_element(By.NAME, 'contrasena')
boton = driver.find_element(By.NAME, 'ok')
nombre.send_keys('prueba')
contrasena.send_keys('prueba')
sleep(5)
boton.click()

# Espera que la siguiente página se cargue y luego busca el segundo botón.
segundo_boton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'boton2')))
sleep(5)

# Haz clic en el segundo botón y espera que la última página se cargue.
segundo_boton.click()
WebDriverWait(driver, 10).until(EC.title_contains('Enhorabuena'))

# Imprime el título de la última página en consola y cierra el navegador.
print(driver.title)
driver.quit()
