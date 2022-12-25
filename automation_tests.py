import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://192.168.99.100:5000/')
driver.implicitly_wait(5)

# R1

# driver.find_element_by_css_selector('div > a:nth-child(3)').click()
# email = driver.find_element_by_css_selector('[name="email"]')
# email.send_keys('1234@gmail.com')
# name = driver.find_element_by_css_selector('[name="name"]')
# name.send_keys('Ivan')
# password = driver.find_element_by_css_selector('[name="password"]')
# password.send_keys('1234')
# driver.find_element_by_class_name('is-fullwidth').click()


# R2

# driver.find_element_by_css_selector('div > a:nth-child(3)').click()
# email = driver.find_element_by_css_selector('[name="email"]')
# email.send_keys('1234@gmail.com')
# name = driver.find_element_by_css_selector('[name="name"]')
# name.send_keys('Ivan')
# password = driver.find_element_by_css_selector('[name="password"]')
# password.send_keys('1234')
# driver.find_element_by_class_name('is-fullwidth').click()


# R3

# driver.find_element_by_css_selector('div > a:nth-child(3)').click()
# email = driver.find_element_by_css_selector('[name="email"]')
# email.send_keys('1234@gmail.com')
# name = driver.find_element_by_css_selector('[name="name"]')
# name.send_keys('Anton')
# password = driver.find_element_by_css_selector('[name="password"]')
# password.send_keys('1234')
# driver.find_element_by_class_name('is-fullwidth').click()


# R4

# driver.find_element_by_css_selector('div > a:nth-child(3)').click()
# email = driver.find_element_by_css_selector('[name="email"]')
# email.send_keys('1234@gmail.com')
# name = driver.find_element_by_css_selector('[name="name"]')
# name.send_keys('Ivan')
# password = driver.find_element_by_css_selector('[name="password"]')
# password.send_keys('4321')
# driver.find_element_by_class_name('is-fullwidth').click()


# R5

# driver.find_element_by_css_selector('div > a:nth-child(3)').click()
# driver.find_element_by_class_name('is-fullwidth').click()


# R6

# driver.find_element_by_css_selector('div > a:nth-child(3)').click()
# email = driver.find_element_by_css_selector('[name="email"]')
# email.send_keys('12345@gmail.com')
# password = driver.find_element_by_css_selector('[name="password"]')
# password.send_keys('1234')
# driver.find_element_by_class_name('is-fullwidth').click()


# R7

# driver.find_element_by_css_selector('div > a:nth-child(3)').click()
# email = driver.find_element_by_css_selector('[name="email"]')
# email.send_keys('123456@gmail.com')
# name = driver.find_element_by_css_selector('[name="name"]')
# name.send_keys('Viktor')
# driver.find_element_by_class_name('is-fullwidth').click()


# R8

# driver.find_element_by_css_selector('div > a:nth-child(3)').click()
# name = driver.find_element_by_css_selector('[name="name"]')
# name.send_keys('Alex')
# password = driver.find_element_by_css_selector('[name="password"]')
# password.send_keys('1234')
# driver.find_element_by_class_name('is-fullwidth').click()


# R9

# driver.find_element_by_css_selector('div > a:nth-child(3)').click()
# email = driver.find_element_by_css_selector('[name="email"]')
# email.send_keys('12345')
# name = driver.find_element_by_css_selector('[name="name"]')
# name.send_keys('Viktor')
# password = driver.find_element_by_css_selector('[name="password"]')
# password.send_keys('1234')
# driver.find_element_by_class_name('is-fullwidth').click()


# R10

# driver.find_element_by_css_selector('div > a:nth-child(3)').click()
# email = driver.find_element_by_css_selector('[name="email"]')
# email.send_keys("123123!'№;%:?*()+=\/,@#$^&{}[]><@gmail.com")
# name = driver.find_element_by_css_selector('[name="name"]')
# name.send_keys('Viktor')
# password = driver.find_element_by_css_selector('[name="password"]')
# password.send_keys('1234')
# driver.find_element_by_class_name('is-fullwidth').click()
# email.clear()
# email.send_keys("123123!%?*+=/`~@gmail.com")
# driver.find_element_by_class_name('is-fullwidth').click()


# R11

# driver.find_element_by_css_selector('div > a:nth-child(3)').click()
# email = driver.find_element_by_css_selector('[name="email"]')
# email.send_keys("123123@gmail!'№;%:?*()+=\/,@#$^&{}[]><.com")
# name = driver.find_element_by_css_selector('[name="name"]')
# name.send_keys('Viktor')
# password = driver.find_element_by_css_selector('[name="password"]')
# password.send_keys('1234')
# driver.find_element_by_class_name('is-fullwidth').click()
# email.clear()
# email.send_keys("123123@gmail.com")
# driver.find_element_by_class_name('is-fullwidth').click()


# R12

