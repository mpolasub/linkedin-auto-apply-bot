from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException



# keep chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create & configure the chrome webdriver
driver = webdriver.Chrome(options=chrome_options)


def apply_for_job(job_item):
    link = job_item.get_attribute('href')
    print(link)
    time.sleep(3)


# navigate to LinkedIn
driver.get("https://www.linkedin.com/jobs/search/"
           "?currentJobId=3786715581&distance=25.0"
           "&f_AL=true&geoId=103644278"
           "&keywords=software%20developer%20intern"
           "&origin=JOB_SEARCH_PAGE_JOB_FILTER")

time.sleep(2)
sign_in_button = driver.find_element(By.CLASS_NAME, value="nav__button-secondary")
sign_in_button.click()

time.sleep(1)
email_box = driver.find_element(By.NAME, value="session_key")
email_box.send_keys(USERNAME)

password_box = driver.find_element(By.NAME, value="session_password")
password_box.send_keys(PASSWORD, Keys.ENTER)

job_list = driver.find_elements(By.CSS_SELECTOR, value=".scaffold-layout__list-container li .job-card-container [href]")
print(job_list)

for job in job_list:
    apply_for_job(job)

#ember178#ember178