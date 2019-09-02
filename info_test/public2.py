import time

from selenium.webdriver.common.keys import Keys


class LoginInfo():

    # 登录
    def user_login(self, driver, user, password):
        driver.find_element_by_id('user').send_keys(user)
        driver.find_element_by_id('pass').send_keys(password)
        driver.find_element_by_id('loginButtonId').send_keys(Keys.ENTER)
        time.sleep(3)

    # 退出
    def user_logout(self, driver):
        # driver.find_element_by_id('user').send_keys(user)
        # driver.find_element_by_id('pass').send_keys(password)
        # driver.find_element_by_id('loginButtonId').send_keys(Keys.ENTER)
        # time.sleep(5)
        js_logout = "beforeLogout();"
        driver.execute_script(js_logout)
        # time.sleep(1)
        driver.find_element_by_xpath("//*[@class='btn btn-sub']").send_keys(Keys.ENTER)
        print('=====退出info=====')
        driver.delete_all_cookies()
        driver.quit()

    # 切换到第二个窗口
    def switch_window(self, driver):
        windows = driver.window_handles  # 窗口总数
        window_1 = driver.current_window_handle  # 当前窗口句柄
        for current_window in windows:
            if current_window != window_1:
                driver.switch_to.window(current_window)
        print('所有句柄:', windows)
        print("当前窗口：", window_1)
        print("窗口title", driver.title)
        time.sleep(2)
        driver.close()
        # 切换回第一个窗口
        driver.switch_to.window(windows[0])
        window_2 = driver.current_window_handle
        print("当前窗口：", window_2)
