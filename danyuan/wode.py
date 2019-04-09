#-*-coding:utf-8-*-

from appium import webdriver
import unittest

from fz.qidong import Qidong
from fz.shoushicaozuo import Shoushi
from log.logfz import Log
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
import sys





reload(sys)
sys.setdefaultencoding( "utf-8" )


class  Denglu(unittest.TestCase):
    def setUp(self):
        Log().info(u"点击我的按钮")
        self.driver.find_element_by_id("com.yougou:id/rl_toolbar_more").click()
        pass
    def tearDown(self):
        pass
    @classmethod
    def setUpClass(self):
        #启动app
        Log().info(u"打开软件")
        self.driver=Qidong().driver
        time.sleep(2)
        pass
    @classmethod
    def tearDownClass(self):
        pass
    # def test_001(self):
    #     # Log().info(u"点击我的按钮")
    #     # self.driver.find_element_by_id("com.yougou:id/rl_toolbar_more").click()
    #     Log().info(u"点击登录按钮")
    #     self.driver.find_element_by_id("com.yougou:id/login_btn").click()
    #     time.sleep(2)
    #     Log().info(u"点击账号密码登录")
    #     self.driver.find_element_by_id("com.yougou:id/tabLayout_putong").click()
    #     Log().info(u"输入账号")
    #     self.driver.find_element_by_id("com.yougou:id/editUserEmail").clear()
    #     self.driver.find_element_by_id("com.yougou:id/editUserEmail").send_keys("15712959187")
    #     Log().info(u"输入密码")
    #     self.driver.find_element_by_id("com.yougou:id/editPassword").send_keys("1")
    #     Log().info(u"点击登录按钮")
    #     self.driver.find_element_by_id("com.yougou:id/login").click()
    #     #吐司未解决
    #     # Shoushi().toast_text(u"请输入3-25位密码")
    #     # print Shoushi().toast_text(u"请输入3-25位密码")
    #     # self.assertEqual(t.text,u"请输入3-25位密码")
    #
    #     pass
    #点击设置按钮
    # def test_002(self):
    #     Log().info(u"点击设置按钮")
    #     self.driver.find_element_by_id("com.yougou:id/setup_copy").click()
    #     Log().info(u"点击关于")
    #     self.driver.find_element_by_id("com.yougou:id/more_item_new_about").click()
    #     Log().info(u"点击版本号")
    #     self.driver.find_element_by_id("com.yougou:id/textVersionsAdd").click()
    #     Log().info(u"获取弹框内容")
    #     a=self.driver.find_element_by_id("android:id/message").text
    #     print a
    #     Log().info(u"断言")
    #     self.assertEqual(a,u"当前已经是最新版本，祝您购物愉快")
    #     Log().info(u"点击按钮关闭弹框")
    #     self.driver.find_element_by_id("android:id/button1").click()
    #
    #     pass






