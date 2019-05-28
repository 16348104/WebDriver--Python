# coding=utf-8
import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# driver = webdriver.Chrome(executable_path='C:/Users/zb/Desktop/test/python/chromedriver.exe')  # modify
# driver = webdriver.Firefox()

driver = webdriver.Chrome()


# driver = webdriver.Firefox(
#     executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/wlxt/geckodriver')  # mac firefox
# driver = webdriver.Chrome(executable_path='/Users/xiaodaxing/Downloads/PycharmProjects/wlxt/chromedriver')  # mac  chrome
# driver = webdriver.Safari() #Mac os

def time_format():
    current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    return current_time


######################################################登录网络学堂######################################################
# 打开网络学堂
driver.get("http://learn.tsinghua.edu.cn")
driver.maximize_window()
print("======登录网络学堂=====")
print(driver.title)
print('测试浏览器:' + driver.name)
ticks = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# 计算明天时间
tomorrow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 3600))
print("当前时间戳为:", ticks)
# print ("当前时间戳为:", tomorrow)
driver.find_element_by_name("i_user").send_keys("")
driver.find_element_by_name("i_pass").send_keys("")
driver.find_element_by_id("loginButtonId").click()
time.sleep(1)
######################################################课程公告##########################################################
print('=====测试课程公告=====')
driver.get(
    "http://learn.tsinghua.edu.cn/f/wlxt/kcgg/wlkc_ggb/teacher/beforeAdd?wlkcid=2018-2019-226ef84e7689589e901689906e324686a")
