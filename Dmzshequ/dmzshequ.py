import random
import time
from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException, TimeoutException, \
    ElementNotInteractableException

# browser = webdriver.Firefox()
# browser = webdriver.Ie()
# browser = webdriver.Chrome()

# browser = webdriver.Chrome(executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/wlxt/chromedriver')

browser = webdriver.Safari()
browser.maximize_window()
browser.get('http://www.dmzshequ.com')
# browser.get('http://www.dmzshequ.com/plugin.php?id=dsu_paulsign:sign')#直接登录
browser.implicitly_wait(3)
print('登录Dmz社区!')
print(browser.title)
print('浏览器:' + browser.name)
time.sleep(2)
browser.find_element_by_xpath("//a[@class='deandengluanniu']").click()


def login(user, password):
    browser.find_element_by_name("username").send_keys(user)
    browser.find_element_by_name("password").send_keys(password)


## 登录
# login('zijing228', 'yu123456')
login('milometer', 'ustb55')
# browser.implicitly_wait(2)
browser.find_element_by_xpath('//button[@name="loginsubmit"]').click()
time.sleep(3)
print('登录成功!')
browser.refresh()  # 刷新
##### 签到
time.sleep(3)
print("Dmz社区>", browser.find_element_by_xpath("//*[@id='pt']//a[2]").text)
try:
    browser.find_element_by_xpath("//ul[@class='qdsmile']//following-sibling::li")
    # except NoSuchElementException as msg:
except BaseException:
    print('今天已签到!')
    print(BaseException)
else:
    qdbq = len(browser.find_elements_by_xpath("//ul[@class='qdsmile']//following-sibling::li"))
    ran_bq = random.randrange(qdbq)
    xq = random.choice(['开心', '难过', '郁闷', '无聊', '发怒', '擦汗', '奋斗', '慵懒', '悲哀'])
    print('签到头像:', ran_bq)
    browser.find_elements_by_xpath("//ul[@class='qdsmile']//following-sibling::li").pop(ran_bq).click()
    browser.implicitly_wait(1)
    print('签到心情:', xq)
    browser.find_element_by_id('todaysay').send_keys('今天', xq, '!')
    browser.find_element_by_xpath("//*[@id='qiandao']/table[1]/tbody/tr/td/div/a").click()

##### 摇一摇
time.sleep(5)
try:
    browser.find_element_by_xpath("//*[@id='zzza_tixing']/div[1]/div[1]/a")
except BaseException:
    print('今天摇过了!')
    print(BaseException)
else:
    print(browser.find_element_by_xpath("//*[@id='zzza_tixing']/div[1]/div[1]/a").text)
    browser.find_element_by_xpath("//*[@id='zzza_tixing']/div[1]/div[1]/a").click()
    # browser.switch_to_alert()
    time.sleep(5)
    try:
        print(browser.find_element_by_xpath("//*[@id='zzza_go']").text)
        browser.find_element_by_xpath("//*[@id='zzza_go']").click()  # 摇金币
        time.sleep(1)
    # except UnexpectedAlertPresentException as msg_alert:
    except BaseException:
        print(BaseException)
        print(browser.switch_to.alert.text)  # 如果签到不成功，接受摇金币时弹出alter
        browser.switch_to.alert.accept()
    else:
        pass
        # time.sleep(5)
        # browser.find_element_by_xpath('//*[@id="yyl-random-box"]/div[1]').click()
time.sleep(5)
print('今天任务已完成!')
current_time = time.strftime("%y-%m-%d %H:%M:%S", time.localtime(time.time()))
print('在', current_time, '退出Dmz社区')
browser.close()
