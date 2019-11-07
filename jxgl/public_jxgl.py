import os
import time
import random

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class LoginJXGL():
    # 登录
    def userlogin(self, driver, username, password):
        print("public:", username, password)
        driver.find_element_by_xpath('//*[@id="userName"]').send_keys(username)
        driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
        time.sleep(1)
        driver.find_element_by_xpath('//td[@class="but"]/input').click()
        time.sleep(3)
        print("登录信息门户")
        driver.find_element_by_xpath('//*[@id="menu"]/li[1]/a[8]').click()
        time.sleep(3)
        print("进入教学评估")
        # # 切换【第二个窗口】
        windows = driver.window_handles
        # # 切换到新窗口
        driver.switch_to.window(windows[1])
        window_2 = driver.current_window_handle
        print('所有句柄:', windows)
        print("当前窗口：", window_2)
        time.sleep(1)

    # 评估问卷填写
    def fill_questionaire(self, driver):
        driver.find_element_by_xpath("//ul[@class='page-sidebar-menu']//li[4]//a[1]").click()
        time.sleep(1)
        print(driver.find_element_by_xpath("//li[@class='active']//span[@class='title']").text)
        driver.find_element_by_xpath('//tr[2]//td[6]//a[1]').click()
        time.sleep(4)
        print('教师评价')
        js_pg = len(driver.find_elements_by_xpath("//table[@class='table table-bordered']//tbody//tr"))
        print("教师评价项", js_pg)
        for i in range(0, js_pg):
            # 点第一颗心
            driver.find_elements_by_xpath(
                "//table[@class='table table-bordered']//li[1]").pop(i).click()
            time.sleep(1)
        # 保存教师评价
        # driver.find_element_by_xpath("//div[@class='jxpg container-fluid']//a[2]").click()
        # print('弹框消息:', driver.find_element_by_xpath("//div[@class='aui_content']//strong"))
        # time.sleep(2)
        print('课程评价')
        # 点第三颗心
        driver.find_element_by_xpath("//table[@class='table table-bordered second']//tbody//li[3]").click()
        print('助教评价')
        try:
            driver.find_element_by_xpath("//table[@class='table table-bordered third']")
        except NoSuchElementException as msg:
            print('本课程没助教!', msg)
        else:
            zj_pg = len(driver.find_elements_by_xpath("//table[@class='table table-bordered third']//tbody//tr"))
            print("助教评价列表", zj_pg)
            for i in range(0, zj_pg):
                # 点第二颗心
                driver.find_elements_by_xpath(
                    "//table[@class='table table-bordered']//li[2]").pop(i).click()
                time.sleep(1)
        print('建议与意见')
        proposal = len(driver.find_elements_by_xpath('//*[@id="xswjtxFormid"]//textarea'))
        print('textarea:', proposal)
        for i in range(0, proposal):
            driver.find_elements_by_xpath('//*[@id="xswjtxFormid"]//textarea').pop(i).clear()
            time.sleep(0.5)
            driver.find_elements_by_xpath('//*[@id="xswjtxFormid"]//textarea').pop(i).send_keys(
                "Writing task: Reflections on Pericles’ WordsInstructions:How does Athens look like in Pericles' words? Which aspect of it appeals to you most?Write an essay to present your reflection on these Writin!")
            time.sleep(1)
        # 保存并前往下一课
        driver.execute_script("document.documentElement.scrollTop = 10000;")  # 滚动条
        msg_success = "操作成功，评估关闭前可再次操作"
        try:
            driver.find_element_by_xpath("//*[@class='btngrouppg btn3']//a[2]").click()
            time.sleep(2)
            # try:
            msg_pj = driver.find_element_by_xpath("//div[@class='aui_content']//strong").text
            print('弹框:', msg_pj)
            time.sleep(2)
            if (msg_pj != msg_success):
                print("修改教师评价")
                # 点修改按钮
                driver.find_element_by_xpath('//*[@class="aui_state_highlight"]/following-sibling::button').click()
                time.sleep(2)
                for i in range(0, js_pg):
                    # 点第5颗心
                    driver.find_elements_by_xpath(
                        "//table[@class='table table-bordered']//li[5]").pop(i).click()
                    time.sleep(1)
                # 点保存
                driver.execute_script("document.documentElement.scrollTop = 10000;")  # 滚动条
                driver.find_element_by_xpath("//*[@class='jxpg container-fluid']//a[3]").click()
                time.sleep(2)
                print('弹框:', driver.find_element_by_xpath("//div[@class='aui_content']//strong").text)
                # 点关闭
                driver.find_element_by_xpath("//*[@class='aui_buttons']//button").send_keys(Keys.ENTER)
                # 点下一课
                time.sleep(2)
                driver.find_element_by_xpath("//*[@class='jxpg container-fluid']//a[2]").click()
            # 点不修改
            # driver.find_element_by_xpath('//*[@class="aui_state_highlight"]').send_keys(Keys.ENTER)
            # 关闭
            # driver.find_element_by_xpath("//*[@class='aui_buttons']//button").send_keys(Keys.ENTER)
            # except NoSuchElementException as msg:
            # print('本课程已评估,前往下一课!', msg)
        except NoSuchElementException as msg:
            print('本学期所有课程都已评估！', msg)
        time.sleep(2)
        print('切换课程')
        driver.find_element_by_xpath('//*[@id="controlw"]/i').click()
        time.sleep(1)
        cj_list = len(driver.find_elements_by_xpath("//*[@id='youwindow']//a"))
        ran_list = random.randrange(0, cj_list - 1)
        print('随机数', ran_list)
        driver.find_elements_by_xpath("//*[@id='youwindow']//a").pop(ran_list).click()
        time.sleep(2)
        print('弹框:', driver.find_element_by_xpath("//div[@class='aui_content']//strong").text)
        driver.find_element_by_xpath('//button[@class="aui_state_highlight"]').send_keys(Keys.ENTER)
        time.sleep(2)
        # 返回列表
        driver.find_element_by_xpath("//*[@class='jxpg container-fluid']//a[1]").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_xpath('//button[@class="aui_state_highlight"]').send_keys(Keys.ENTER)
        print("填写问卷测试完毕")
        driver.delete_all_cookies()
        time.sleep(3)
        driver.quit()

    # 历史评估查看
    def view_evaluation(self, driver):
        driver.find_element_by_xpath("//ul[@class='page-sidebar-menu']//li[5]//a[1]").click()
        print(driver.find_element_by_xpath("//li[@class='active']//span[@class='title']").text)
        time.sleep(2)
        driver.find_element_by_xpath("//tr[1]//td[5]//a[1]").click()
        driver.execute_script("document.documentElement.scrollTop = 10000;")  # 滚动条
        time.sleep(5)
        driver.execute_script("document.documentElement.scrollTop = 0;")  # 滚动条
        driver.find_element_by_xpath("//a[@class='btn btn-pgfh']").click()
        time.sleep(5)
        driver.quit()
        print("查阅历史评估测试完毕")

    # 发邮件
    def email(self):
        os.system("E:/163study/WebDriver--Python/Example/Email/sina_smtp.py")
