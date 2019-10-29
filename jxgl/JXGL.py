import time

from openpyxl import Workbook
import xlrd
# //table[@class='table table-bordered']//tbody//tr[1]//td[3]//ul[1]//li
from selenium import webdriver
from public import LoginJXGL


class Test_JXGL():
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        # Mac os
        # self.driver = webdriver.Safari()
        # self.driver = webdriver.Chrome(executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/chromedriver')  # MacOS

        # Eng_info模拟环境
        self.driver.get('http://infoen.syx.thcic.cn')
        self.driver.maximize_window()
        print("======进入info学生端=====")
        time.sleep(4)
