# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 17:24
# @Author  : pengketong
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Test_App:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        # caps["appPackage"] = "com.tencent.wework"
        # caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["appPackage"] = " com.uroad.carclub"
        caps["appActivity"] = ".splash.SplashActivity"
        caps["noReset"] = "true"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
    #ETC车宝app登录
    def test_delete(self):
        name = 'hh'
        # 点击通讯录
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element_by_id('com.uroad.carclub:id/tab_lottie_anim_layout_4').click()
        self.driver.find_element_by_id('com.uroad.carclub:id/mine_head_iv').click()
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.uroad.carclub:id/login_with_pwd_tv'and @text='密码登录']").click()
        self.driver.find_element_by_id('com.uroad.carclub:id/phone_number_two_et').send_keys("13680586193")
        self.driver.find_element_by_id('com.uroad.carclub:id/login_pwd_et').send_keys("qw111111")
        self.driver.find_element_by_id('com.uroad.carclub:id/login_with_pwd_btn').click()
        sleep(3)
        # # 点击搜索
        # self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/i6n').click()
        # # 搜索输入内容
        # self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/gpg').send_keys(name)
