from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Inicializa el navegador
driver =  webdriver.Chrome() 
# Abre la página web
url = "file:///C:/Users/carlo/OneDrive/Escritorio/TFG/pagina.html"
driver.get(url)

# Llena el formulario y envía los datos
name_field = driver.find_element(By.NAME,'name')
name_field.send_keys('John Doe')

email_field = driver.find_element(By.NAME,'email')
email_field.send_keys('johndoe@example.com')

message_field = driver.find_element(By.NAME,'message')
message_field.send_keys('Hola, esto es un mensaje de prueba.')

submit_button = driver.find_element(By.XPATH,'//button[@type="submit"]')
sleep(50)
submit_button.click()
driver.quit()