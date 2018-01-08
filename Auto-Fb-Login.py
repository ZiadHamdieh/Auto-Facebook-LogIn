from selenium import webdriver
import config

browser = webdriver.Firefox()

email = config.email
pw = config.password

## open browser & navigate to www.facebook.com
browser.get('https://www.facebook.com')
assert "Facebook" in browser.title

## find email & password fields, and send keys to them
email_field = browser.find_element_by_id('email')
email_field.send_keys(email)

password_field = browser.find_element_by_id('pass')
password_field.send_keys(pw)

## find login button and click it
login_button = browser.find_element_by_xpath("//input[@id='u_0_2']")
login_button.click()
assert "Facebook" in browser.title



