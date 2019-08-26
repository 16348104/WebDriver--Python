from selenium.webdriver.common.keys import Keys


class LoginInfo():

    # 登录
    def user_login(self, driver, user, password):
        driver.find_element_by_id('user').send_keys(user)
        driver.find_element_by_id('pass').send_keys(password)
        # time.sleep(1)
        driver.find_element_by_id('loginButtonId').send_keys(Keys.ENTER)

    # 退出
    def user_logout(self, driver):
        driver.find_element_by_link_text("退出").click()
        driver.quit()