print('发布公告')
time.sleep(2)
driver.find_element_by_name("bt").send_keys("测试公告" + ticks)
driver.find_element_by_xpath("//div[@class='list title notext']//label[1]").click()  # 标记重要公告
driver.find_element_by_xpath("//div[@class='list order clearfix']//label[1]").click()  # 不推送邮件、微信
time.sleep(1)
driver.find_element_by_id("saveBtn").click()
time.sleep(1)
print('弹框结果:' + driver.find_element_by_css_selector(
    "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
print('预览公告')
driver.find_element_by_xpath("//a[@id='wlxt_kcgg_wlkc_ggb']").click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[1]/a').click()
driver.execute_script("document.documentElement.scrollTop = 10000;")  # 滚动条
time.sleep(1)
print('=====公告测试完毕=====')
time.sleep(4)
######################################################课程文件##########################################################
# 打开课程文件
driver.get(
    "http://learn.tsinghua.edu.cn/f/wlxt/kj/wlkc_kjxxb/teacher/beforeAdd?wlkcid=2018-2019-226ef84e7689589e901689906e324686a")
# 定位上传按钮，添加本地文件
print('=====测试课程文件=====')
js = "document.getElementById('fileupload').style.display=\'block\'"
driver.execute_script(js)
driver.find_element_by_name("bt").send_keys("测试课件" + ticks)
driver.find_element_by_xpath("//div[@class='list']//label[1]").click()  # 重要标记
# driver.find_element_by_name("fileupload").send_keys("D:/Global .mp4")  # modify
driver.find_element_by_id('fileupload').send_keys(
    r'/Users/xdx/PycharmProjects/WebDriver--Python/wlxt/readme.txt')  # mac上传文件
time.sleep(5)
driver.find_element_by_id("sub").click()
time.sleep(1)
try:
    driver.find_element_by_css_selector(
        "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1")
except NoSuchElementException as msg:
    print('截图', msg)
    driver.get_screenshot_as_file("C:/Users/zb/Downloads/" + 'KJ' + time_format() + ".png")
else:
    print('弹框结果:' + driver.find_element_by_css_selector(
        "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
print('查看课件详情')
driver.find_element_by_xpath("//a[@id='wlxt_kj_wlkc_kjxxb']").click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]/a').click()
driver.execute_script("document.documentElement.scrollTop = 10000;")  # 滚动条
time.sleep(2)
# print('下载课件')


print('=====文件测试完毕=====')
time.sleep(5)
######################################################课程作业##########################################################
# 布置作业
print('=====测试课程作业=====')
print('=====布置作业=====')
driver.get(
    "http://learn.tsinghua.edu.cn/f/wlxt/kczy/zy/teacher/bzzy?wlkcid=2018-2019-226ef84e7689589e901689906e324686a")
# driver.find_element_by_name("bt").send_keys("测试全体作业" + ticks)
# # 定位上传按钮，添加本地文件
# js = "document.getElementById('fileupload').style.display=\'block\'"
# driver.execute_script(js)
# driver.find_element_by_name("fileupload").send_keys("D:/listening.pdf")  # modify
# # 设置截止时间
# # driver.find_element_by_name("jzsj").send_keys(tomorrow)
# scroll = "document.documentElement.scrollTop = 10000;"
# driver.execute_script(scroll)
# time.sleep(1)
# driver.find_element_by_id('endtime').click()
# time.sleep(2)
# driver.find_element_by_xpath("//span[@class='laydate-btns-confirm']").click()
# time.sleep(1)
# driver.find_element_by_id("goBtn").click()  # 发布作业
# time.sleep(2)
# try:
#     driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1")
# except NoSuchElementException as msg:
#     print(msg, '截图')
#     driver.get_screenshot_as_file("C:/Users/zb/Downloads/" + 'ZY' + time_format() + ".png")
# else:
#     print('弹框结果:' + driver.find_element_by_css_selector(
#         "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
time.sleep(3)
print('=====编辑作业=====')
driver.find_element_by_xpath("//a[@id='wlxt_kczy_zy']").click()
time.sleep(2)
driver.find_element_by_xpath("//tr[2]//td[8]//a[3]").click()
# zy_geren = driver.find_element_by_xpath('//*[@id="r1"]').get_property('checked')  # 选作业完成方式:个人
# print('get_property是否个人作业：', zy_geren)
zy_geren = driver.find_element_by_xpath('//*[@id="r1"]').get_attribute('checked')  # 选作业完成方式:个人
print('是否个人作业：', zy_geren)
zy_zu = driver.find_element_by_xpath('//*[@id="r2"]').get_attribute('checked')  # 选作业完成方式:组
print('是否组作业：', zy_zu)
jf_fz = driver.find_element_by_xpath('//*[@id="r7"]').get_attribute('checked')  # 成绩计分方式:分值成绩
print('是否分值:', jf_fz)
jf_ffz = driver.find_element_by_xpath('//*[@id="r8"]').get_attribute('checked')  # 成绩计分方式:非分值成绩
print('是否非分值:', jf_ffz)
time.sleep(3)
print('=====批阅作业=====')
driver.find_element_by_xpath("//a[@id='wlxt_kczy_zy']").click()
time.sleep(2)
# 批阅作业列表beforePageList
driver.find_element_by_xpath('//tr[2]//td[8]//a[1]').click()  # 去批阅作业
driver.find_element_by_xpath("//*[@class='zhan']").click()  # 展开
if zy_geren == 'true' and jf_fz == 'true':  # 个人分值作业
    try:
        driver.find_element_by_xpath('//*[@id="done"]/tbody/tr/td[11]/a')  # 已交作业名单beforePiYue
    except NoSuchElementException as msg:
        print('表中数据为空,作业未提交', msg)
    else:
        driver.find_element_by_xpath('//*[@id="done"]/tbody/tr/td[11]/a').click()  # 批阅作业
        time.sleep(1)
        try:
            driver.find_element_by_xpath('//*[@id="attachment222"]/div[2]/a[2]')  # 学生作业附件
        except NoSuchElementException as msg:
            print('无上交作业附件', msg)
        else:
            driver.find_element_by_xpath('//*[@id="attachment222"]/div[2]/a[2]').click()  # 下载学生的作业附件
        driver.find_element_by_xpath("//*[@id='cj']").clear()
        driver.find_element_by_xpath("//*[@id='cj']").send_keys('100')  # 打分
        driver.find_element_by_xpath("//*[@id='documention']").clear()
        driver.find_element_by_xpath("//*[@id='documention']").send_keys('个人作业已阅')  # 填评语
        driver.find_element_by_id('fileupload').send_keys(
            r'C:/Users/zb/Desktop/test/python/review.docx')  # modify      # 传评语附件
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='sub-back sub-back-3 absolute']//input[1]").click()
        time.sleep(2)
        try:
            driver.find_element_by_css_selector(
                "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1")
        except NoSuchElementException as msg:
            print('批阅截图', msg)
            driver.get_screenshot_as_file("C:/Users/zb/Downloads/" + 'PZJ' + time_format() + ".png")  # modify
        else:
            print('弹框结果:' + driver.find_element_by_css_selector(
                "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
elif zy_geren == 'true' and jf_ffz == 'true':  # 个人非分值作业
    try:
        driver.find_element_by_xpath('//*[@id="done"]/tbody/tr/td[11]/a')  # 已交作业名单beforePiYue
    except NoSuchElementException as msg:
        print('表中数据为空,作业未提交', msg)
    else:
        driver.find_element_by_xpath('//*[@id="done"]/tbody/tr/td[11]/a').click()  # 批阅作业
        time.sleep(1)
        try:
            driver.find_element_by_xpath("//a[@class='ml-10']")  # 学生作业附件
        except NoSuchElementException as msg:
            print('无上交作业附件', msg)
        else:
            driver.find_element_by_xpath("//a[@class='ml-10']").click()  # 下载学生的作业附件
        driver.find_element_by_xpath('//*[@id="select2-cj-container"]').click()  # 定位下拉菜单
        time.sleep(1)
        driver.find_element_by_xpath('//ul[@id="select2-cj-results"]')
        time.sleep(1)
        # driver.find_element_by_xpath('//ul[@id="select2-cj-results"]/li[2]').click()
        key = len(driver.find_elements_by_xpath("//li[@class='select2-results__option']"))
        print("等级成绩个数", key)
        li = random.randrange(1, key)
        # cj = driver.find_elements_by_xpath("//li[@class='select2-results__option']").pop(li).text
        print('成绩:', driver.find_elements_by_xpath("//li[@class='select2-results__option']").pop(li).text)
        driver.find_elements_by_xpath("//li[@class='select2-results__option']").pop(li).click()  # 选成绩
        driver.find_element_by_xpath("//*[@id='documention']").clear()
        driver.find_element_by_xpath("//*[@id='documention']").send_keys('个人作业已阅')  # 填评语
        time.sleep(1)
        driver.find_element_by_id('fileupload').send_keys(
            r'C:/Users/zb/Desktop/test/python/review.docx')  # modify      # 传评语附件
        time.sleep(1)
        driver.find_element_by_xpath("//*[@class='sub-back sub-back-3 absolute']//input[1]").click()
        time.sleep(2)
        try:
            driver.find_element_by_css_selector(
                "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1")
        except NoSuchElementException as msg:
            print('批阅截图', msg)
            driver.get_screenshot_as_file("C:/Users/zb/Downloads/" + 'PZJ' + time_format() + ".png")  # modify
        else:
            print('弹框结果:' + driver.find_element_by_css_selector(
                "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
elif zy_zu == 'true' and jf_fz == 'true':  # 分值组作业
    try:
        driver.find_element_by_xpath('//*[@id="done"]/tbody/tr/td[8]/a')  # 已交作业名单beforePiYue
    except NoSuchElementException as msg:
        print('表中数据为空,作业未提交', msg)
    else:
        driver.find_element_by_xpath('//*[@id="done"]/tbody/tr/td[8]/a').click()  # 批阅作业
        time.sleep(1)
        try:
            driver.find_element_by_xpath('//*[@id="attachment2"]/div[2]/a[2]')  # 无学生作业附件
        except NoSuchElementException as msg:
            print('无上交作业附件', msg)
        else:
            driver.find_element_by_xpath('//*[@id="attachment2"]/div[2]/a[2]').click()  # 下载学生作业附件
        driver.find_element_by_id('resetPL').click()  # 重置
        driver.find_element_by_id('inputPL').send_keys('100')  # 打分
        driver.find_element_by_id('recommandPL').send_keys('组作业已阅')  # 填评语
        driver.find_element_by_id('setPL').click()  # 设定成绩
        driver.find_element_by_id('fileupload').send_keys(
            r'C:/Users/zb/Desktop/test/python/review.docx')  # modify # 传评语附件
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='sub-back sub-back-3 absolute']//input[1]").click()
        time.sleep(1)
        try:
            driver.find_element_by_css_selector(
                "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1")
        except NoSuchElementException as msg:
            print('截图', msg)
            driver.get_screenshot_as_file("C:/Users/zb/Downloads/" + 'PZY' + time_format() + ".png")  # modify
        else:
            print('弹框结果:' + driver.find_element_by_css_selector(
                "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
elif zy_zu == 'true' and jf_ffz == 'true':  # 非分值组作业
    try:
        driver.find_element_by_xpath('//*[@id="done"]/tbody/tr/td[8]/a')  # 已交作业名单beforePiYue
    except NoSuchElementException as msg:
        print('表中数据为空,作业未提交', msg)
    else:
        driver.find_element_by_xpath('//*[@id="done"]/tbody/tr/td[8]/a').click()  # 批阅作业
        time.sleep(1)
        try:
            driver.find_element_by_xpath('//*[@id="attachment2"]/div[2]/a[2]')  # 无学生作业附件
        except NoSuchElementException as msg:
            print('无上交作业附件', msg)
        else:
            driver.find_element_by_xpath('//*[@id="attachment2"]/div[2]/a[2]').click()  # 下载学生作业附件
        driver.find_element_by_id('resetPL').click()  # 重置
        time.sleep(1)
        # sel = driver.find_element_by_id('//*[@id="selectPL"]')
        # Select(sel).select_by_value('-98')
        driver.find_element_by_xpath('//*[@id="select2-selectPL-container"]').click()
        driver.find_element_by_xpath('//*[@id="select2-selectPL-results"]')
        key = len(driver.find_elements_by_xpath("//li[@class='select2-results__option']"))  # 定位下拉菜单
        print("等级成绩个数", key)
        li = random.randrange(1, key)
        # cj = driver.find_elements_by_xpath("//li[@class='select2-results__option']").pop(li).text
        print('成绩:', driver.find_elements_by_xpath("//li[@class='select2-results__option']").pop(li).text)
        driver.find_elements_by_xpath("//li[@class='select2-results__option']").pop(li).click()  # 选成绩
        driver.find_element_by_id('recommandPL').send_keys('组作业已阅')  # 填评语
        driver.find_element_by_id('setPL').click()  # 设定成绩
        driver.find_element_by_id('fileupload').send_keys(
            r'C:/Users/zb/Desktop/test/python/review.docx')  # modify # 传评语附件
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='sub-back absolute sub-back-3']//input[1]").click()
        time.sleep(2)
        try:
            driver.find_element_by_css_selector(
                "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1")
        except NoSuchElementException as msg:
            print('截图', msg)
            driver.get_screenshot_as_file("C:/Users/zb/Downloads/" + 'PZY' + time_format() + ".png")  # modify
        else:
            print('弹框结果:' + driver.find_element_by_css_selector(
                "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)

print('=====作业测试完毕=====')
time.sleep(5)
######################################################课程邮件##########################################################
# print('=====测试课程邮件=====')
# driver.get(
#     "http://learn.tsinghua.edu.cn/f/wlxt/mail/yj_yjxxb/teacher/beforePageList?wlkcid=2018-2019-226ef84e7689589e901689906e324686a")
# # 新邮件
# # driver.get("http://learn.tsinghua.edu.cn/f/wlxt/mail/yj_yjxxb/teacher/beforeAdd?wlkcid=2018-2019-226ef84e7689589e901689906e324686a")
# driver.find_element_by_xpath("//a[contains(text(),'新邮件')]").click()
# driver.find_element_by_class_name("ui-autocomplete-input").send_keys(
#     "xiesp@tsinghua.edu.cn,chc@tsinghua.edu.cn,xdx2016@tsinghua.edu.cn,dj1005@tsinghua.edu.cn,zhongwenfeng@tsinghua.edu.cn")
# driver.find_element_by_id("bt").send_keys("网络学堂自动测试:教师端系统正常" + ticks)
# driver.find_element_by_id("submitButton").click()
# time.sleep(1)
# print('弹框结果:' + driver.find_element_by_css_selector(
#     "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1").text)
# print('=====邮件测试完毕=====')
# time.sleep(5)
##################################################退出网络学堂##########################################################
driver.find_element_by_xpath("//i[@class='webicon-out']").click()
time.sleep(2)
driver.find_element_by_xpath("//div[contains(@class,'zeromodal-footer')]//button[contains(text(),'确定')]").send_keys(
    Keys.ENTER)
print('=====退出网络学堂=====')
driver.quit()
