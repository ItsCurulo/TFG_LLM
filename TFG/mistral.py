from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
# Inicializa el navegador
driver = webdriver.Chrome()

# Abre la primera página y rellena el formulario
driver.get('file:///C:/Users/carlo/OneDrive/Escritorio/TFG/pagina2.html')
name_field = driver.find_element(By.ID, 'name')
name_field.send_keys('Tu nombre aquí')
sleep(50)
submit_button = driver.find_element(By.TAG_NAME, 'input').click()

# Espera a que se cargue la segunda página
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))

# Muestra el mensaje de enhorabuena y cierra el navegador
print(driver.find_element(By.TAG_NAME, 'h1').text)
driver.close()