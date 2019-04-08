#-*-coding:utf-8-*-

from appium import webdriver
import unittest

from fz.qidong import Qidong
from fz.shoushicaozuo import Shoushi
from log.lianxi123 import Logger

from selenium import webdriver
import  time

class  Denglu(unittest.TestCase):
    def setUp(self):

        pass
    def tearDown(self):
        pass
    @classmethod
    def setUpClass(self):
        #启动app
        self.driver=Qidong().driver
        pass
    @classmethod
    def tearDownClass(self):
        pass
    def test_001(self):
        #添加截图方法
        #点击耐克图标
        # try:
        self.driver.find_element_by_id("com.yougou:id/rl_toolbar_categories").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget."
                                          "FrameLayout/android.widget."
                                          "LinearLayout/android.widget."
                                          "FrameLayout/android.widget.RelativeLayout/"
                                          "android.widget.LinearLayout/android.widget."
                                          "FrameLayout/android.widget.LinearLayout/android.widget."
                                          "LinearLayout/android.widget.LinearLayout/android.widget."
                                          "FrameLayout/android.widget.ListView/android.widget."
                                          "LinearLayout[2]/android.widget."
                                          "LinearLayout/android.widget.ListView/android.widget."
                                          "LinearLayout/android.widget.LinearLayout/android.widget."
                                          "LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout").click()


        # except:
        #     self.driver.get_screenshot_as_file("../error_png.png")






