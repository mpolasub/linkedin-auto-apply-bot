from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create & configure the chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# navigate to LinkedIn
driver.get("https://www.linkedin.com/home")