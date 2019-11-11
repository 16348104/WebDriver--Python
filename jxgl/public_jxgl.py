import os
import time
import random
import smtplib
from email.header import Header
from email.mime.text import MIMEText
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
        driver.delete_all_cookies()
        time.sleep(2)
        driver.quit()

    # 未评估问卷填写
    def fill_questionaire_wp(self, driver):
        driver.find_element_by_xpath("//ul[@class='page-sidebar-menu']//li[4]//a[1]").click()
        time.sleep(1)
        print(driver.find_element_by_xpath("//li[@class='active']//span[@class='title']").text)
        driver.find_element_by_xpath('//tr[2]//td[6]//a[1]').click()
        time.sleep(3)
        print('课程名:', driver.find_element_by_xpath("//div[@class='head']").text)
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
        driver.find_element_by_xpath("//span[@class='go-top']").click()
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
                driver.find_element_by_xpath("//span[@class='go-top']").click()
                # 点修改按钮
                driver.find_element_by_xpath('//*[@class="aui_state_highlight"]/following-sibling::button').click()
                time.sleep(2)
                for i in range(0, js_pg):
                    # 点第5颗心
                    driver.find_elements_by_xpath(
                        "//table[@class='table table-bordered']//li[5]").pop(i).click()
                    time.sleep(1)
                driver.execute_script("document.documentElement.scrollTop = 10000;")  # 滚动条
                # 点保存
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
        # print('切换课程')
        # driver.find_element_by_xpath("//span[@class='go-top']").click()
        # driver.find_element_by_xpath('//*[@id="controlw"]/i').click()
        # time.sleep(1)
        # cj_list = len(driver.find_elements_by_xpath("//*[@id='youwindow']//a"))
        # ran_list = random.randrange(0, cj_list - 1)
        # print('随机数', ran_list)
        # driver.find_elements_by_xpath("//*[@id='youwindow']//a").pop(ran_list).click()
        # time.sleep(3)
        # print('弹框:', driver.find_element_by_xpath("//div[@class='aui_content']//strong").text)
        # driver.find_element_by_xpath('//button[@class="aui_state_highlight"]').send_keys(Keys.ENTER)
        # time.sleep(2)
        # print('课程名:', driver.find_element_by_xpath("//div[@class='head']").text)
        # 返回列表
        driver.find_element_by_xpath("//a[@class='btn btn-pgfh']").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_xpath('//button[@class="aui_state_highlight"]').send_keys(Keys.ENTER)
        print("填写未评问卷测试完毕")
        driver.delete_all_cookies()
        time.sleep(2)
        driver.quit()

    # 已评估问卷填写
    def fill_questionaire_yp(self, driver):
        driver.find_element_by_xpath("//ul[@class='page-sidebar-menu']//li[4]//a[1]").click()
        time.sleep(1)
        print(driver.find_element_by_xpath("//li[@class='active']//span[@class='title']").text)
        driver.find_element_by_xpath('//tr[1]//td[6]//a[1]').click()
        time.sleep(3)
        print('课程名:', driver.find_element_by_xpath("//div[@class='head']").text)
        print('教师评价')
        js_pg = len(driver.find_elements_by_xpath("//table[@class='table table-bordered']//tbody//tr"))
        print("教师评价项", js_pg)
        for i in range(0, js_pg):
            # 点第七颗心
            driver.find_elements_by_xpath(
                "//table[@class='table table-bordered']//li[6]").pop(i).click()
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
        driver.find_element_by_xpath("//span[@class='go-top']").click()
        proposal = len(driver.find_elements_by_xpath('//*[@id="xswjtxFormid"]//textarea'))
        print('textarea:', proposal)
        for i in range(0, proposal):
            driver.find_elements_by_xpath('//*[@id="xswjtxFormid"]//textarea').pop(i).clear()
            time.sleep(0.5)
            driver.find_elements_by_xpath('//*[@id="xswjtxFormid"]//textarea').pop(i).send_keys(
                "Writing task: Reflections on Pericles’ WordsInstructions:How does Athens look like in Pericles' words? Which aspect of it appeals to you most?Write an essay to present your reflection on these Writin!")
            time.sleep(1)
        # 保存评价
        driver.execute_script("document.documentElement.scrollTop = 10000;")  # 滚动条
        # msg_success = "操作成功，评估关闭前可再次操作"
        try:
            driver.find_element_by_xpath("//*[@class='btngrouppg btn3']//a[2]").click()
            time.sleep(2)
            # try:
            msg_pj = driver.find_element_by_xpath("//div[@class='aui_content']//strong").text
            print('弹框:', msg_pj)
            time.sleep(2)

            # if (msg_pj != msg_success):
            #     print("修改教师评价")
            #     driver.find_element_by_xpath("//span[@class='go-top']").click()
            #     # 点修改按钮
            #     driver.find_element_by_xpath('//*[@class="aui_state_highlight"]/following-sibling::button').click()
            #     time.sleep(2)
            #     for i in range(0, js_pg):
            #         # 点第5颗心
            #         driver.find_elements_by_xpath(
            #             "//table[@class='table table-bordered']//li[5]").pop(i).click()
            #         time.sleep(1)
            #     driver.execute_script("document.documentElement.scrollTop = 10000;")  # 滚动条
            #     # 点保存按钮
            #     driver.find_element_by_xpath("//*[@class='jxpg container-fluid']//a[2]").click()
            #     time.sleep(2)
            #     print('弹框:', driver.find_element_by_xpath("//div[@class='aui_content']//strong").text)
            #     # 点关闭
            #     driver.find_element_by_xpath("//*[@class='aui_buttons']//button").send_keys(Keys.ENTER)
            # 点不修改
            # driver.find_element_by_xpath('//*[@class="aui_state_highlight"]').send_keys(Keys.ENTER)
            # 关闭弹框
            driver.find_element_by_xpath("//*[@class='aui_buttons']//button").send_keys(Keys.ENTER)
        except NoSuchElementException as msg:
            pass
        time.sleep(2)
        # print('切换课程')
        # driver.find_element_by_xpath("//span[@class='go-top']").click()
        # driver.find_element_by_xpath('//*[@id="controlw"]/i').click()
        # time.sleep(1)
        # cj_list = len(driver.find_elements_by_xpath("//*[@id='youwindow']//a"))
        # ran_list = random.randrange(0, cj_list - 1)
        # print('随机数', ran_list)
        # driver.find_elements_by_xpath("//*[@id='youwindow']//a").pop(ran_list).click()
        # time.sleep(3)
        # print('弹框:', driver.find_element_by_xpath("//div[@class='aui_content']//strong").text)
        # driver.find_element_by_xpath('//button[@class="aui_state_highlight"]').send_keys(Keys.ENTER)
        # time.sleep(2)
        # print('课程名:', driver.find_element_by_xpath("//div[@class='head']").text)
        # 返回列表
        driver.find_element_by_xpath("//a[@class='btn btn-pgfh']").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_xpath('//button[@class="aui_state_highlight"]').send_keys(Keys.ENTER)
        print("填写已评问卷测试完毕")
        driver.delete_all_cookies()
        time.sleep(3)

    # 转换评估课程
    def change_list(self, driver):
        print('切换评估课程')
        driver.find_element_by_xpath("//ul[@class='page-sidebar-menu']//li[4]//a[1]").click()
        time.sleep(1)
        print(driver.find_element_by_xpath("//li[@class='active']//span[@class='title']").text)
        driver.find_element_by_xpath('//tr[1]//td[6]//a[1]').click()
        time.sleep(2)
        print('当前课程:', driver.find_element_by_xpath("//div[@class='head']").text)
        driver.find_element_by_xpath('//*[@id="controlw"]/i').click()
        time.sleep(1)
        cj_list = len(driver.find_elements_by_xpath("//*[@id='youwindow']//a"))
        ran_list = random.randrange(0, cj_list - 1)
        print('随机数', ran_list)
        driver.find_elements_by_xpath("//*[@id='youwindow']//a").pop(ran_list).click()
        time.sleep(3)
        print('弹框:', driver.find_element_by_xpath("//div[@class='aui_content']//strong").text)
        driver.find_element_by_xpath('//button[@class="aui_state_highlight"]').send_keys(Keys.ENTER)
        time.sleep(2)
        print('转换后课程:', driver.find_element_by_xpath("//div[@class='head']").text)
        driver.execute_script("document.documentElement.scrollTop = 10000;")
        time.sleep(2)
        driver.find_element_by_xpath("//span[@class='go-top']").click()
        time.sleep(2)
        # 返回列表
        driver.find_element_by_xpath("//a[@class='btn btn-pgfh']").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_xpath('//button[@class="aui_state_highlight"]').send_keys(Keys.ENTER)

    # 历史评估查看
    def view_evaluation(self, driver):
        # 进入课程
        driver.find_element_by_xpath("//ul[@class='page-sidebar-menu']//li[5]//a[1]").click()
        print(driver.find_element_by_xpath("//li[@class='active']//span[@class='title']").text)
        time.sleep(2)
        driver.find_element_by_xpath("//tr[1]//td[5]//a[1]").click()
        driver.execute_script("document.documentElement.scrollTop = 10000;")  # 滚动条
        time.sleep(3)
        driver.find_element_by_xpath("//span[@class='go-top']").click()
        # 返回首页
        driver.find_element_by_xpath("//a[@class='btn btn-pgfh']").click()
        time.sleep(3)
        driver.quit()
        print("查阅历史评估测试完毕")

    # 发邮件
    def email(self):
        fromaddr = 'chercheren2008@sina.com'
        password = 'b396d7b686e6d9d9'
        toaddrs = ['xdx@pku.org.cn', 'wlxt@tsinghua.edu.cn']
        # 设置email信息
        # ---------------------------发送字符串的邮件-----------------------------
        # 邮件内容设置
        message = MIMEText('此为系统测试邮件，请勿直接回复！', 'plain', 'utf-8')
        # 邮件主题
        message['Subject'] = '教学评估测试完成!'
        # 发送方信息
        message['From'] = fromaddr
        # 接受方信息可以不填
        # message['To'] = toaddrs[0]
        # message['To'] = toaddrs[1]
        # 登录并发送邮件
        try:
            server = smtplib.SMTP('smtp.sina.cn')  # 新浪邮箱服务器地址，端口默认为25
            server.login(fromaddr, password)
            server.sendmail(fromaddr, toaddrs, message.as_string())
            print('Success,Email has send out!')
            server.quit()

        except smtplib.SMTPException as e:
            print('error', e)  # 打印错误
        # os.system("E:/163study/WebDriver--Python/Example/Email/sina_smtp.py")


