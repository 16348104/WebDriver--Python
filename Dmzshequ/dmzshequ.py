import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# browser = webdriver.Firefox()
browser = webdriver.Ie()
# browser = webdriver.Chrome()
# browser = webdriver.Safari()
browser.maximize_window()
browser.get('http://www.dmzshequ.com')
# browser.get('http://www.dmzshequ.com/plugin.php?id=dsu_paulsign:sign')#直接登录
browser.implicitly_wait(2)
print('登录Dmz社区!')
print(browser.title)
print('浏览器:' + browser.name)
browser.implicitly_wait(5)
browser.find_element_by_xpath("//a[@class='deandengluanniu']").click()


def login(user, password):
    browser.find_element_by_name("username").send_keys(user)
    browser.find_element_by_name("password").send_keys(password)


login('zijing228', 'yu123456')
browser.find_element_by_xpath('//button[@name="loginsubmit"]').click()
print('登录成功')
browser.implicitly_wait(5)
print('开始摇一摇!')

try:
    browser.find_element_by_xpath("//*[@id='zzza_tixing']/div[1]/div[1]/a")
except NoSuchElementException as msg:
    # print('今天已经摇过了!', msg)
    print('今天已经摇过了!')
else:
    print('可以摇奖!')
    browser.find_element_by_xpath("//*[@id='zzza_tixing']/div[1]/div[1]/a").click()
    browser.implicitly_wait(5)
    browser.find_element_by_xpath("//*[@id='zzza_go']").click()
    browser.find_element_by_xpath('//*[@id="yyl-random-box"]/div[1]').click()
print('今天任务已完成!')
current_time = time.strftime("%y-%m-%d %H:%M:%S", time.localtime(time.time()))
print('在', current_time, '退出Dmz社区')
browser.close()