# driver.find_element_by_css_selector('div > a:nth-child(3)').click()
# email = driver.find_element_by_css_selector('[name="email"]')
# email.send_keys('0123йцукенгшщзхъфывапролджэячсмитьбю@gmail.com')
# name = driver.find_element_by_css_selector('[name="name"]')
# name.send_keys('Viktor')
# password = driver.find_element_by_css_selector('[name="password"]')
# password.send_keys('1234')
# driver.find_element_by_class_name('is-fullwidth').click()
# email.clear()
# email.send_keys("0123@gmail.com")
# driver.find_element_by_class_name('is-fullwidth').click()


# R13

# driver.find_element_by_css_selector('div > a:nth-child(3)').click()
# email = driver.find_element_by_css_selector('[name="email"]')
# email.send_keys('0234@gmaiйцукенгшщзхъфывапролджэячсмитьбюl.com')
# name = driver.find_element_by_css_selector('[name="name"]')
# name.send_keys('Viktor')
# password = driver.find_element_by_css_selector('[name="password"]')
# password.send_keys('1234')
# driver.find_element_by_class_name('is-fullwidth').click()
# email.clear()
# email.send_keys("0234@gmail.com")
# driver.find_element_by_class_name('is-fullwidth').click()


# R14

# driver.find_element_by_css_selector('div > a:nth-child(3)').click()
# email = driver.find_element_by_css_selector('[name="email"]')
# email.send_keys('ABCabc@gmail.com')
# name = driver.find_element_by_css_selector('[name="name"]')
# name.send_keys('Ivan')
# password = driver.find_element_by_css_selector('[name="password"]')
# password.send_keys('abcd')
# driver.find_element_by_class_name('is-fullwidth').click()


# R15

# driver.find_element_by_css_selector('div > a:nth-child(3)').click()
# email = driver.find_element_by_css_selector('[name="email"]')
# email.send_keys('ABabc@GmAil.com')
# name = driver.find_element_by_css_selector('[name="name"]')
# name.send_keys('Viktor')
# password = driver.find_element_by_css_selector('[name="password"]')
# password.send_keys('4321')
# driver.find_element_by_class_name('is-fullwidth').click()


# L1

# driver.find_element_by_css_selector('div > a:nth-child(2)').click()
# email = driver.find_element_by_css_selector('[name="email"]')
# email.send_keys('1234@gmail.com')
# password = driver.find_element_by_css_selector('[name="password"]')
# password.send_keys('1234')
# driver.find_element_by_class_name('is-fullwidth').click()


# L2

# driver.find_element_by_css_selector('div > a:nth-child(2)').click()
# email = driver.find_element_by_css_selector('[name="email"]')
# email.send_keys('1234@gmail.com')
# password = driver.find_element_by_css_selector('[name="password"]')
# password.send_keys('5678')
# driver.find_element_by_class_name('is-fullwidth').click()


# L3

# driver.find_element_by_css_selector('div > a:nth-child(2)').click()
# email = driver.find_element_by_css_selector('[name="email"]')
# email.send_keys('12345678@gmail.com')
# password = driver.find_element_by_css_selector('[name="password"]')
# password.send_keys('1234')
# driver.find_element_by_class_name('is-fullwidth').click()


# L4

# driver.find_element_by_css_selector('div > a:nth-child(2)').click()
# driver.find_element_by_class_name('is-fullwidth').click()


# L5

# driver.find_element_by_css_selector('div > a:nth-child(2)').click()
# email = driver.find_element_by_css_selector('[name="email"]')
# email.send_keys('1234@gmail.com')
# driver.find_element_by_class_name('is-fullwidth').click()


# L6

# driver.find_element_by_css_selector('div > a:nth-child(2)').click()
# email = driver.find_element_by_css_selector('[name="email"]')
# email.send_keys('1122345678@gmail.com')
# driver.find_element_by_class_name('is-fullwidth').click()


# L7

# driver.find_element_by_css_selector('div > a:nth-child(2)').click()
# password = driver.find_element_by_css_selector('[name="password"]')
# password.send_keys('1234')
# driver.find_element_by_class_name('is-fullwidth').click()


# L8

# driver.find_element_by_css_selector('div > a:nth-child(2)').click()
# email = driver.find_element_by_css_selector('[name="email"]')
# email.send_keys('ABC@GMAIL.COM')
# password = driver.find_element_by_css_selector('[name="password"]')
# password.send_keys('1234')
# driver.find_element_by_class_name('is-fullwidth').click()


# L9

# driver.find_element_by_css_selector('div > a:nth-child(2)').click()
# email = driver.find_element_by_css_selector('[name="email"]')
# email.send_keys('ABCabc@gmail.com')
# password = driver.find_element_by_css_selector('[name="password"]')
# password.send_keys('ABCD')
# driver.find_element_by_class_name('is-fullwidth').click()


time.sleep(4)
driver.quit()