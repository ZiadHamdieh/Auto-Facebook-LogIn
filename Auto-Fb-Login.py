from selenium import webdriver

browser = webdriver.Firefox()

usr = input('Enter username/email: ')
pw = input('enter password')

## open browser & navigate to www.facebook.com
browser.get('https://www.facebook.com')
assert "Facebook" in browser.title

## find username & password fields, and send keys to them
username_field = browser.find_element_by_id('email')
username_field.send_keys(usr)

password_field = browser.find_element_by_id('pass')
password_field.send_keys(pw)

## find login button and click it
login_button = browser.find_element_by_xpath("//input[@id='u_0_2']")
login_button.click()
assert "Facebook" in browser.title



