import time

from selenium import webdriver


class LoginJXGL():
    # 登录
    def userlogin(self, driver, username, password):
        # print("public:"user, password)
        driver.find_element_by_xpath('//*[@id="userName"]').send_keys(username)
        driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
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
        print(driver.find_element_by_xpath("//li[@class='active']//span[@class='title']").text)
        driver.find_element_by_xpath('//tr[1]//td[6]//a[1]').click()
        time.sleep(3)
        print('教师评价')
        jspj = len(driver.find_elements_by_xpath("//table[@class='table table-bordered']//tbody//tr"))
        print("教师评价列表", jspj)
        for i in range(0, jspj):
            # 点第一颗心
            driver.find_elements_by_xpath(
                "//table[@class='table table-bordered']//tbody//tr[1]//td[3]//ul[1]//li[1]").pop(
                i).click()
        # 保存教师评价
        driver.find_element_by_xpath("//*[@class='btngrouppg btn3']//a[3]").click()
        time.sleep(2)
        print('弹框消息:', driver.find_element_by_xpath("//div[@class='aui_content']//strong"))
        print('课程评价')
        driver.find_element_by_xpath("//table[@class='table table-bordered second']//tbody//li[7]").click()
        time.sleep(2)
        # 助教评价
        try:
            driver.find_element_by_xpath("//table[@class='table table-bordered third']")
        except:
            print('此课程没有助教!')
        else:
            zjpj = len(driver.find_elements_by_xpath("//table[@class='table table-bordered third']//tbody//tr"))
            print("助教评价列表", zjpj)
            for i in range(0, jspj):
                # 点第一颗心
                driver.find_elements_by_xpath(
                    "//table[@class='table table-bordered']//tbody//tr[1]//td[3]//ul[1]//li[1]").pop(
                    i).click()
        # 保存并前往下一课
        driver.find_element_by_xpath("//*[@class='btngrouppg btn3']//a[2]")
        time.sleep(2)
        driver.quit()
        print("填写问卷测试完毕")

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
