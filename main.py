from selenium import webdriver
import time

driver = webdriver.Firefox() # choose the browser according to your type.

driver.get("https://instagram.com")


# before we start locationg element. we first need to wait for some second
# so that the page loads completely.
time.sleep(2)

username_field = driver.find_element_by_name("username")
username_field.send_keys("ENTER_YOUR_USERNAME_HERE")

password_field = driver.find_element_by_name("password")
password_field.send_keys("ENTER_YOUR_PASSWORD_HERE")

login_button = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
login_button.click()
