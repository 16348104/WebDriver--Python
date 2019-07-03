import time
from selenium import webdriver

# browser = webdriver.Firefox()
# # browser = webdriver.Ie()
browser = webdriver.Chrome()
browser.get('https://net.tsinghua.edu.cn')
browser.maximize_window()
time.sleep(2)
print("联接校园网！")


def login(user, password):
    browser.find_element_by_id('uname').send_keys(user)
    browser.find_element_by_id('pass').send_keys(password)
    browser.find_element_by_id('connect').click()


login('', "")
try:
    print(browser.switch_to.alert.text)
    browser.switch_to.alert.accept()
except BaseException:
    pass
# browser.get('http://net.tsinghua.edu.cn')
time.sleep(10)
js = "window.do_logout();"
browser.execute_script(js)
print(browser.switch_to.alert.text)
browser.switch_to.alert.accept()
