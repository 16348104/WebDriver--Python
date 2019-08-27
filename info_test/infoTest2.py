import time

from selenium import webdriver
from public2 import LoginInfo


class LoginTest():
    def __init__(self):
        self.driver = webdriver.Chrome()
        # driver = webdriver.Firefox()
        # driver = webdriver.Safari() #Mac os
        self.driver.get('http://infoen.syx.thcic.cn')
        # driver.get('http://101.6.28.150:29009')
        # self.driver.get('http://eng.info.tisnghua.edu.cn')
        self.driver.maximize_window()
        time.sleep(2)
        # driver.set_window_size(1080*760)
        # self.driver.implicitly_wait(10)

    # 教师登录
    def test_admin_login(self):
        username = '2011990118'
        password = 'a123456'
        LoginInfo().user_login(self.driver, username, password)
        time.sleep(2)

    # 本科登录
    def test_bachelor_login(self):
        username = '2017013478'
        password = 'a123456'
        LoginInfo().user_login(self.driver, username, password)

    # 硕士登录
    def test_master_login(self):
        username = '2017013478'
        password = 'a123456'
        LoginInfo().user_login(self.driver, username, password)

    # 退出系统
    def test_logout(self):
        username = '2017013478'
        password = 'a123456'
        LoginInfo().user_login(self.driver, username, password)
        time.sleep(5)
        # LoginInfo().user_login(self.driver)



# 执行测试
# LoginTest().test_admin_login()
# LoginTest().test_bachelor_login()
LoginTest().test_logout()
