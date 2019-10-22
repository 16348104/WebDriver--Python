# -*- coding: utf-8 -*-
# browser.download.dir：指定下载路径
# browser.download.folderList：设置成 2 表示使用自定义下载路径；设置成 0 表示下载到桌面；设置成 1 表示下载到默认路径
# browser.download.manager.showWhenStarting：在开始下载时是否显示下载管理器
# browser.helperApps.neverAsk.saveToDisk：对所给出文件类型不再弹出框进行询问
import os

from selenium import webdriver
import time

# profile = webdriver.FirefoxProfile()
# profile.set_preference('browser.download.dir', os.getcwd())
# profile.set_preference('browser.download.folderList', 0)
# profile.set_preference('browser.download.manager.showWhenStarting', False)
# profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
#                        'application/zip,application/xhtml+xml,application/xml,application/x-msdownload,application/octet/octet-stream,application/exe,txt/csv,application/pdf,application/x-msexcl,application/x-excel,application/excel,image/png,image/jpeg,text/html,text/plain,text/x-c')

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showhenStarting", False)
fp.set_preference("browser.download.dir", "E:\\")
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip,application/xhtml+xml,application/xml,application/x-msdownload,application/octet-stream,application/exe,txt/csv,application/pdf,application/x-msexcl,application/x-excel,application/excel,image/png,image/jpeg,text/html,text/plain,text/x-c'")  # 下载文件类型

driver = webdriver.Firefox(firefox_profile=fp)
driver.get("http://pypi.Python.org/pypi/selenium")
driver.maximize_window()
driver.find_element_by_xpath("//a[@id='files-tab']").click()
time.sleep(3)
driver.find_element_by_xpath("//a[contains(text(),'selenium-3.141.0.tar.gz')]").click()
time.sleep(10)
driver.quit()
