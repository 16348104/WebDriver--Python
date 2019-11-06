import time
import os
from selenium import webdriver

# browser = webdriver.Firefox()
browser = webdriver.Ie(executable_path='E:\Program Files\Python\Python37\IEDriverServer.exe')
# browser = webdriver.Chrome()
browser.get('https://net.tsinghua.edu.cn')
browser.maximize_window()
time.sleep(2)


# 连接校园网
def login(user, password):
    browser.find_element_by_id('uname').send_keys(user)
    browser.find_element_by_id('pass').send_keys(password)
    # browser.find_element_by_id('connect').click()
    time.sleep(1)
    js_connect = 'do_login();'
    browser.execute_script(js_connect)
    time.sleep(1)
    print(browser.switch_to.alert.text)
    browser.switch_to.alert.accept()


try:
    login('', "")
except BaseException:
    print('已连网')
time.sleep(2)
date = browser.find_element_by_xpath('//*[@id="usage_flux"]').text
print(date)
os.system("E:/163study/WebDriver--Python/Example/Email/send_mail.py")
print("连网中")
browser.minimize_window()
time.sleep(120)
# 断网
time.sleep(1)
js_disconnect = "do_logout();"
browser.execute_script(js_disconnect)
time.sleep(1)
print(browser.switch_to.alert.text)
browser.switch_to.alert.accept()
time.sleep(2)
browser.quit()
