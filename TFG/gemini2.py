from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# URL de la página 1
url_formulario = "file:///C:/Users/carlo/OneDrive/Escritorio/TFG/pagina2.html"

# URL de la página 2
url_enhorabuena = "file:///C:/Users/carlo/OneDrive/Escritorio/TFG/pagina3.html"

# Abrir el navegador Chrome
driver = webdriver.Chrome()

# Acceder a la página 1
driver.get(url_formulario)

# Introducir nombre
nombre_input = driver.find_element(By.ID, "nombre")
nombre_input.send_keys("John Doe")
sleep(20)

# Hacer clic en el botón "Siguiente"
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()

# Esperar a que la página 2 se cargue
sleep(20)

# Verificar la URL de la página 2
assert driver.current_url == url_enhorabuena

# Verificar el texto de la página 2
enhorabuena_text = driver.find_element(By.CSS_SELECTOR, "h1").text
assert enhorabuena_text == "¡Enhorabuena!"

# Cerrar el navegador
driver.quit()