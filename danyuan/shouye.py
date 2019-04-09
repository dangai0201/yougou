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



    # def test_001(self):
    #     self.driver.find_element_by_id("com.yougou:id/iv_101").click()
    #     time.sleep(2)
    #     a=self.driver.current_activity
    #     print a
    #     self.assertEqual(".activity.AHomeSecendActivity",a)
    #     pass
    # def test_002(self):
    #     self.driver.back()
    #     self.driver.find_element_by_id("com.yougou:id/imageView1").click()
    #     a1=self.driver.current_activity
    #     print a1
    #     self.assertEqual(".activity.Html5Activity",a1)
    #     self.driver.find_element_by_id("signEvent").click()
    #     pass
    # def test_003(self):
    #     #self.driver.find_element_by_id("com.yougou:id/textBack").click()
    #     Log().info(u"开始滑动")
    #     Shoushi().swipe_up(2)
    #     time.sleep(2)
    #     Shoushi().swipe_left(1)
    #     Log().info(u"点击商品")
    #     self.driver.find_element_by_id("com.yougou:id/imageView1").click()
    #     time.sleep(2)
    #     a=Shoushi().getCurrentActivity()
    #     print a
    #     self.assertEqual(".activity.CNewProductDetails",a)
    #     pass
    def test_004(self):
        #下拉刷新方法
        Shoushi().swipe_down(1)























if __name__ == '__main__':
    unittest.main()


