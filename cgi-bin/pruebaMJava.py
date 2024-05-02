from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
# Reemplaza 'path/to/chromedriver' con la ruta real del ejecutable del navegador que estás utilizando (por ejemplo, ChromeDriver.exe para Google Chrome).
driver = webdriver.Chrome()

ruta=os.path.dirname(os.path.abspath(__file__))

ruta_pagina_principal = os.path.join(ruta, '../paginaPrincipalJava.html')
# Abre la primera página en una nueva ventana del navegador.

if not os.path.exists(ruta_pagina_principal):
    print("File not found:", ruta_pagina_principal)
    exit



try:
    driver.get('file://'+ ruta_pagina_principal)  # Reemplaza 'https://your-url-here.com' con la URL de la página que deseas probar

    # Espera a que se muestre el formulario de registro
    form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'registroForm')))

    # Llena el formulario y envía la solicitud
    nombre = form.find_element_by_id('nombre')
    nombre.send_keys('Tu nombre aquí')  # Reemplaza con tu nombre real

    contrasenia = form.find_element_by_id('contrasenia')
    contrasenia.send_keys('Contraseña1234!')  # Reemplaza con la contraseña que deseas probar

    form.submit()

except TimeoutException:
    print("No se pudo encontrar el formulario de registro")

finally:
    driver.quit()