from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

USERNAME = "#@gmail.com"
PASSWORD = "#"
STREET = "#"
CITY = "#, #, #"
STATE = "#"

# keep chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create & configure the chrome webdriver
driver = webdriver.Chrome(options=chrome_options)


def fill_address(header):
        street = driver.find_element(By.ID,
                                     value="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3807769738-6496872757593706718-text")
        city = driver.find_element(By.ID,
                                   value="single-typeahead-entity-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3807769738-6650951340736869074-city-HOME-CITY")
        state = driver.find_element(By.ID,
                                    value="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3807769738-1694117591222500277-text")
        street.send_keys(STREET)
        city.send_keys(CITY)
        state.send_keys(STATE)


def get_job(job_item):
    link = job_item.get_attribute('href')
    if "www.linkedin.com" in link:
        job_item.click()
        time.sleep(2)
        apply_button = driver.find_element(By.CLASS_NAME, value="jobs-apply-button")
        apply_button.click()

        time.sleep(2)

        next_button = driver.find_element(By.CSS_SELECTOR, value="[aria-label='Continue to next step']")
        next_button.click()

        header = driver.find_element(By.CSS_SELECTOR, value="h3")
        while header.text != "Review your application":
            next_button = driver.find_element(By.CSS_SELECTOR, value="[aria-label='Continue to next step']")
            if header.text == "Home address":
                fill_address(header)
            next_button.click()
            header = driver.find_element(By.CSS_SELECTOR, value="h3")

        time.sleep(2)
        review_button = driver.find_element(By.CSS_SELECTOR, value="[aria-label='Review your application']")
        review_button.click()

        time.sleep(2)
        submit_button = driver.find_element(By.CSS_SELECTOR, value="[aria-label='Submit application']")
        submit_button.click()

        time.sleep(2)
        dismiss_button = driver.find_element(By.CSS_SELECTOR, value="[aria-label='Dismiss']")
        dismiss_button.click()

        time.sleep(2)
        dismiss_job_button = driver.find_element(By.CSS_SELECTOR, value="[aria-label='Dismiss job']")
        dismiss_job_button.click()

        time.sleep(2)


# navigate to LinkedIn
driver.get("https://www.linkedin.com/jobs/search/"
           "?currentJobId=3760383701&distance=25.0"
           "&f_AL=true&f_E=1&geoId=103644278"
           "&keywords=software%20developer%20intern"
           "&origin=JOB_SEARCH_PAGE_JOB_FILTER")

time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in_button.click()

time.sleep(1)
email_box = driver.find_element(By.NAME, value="session_key")
email_box.send_keys(USERNAME)

password_box = driver.find_element(By.NAME, value="session_password")
password_box.send_keys(PASSWORD, Keys.ENTER)

job_list = driver.find_elements(By.CSS_SELECTOR, value=".scaffold-layout__list-container li .job-card-container [href]")
print(job_list)

for job in job_list:
    get_job(job)

#ember178#ember178