from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
# Ubica la ubicación de tu ChromeDriver
driver = webdriver.Chrome()

ruta=os.path.dirname(os.path.abspath(__file__))

ruta_pagina_principal = os.path.join(ruta, '../paginaUnica.html')
# Abre la primera página en una nueva ventana del navegador.

if not os.path.exists(ruta_pagina_principal):
    print("File not found:", ruta_pagina_principal)
    exit
# Abre la página HTML
driver.get('file://'+ ruta_pagina_principal)

# Wait for the title of the page to contain 'Mi primera página web interactiva'
WebDriverWait(driver, 10).until(EC.title_contains("Mi primera página web interactiva"))

# Verify that the page contains the expected text
expected_text = "¡Has hecho clic en el botón!"
print("Page title:", driver.title)
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "mensaje")))
    print("Mensaje texto:", element.text)
    assert expected_text in element.text
except AssertionError:
    print(f"No se encontró el mensaje '{expected_text}'")

# Click the button
button = driver.find_element(By.ID, "boton")
button.click()

# Wait for the message to appear and then verify its content
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "mensaje")))
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "mensaje")))
    print("Mensaje texto después de hacer clic:", element.text)
    assert expected_text in element.text
except AssertionError:
    print(f"No se encontró el mensaje '{expected_text}' después de hacer clic")

# Close the browser
driver.quit()