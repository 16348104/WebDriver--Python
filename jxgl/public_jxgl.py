import time



class LoginJXGL():
    # 登录
    def userlogin(self, driver, user, password):
        print(user, password)
        driver.find_element_by_xpath('//*[@id="userName"]').send_keys(user)
        driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
        time.sleep(3)
        driver.find_element_by_xpath('//td[@class="but"]/input').click()
        time.sleep(20)
        driver.quit()
