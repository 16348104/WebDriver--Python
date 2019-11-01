import time



class LoginJXGL():
    # 登录
    def userlogin(self, driver, user, password):
        # print("public:"user, password)
        driver.find_element_by_xpath('//*[@id="userName"]').send_keys(user)
        driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
        driver.find_element_by_xpath('//td[@class="but"]/input').click()
        time.sleep(10)
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
        time.sleep(10)

        # driver.quit()
