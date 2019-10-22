# -*- coding: utf-8 -*-
# browser.download.dir：指定下载路径
# browser.download.folderList：设置成 2 表示使用自定义下载路径；设置成 0 表示下载到桌面；设置成 1 表示下载到默认路径
# browser.download.manager.showWhenStarting：在开始下载时是否显示下载管理器
# browser.helperApps.neverAsk.saveToDisk：对所给出文件类型不再弹出框进行询问


from selenium import webdriver
import time

profile = webdriver.FirefoxProfile()
# profile.set_preference('browser.download.dir', 'd:\\')
profile.set_preference('browser.download.folderList', 0)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
                       'application/zip,application/xhtml+xml,application/xml,application/x-msdownload,application/octet/octet-stream,application/exe,txt/csv,application/pdf,application/x-msexcl,application/x-excel,application/excel,image/png,image/jpeg,text/html,text/plain,text/x-c')
# 不会打开未知MIMe类型
# profile.set_Preference("browser.helperApps.alwaysAsk.force", False)
# 不会弹出警告框
# profile.set_Preference("browser.download.manager.alertOnEXEopen", False)
# profile.set_Preference("browser.download.manager.focusWhenStarting", False)
# profile.set_Preference("browser.download.manager.useWindow", False)
# profile.set_Preference("browser.download.manager.showAlertOnComplete", False)
# profile.set_Preference("browser.download.manager.closewhenDone", False)

driver = webdriver.Firefox(profile)

driver.get('http://sahitest.com/demo/saveAs.htm')
driver.find_element_by_xpath('//a[text()="testsaveas.zip"]').click()
time.sleep(3)
driver.quit()
