import time

from selenium import webdriver
from openpyxl import *
import xlrd
# //table[@class='table table-bordered']//tbody//tr[1]//td[3]//ul[1]//li
from public_jxgl import LoginJXGL


class Test_JXGL():
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        # self.driver = webdriver.Ie()
        # Mac os
        # self.driver = webdriver.Safari()
        # self.driver = webdriver.Chrome(executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/chromedriver')  # MacOS

        # Eng_info模拟环境
        self.driver.get('http://info.syx.thcic.cn')
        self.driver.maximize_window()
        print('测试浏览器:' + self.driver.name)
        time.sleep(2)

    # 登录
    def login(self):
        wb = load_workbook(r'E:\sample.xlsx', read_only=True)
        my_sheet = wb.worksheets[0]
        # A2 = my_sheet["A2"]
        # B2 = my_sheet["B2"]
        # 用cell 函数
        user = my_sheet.cell(row=2, column=1).value
        password = my_sheet.cell(row=2, column=2).value
        # print(A2.value, B2.value)
        # print(user, password)
        LoginJXGL().userlogin(self.driver, user, password)


# 执行测试
Test_JXGL().login()
