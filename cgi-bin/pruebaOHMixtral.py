from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
# Usa el controlador de webdriver correspondiente al navegador que estás usando. En este caso, Chrome.
driver = webdriver.Chrome()

# Abre la primera página en una nueva ventana del navegador.
driver.get('paginaPrincipal.html')

# Intenta encontrar el formulario y completarlo con datos de prueba.
nombre = driver.find_element(By.NAME, 'nombre')
contrasena = driver.find_element(By.NAME, 'contrasena')
boton = driver.find_element(By.NAME, 'ok')
nombre.send_keys('prueba')
contrasena.send_keys('prueba')
sleep(5)
boton.click()

# Espera que la siguiente página se cargue y luego busca el segundo botón.
driver.implicitly_wait(10) # Tiempo en segundos para que el script espere antes de lanzar un error
segundo_boton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'boton2')))
sleep(5)
# Haz clic en el segundo botón y espera que la última página se cargue.
segundo_boton.click()
WebDriverWait(driver, 10).until(EC.title_contains('Enhorabuena!'))

# Imprime el título de la última página en consola y cierra el navegador.
print(driver.title)
driver.quit()