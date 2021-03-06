"""
光标操作
ctrl+alt+enter:向上插入
shift+enter:向下插入
end:光标
操作代码
ctrl+d:复制粘贴一行
ctrl+y:删除一行
shift+F6:重命令
ctrl+O:复写代码
接使用快捷键的方式来，来对代码进行缩进，选中代码之后，直接按 tab键即可
"""
from time import sleep

import pytest
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# 定义类
class TestHome:

    # def setup(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.maximize_window()
        # self.driver.implicitly_wait(5)
        # self.driver.get("https://www.baidu.com")

    # def teardown(self):
    #     self.driver.quit()

    # @pytest.mark.skip
    def test_case_click(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com')
        # self.driver.get('http://sahitest.com/demo/clicks.htm')
        # self.driver.find_element(By.CSS_SELECTOR,'#kw').send_keys("霍格沃兹测试学院")
        # sleep(2)
        # elemenet_click = self.driver.find_element_by_xpath('//*[@value="click me"]')
        # elemenet_doubleclick = self.driver.find_element_by_xpath('//*[@value="dbl click me"]')
        # elemenet_rightclick = self.driver.find_element_by_xpath('//*[@value="right click me"]')
        # action = ActionChains(self.driver)
        # action.click(elemenet_click)
        # action.context_click(elemenet_rightclick)
        # action.double_click(elemenet_doubleclick)
        # action.perform()
        sleep(10)

    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("http://www.baidu.com")
        #ele = self.driver.find_element_by_xpath('//*[@name="tj_briicon"]')
        ele = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')

        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(10)

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")
        drop_element = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_element, drop_element).perform()
        sleep(10)
# if __name__ == '__main__':
#  pytest.main(['-v', '-s', 'test_selenium.py'])
