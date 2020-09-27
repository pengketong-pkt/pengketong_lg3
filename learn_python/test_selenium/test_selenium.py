from time import sleep

import pytest
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestHome:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        # self.driver.get("https://www.baidu.com")
        self.driver.get('http://sahitest.com/demo/clicks.htm')


    def teardown(self):
        self.driver.quit()

    def test_case_click(self):
        # self.driver.find_element(By.CSS_SELECTOR,'#kw').send_keys("霍格沃兹测试学院")
        # sleep(2)
        elemenet_click = self.driver.find_element_by_xpath('//*[@value="click me"]')
        elemenet_doubleclick = self.driver.find_element_by_xpath('//*[@value="dbl click me"]')
        elemenet_rightclick = self.driver.find_element_by_xpath('//*[@value="right click me"]')
        action = ActionChains(self.driver)
        action.click(elemenet_click)
        action.context_click(elemenet_rightclick)
        action.double_click(elemenet_doubleclick)
        action.perform()
        sleep(3)


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_selenium.py'])
