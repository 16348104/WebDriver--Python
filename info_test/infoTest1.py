import time

from selenium import webdriver
from pub2 import LoginInfo
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


# 学生端
class LoginTest():
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        # Mac os
        # self.driver = webdriver.Safari()
        # self.driver = webdriver.Chrome(executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/chromedriver')  # MacOS

        # Eng_info开发环境
        # driver.get('http://101.6.28.150:29009')
        # Eng_info模拟环境
        # self.driver.get('http://infoen.syx.thcic.cn')
        # Eng_info正式环境
        self.driver.get('http://eng.info.tsinghua.edu.cn')
        self.driver.maximize_window()
        print("======进入info学生端=====")
        time.sleep(4)
        # driver.set_window_size(1080*760)
        # self.driver.implicitly_wait(10)

    # 本科生登录
    def test_bachelor_login(self):
        user = ''
        password = ''
        LoginInfo().user_login(self.driver, user, password)

    # 硕士生登录
    def test_master_login(self):
        username = '2017013478'
        password = 'a123456'
        LoginInfo().user_login(self.driver, username, password)

    # 退出系统
    def test_logout(self):
        user = '2017013478'
        password = 'a123456'
        LoginInfo().user_login(self.driver, user, password)
        time.sleep(5)
        # LoginInfo().user_login(self.driver)

    # 测试enginfo
    def test_enginfo(self):
        print('测试浏览器:' + self.driver.name)
        # driver.set_window_size(1080*760)
        print("======Forgot your password======")
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/a').click()
        time.sleep(1)
        # # 切换【第二个窗口】
        windows = self.driver.window_handles
        # # 切换到新窗口
        self.driver.switch_to.window(windows[1])
        window_2 = self.driver.current_window_handle
        print('所有句柄:', windows)
        print("当前窗口：", window_2)
        time.sleep(3)
        self.driver.close()
        # 切换到第1个窗口
        self.driver.switch_to.window(windows[0])
        window_2 = self.driver.current_window_handle
        print("当前窗口：", window_2)
        print("======登录English_info======")
        username = ''
        password = ''
        LoginInfo().user_login(self.driver, username, password)
        time.sleep(2)
        print(self.driver.find_element_by_xpath('//li[@class="name"]').text)
        print(self.driver.find_element_by_xpath('//li[@class="stuId"]').text)
        print("======Student Status======")
        self.driver.find_element_by_xpath("//*[@class='btn'][1]").click()
        time.sleep(1)
        windows = self.driver.window_handles
        # # 切换到新窗口
        self.driver.switch_to.window(windows[1])
        window_2 = self.driver.current_window_handle
        print('所有句柄:', windows)
        print("当前窗口：", window_2)
        time.sleep(3)
        self.driver.close()
        # 切换到第1个窗口
        self.driver.switch_to.window(windows[0])
        window_2 = self.driver.current_window_handle
        print("当前窗口：", window_2)
        time.sleep(1)
        print("======Edit Personal Details======")
        self.driver.find_element_by_xpath("//*[@class='btn'][2]").click()
        windows = self.driver.window_handles
        # # 切换到新窗口
        self.driver.switch_to.window(windows[1])
        window_2 = self.driver.current_window_handle
        print('所有句柄:', windows)
        print("当前窗口：", window_2)
        time.sleep(3)
        self.driver.close()
        # 切换到第1个窗口
        self.driver.switch_to.window(windows[0])
        window_2 = self.driver.current_window_handle
        print("当前窗口：", window_2)
        time.sleep(2)
        print("======Tsinghua University Information Portal======")
        link_dict = {}
        mk = len(self.driver.find_elements_by_xpath("//ul[@id='tas']/a"))
        for i in range(0, mk):
            self.driver.find_elements_by_xpath("//ul[@id='tas']/a").pop(i).click()
            time.sleep(1)
            str1 = self.driver.find_elements_by_xpath("//ul[@id='tas']/a").pop(i).text
            print(str1, "板块")
            hrefs = len(self.driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a'))
            for j in range(0, hrefs):
                # 院系
                dep = self.driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a').pop(j).text
                # colum_dep.insert(j, dep)
                # self.driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a').pop(j).click()
                # time.sleep(2)
                # # # 切换【第二个窗口】
                # windows = self.driver.window_handles
                # # # 切换到新窗口
                # self.driver.switch_to.window(windows[1])
                # print("当前窗口标题:", self.driver.title, self.driver.current_window_handle)
                # time.sleep(2)
                # date = self.driver.current_url
                # self.driver.close()
                # # 切换到第1个窗口
                # self.driver.switch_to.window(windows[0])
                # date = driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a').pop(j).get_property('href')
                # 链接
                link = self.driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a').pop(j).get_attribute('href')
                # colum_link.insert(j, link)
                link_dict.update({dep: link})
        # print(dep, ":", link)
        # LoginInfo.write_excel(self, row0, colum_dep, colum_link)
        for k, v in link_dict.items():
            print(k, ":\t", v)
        print("======Change Password======")
        # Action
        self.driver.find_element_by_xpath("//*[@class='btn btn-default dropdown-toggle']").click()
        # 鼠标滑动Change Password
        above = self.driver.find_element_by_xpath("//ul[@class='dropdown-menu']/li[1]/a")
        time.sleep(2)
        ActionChains(self.driver).move_to_element(above).perform()
        above.click()
        time.sleep(3)
        windows = self.driver.window_handles
        # # 切换到新窗口
        LoginInfo.switch_window(self, self.driver)
        # 退出
        LoginInfo.user_logout(self, self.driver)

    # 测试URL
    def test_URL(self):
        # row0 = ["模块", "院系名称", "链接"]
        row0 = ["院系名称", "链接"]
        colum_dep = []
        colum_link = []
        module = []
        # link_dict = {}
        print('测试浏览器:' + self.driver.name)
        print("======登录English_info======")
        username = ''
        password = ''
        LoginInfo().user_login(self.driver, username, password)
        time.sleep(2)
        print(self.driver.find_element_by_xpath('//li[@class="name"]').text)
        print(self.driver.find_element_by_xpath('//li[@class="stuId"]').text)
        print("======Tsinghua University Information Portal======")
        mk = len(self.driver.find_elements_by_xpath("//ul[@id='tas']/a"))
        for i in range(0, mk):
            self.driver.find_elements_by_xpath("//ul[@id='tas']/a").pop(i).click()
            time.sleep(5)
            str1 = self.driver.find_element_by_xpath("//*[@class='active']").text
            hrefs = len(self.driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a'))
            # print(str1, "模块")
            for j in range(0, hrefs):
                # 院系
                dep = self.driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a').pop(j).text
                # 链接
                # link = self.driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a').pop(j).get_property('href')
                link = self.driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a').pop(j).get_attribute('href')
                # 模块
                module.insert(j, str1)
                colum_dep.insert(j, dep)
                colum_link.insert(j, link)
                # link_dict.update({dep: link})
        LoginInfo.write_excel(self, row0, module, colum_dep, colum_link)
        # for k, v in link_dict.items():
        #     print(k, ":\t", v)
        time.sleep(1)
        # 退出
        LoginInfo.user_logout(self, self.driver)


# 执行测试
# LoginTest().test_admin_login()
# LoginTest().test_bachelor_login()
# LoginTest().test_logout()
# 回归测试
# LoginTest().test_enginfo()
LoginTest().test_URL()
