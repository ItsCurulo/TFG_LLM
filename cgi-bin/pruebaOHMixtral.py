from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Configuración del ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Esto ejecutará Chrome en modo headless, sin abrir la ventana del navegador
driver = webdriver.Chrome(options=options)

# Abre la primera página en una nueva ventana del navegador.
driver.get('paginaPrincipal.html')

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
WebDriverWait(driver, 10).until(EC.title_contains('Enhorabuena!'))

# Imprime el título de la última página en consola y cierra el navegador.
print(driver.title)
driver.quit()
