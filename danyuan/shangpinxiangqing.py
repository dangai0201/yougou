#-*-coding:utf-8-*-
from appium import webdriver
import unittest

from fz.qidong import Qidong
from fz.shoushicaozuo import Shoushi
from log.logfz import Log

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
        Log().info(u"打开软件")
        self.driver=Qidong().driver
        pass
    @classmethod
    def tearDownClass(self):
        pass

    def test_001(self):
        Log().info(u"开始滑动")
        Shoushi().swipe_up(2)
        time.sleep(2)
        Log().info(u"点击商品")
        self.driver.find_element_by_id("com.yougou:id/imageView1").click()
        time.sleep(5)
        Log().info(u"点击去结算")
        self.driver.find_element_by_id("com.yougou:id/tv_buy_now").click()
        Log().info(u"选择颜色和大小")
        self.driver.find_elements_by_id("com.yougou:id/iv")[0].click()
        self.driver.find_elements_by_id("com.yougou:id/cs_size_tag_layout")[0].click()







        pass
