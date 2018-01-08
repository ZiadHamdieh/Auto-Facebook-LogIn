from selenium import webdriver

browser = webdriver.Firefox()
usr = input('Enter username/email: ')

## open browser & navigate to www.facebook.com
browser.get('https://www.facebook.com')

## find username & password fields
username_field = browser.get_element_by_id('email')
username_field.send_keys(usr)

password_field = browser.get_element_by_id('pw')
password_field.send_keys(pw)

browser.click('u_0_2') # click the Submit button 


