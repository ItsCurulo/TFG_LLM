
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# URL de la página web
url = "file:///C:/Users/carlo/OneDrive/Escritorio/TFG/pagina.html"

# Abrir el navegador Chrome
driver = webdriver.Chrome()

# Acceder a la página web
driver.get(url)

# Localizar el elemento del formulario: nombre
nombre_input = driver.find_element(By.ID, "name")

# Introducir nombre
nombre_input.send_keys("John Doe")

# Localizar el elemento del formulario: email
email_input = driver.find_element(By.ID, "email")

# Introducir email
email_input.send_keys("johndoe@example.com")

# Localizar el elemento del formulario: mensaje
mensaje_input = driver.find_element(By.ID, "message")

# Introducir mensaje
mensaje_input.send_keys("Este es un mensaje de prueba.")

# Localizar el botón "Enviar"
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
sleep(50)
# Hacer clic en el botón "Enviar"
submit_button.click()

# Cerrar el navegador
driver.quit()