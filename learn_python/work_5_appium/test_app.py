# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 17:24
# @Author  : pengketong


from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Test_App:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_delete(self):
        name = 'hh'
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # # 点击搜索
        # self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/i6n').click()
        # # 搜索输入内容
        # self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/gpg').send_keys(name)