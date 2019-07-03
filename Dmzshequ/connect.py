import time
from selenium import webdriver

# browser = webdriver.Firefox()
# # browser = webdriver.Ie()
browser = webdriver.Chrome()
browser.get('https://net.tsinghua.edu.cn')
browser.maximize_window()
time.sleep(2)


# 连接校园网
def login(user, password):
    browser.find_element_by_id('uname').send_keys(user)
    browser.find_element_by_id('pass').send_keys(password)
    browser.find_element_by_id('connect').click()


login('', "")
time.sleep(1)
print(browser.switch_to.alert.text)
browser.switch_to.alert.accept()
time.sleep(100)
# 断网
browser.refresh()
time.sleep(1)
js = "window.do_logout();"
browser.execute_script(js)
time.sleep(1)
print(browser.switch_to.alert.text)
browser.switch_to.alert.accept()
