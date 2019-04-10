from selenium import webdriver
import time
browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Ie()
# browser.get('http://www.baidu.com')
browser.get(r'E:\163study\WebDriver--Python\upload.html')  # 文件的地址
# browser.find_element_by_name('file').send_keys(r'E:/map.png')  # 上传文件
# print('文件上传完毕')
# browser.find_element_by_class_name()
time.sleep(5)
browser.quit()
