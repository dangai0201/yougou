#-*-coding:utf-8-*-
from appium import webdriver
import time
from fz.danli import singleton

@singleton
class Qidong():
    def __init__(self):
        self.shouji = {}
        self.shouji['platformName']='Android'
        self.shouji['platformVersion']='8.1'
        self.shouji['appPackage']='com.yougou'
        self.shouji['appActivity']='.IndexActivity'
        self.shouji['appWaitActivity']='.activity.MainActivity'
        self.shouji['deviceName']='WEENU18907106864'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.shouji)







