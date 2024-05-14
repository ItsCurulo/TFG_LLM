from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Optional, runs the browser in the background
driver = webdriver.Chrome(options=options)

# Navigate to Google and perform a search
driver.get("https://www.google.com")
search_box = driver.find_element_by_name("q")
search_box.send_keys("selenium python tutorial")
search_box.submit()

# Wait for the search results to load and click on the first result
time.sleep(5)  # Adjust the wait time as needed
first_result = driver.find_element_by_xpath('//div[@class="BNeawe s3v9rd AP7Wnd"]/c-wiz/div/div/a')
first_result.click()

# Optional: close the browser window after some delay
time.sleep(10)  # Adjust the wait time as needed
driver.close()