#-*-coding:utf-8-*-
from  appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
from fz.shoushicaozuo import Shoushi
from  fz.jietu import Jietu
from log.lianxi123 import Logger
from selenium.webdriver.support.ui import WebDriverWait
import os






# 解决appium setting ,unlock多次安装问题
# 博客地址：https://www.jianshu.com/p/77bd2418d00d(解决)
# https://blog.csdn.net/jackeny37/article/details/78930338（尝试）
# https://blog.csdn.net/wen61995120/article/details/80310994（尝试）



# class Xianxing(object):
#     def shoujixinxi(self):
#         self.shouji={}
#         #平台
#         self.shouji['platformName']='Android'
#         self.shouji['platformVersion']='8.1'
#         self.shouji['app']="/Users/yuliguo/Downloads/bailiyougou_100083.apk"
#         self.shouji['noReset'] = False
#
#         self.shouji['appPackage']='com.tencent.wstt.gt'
#
#         self.shouji['appActivity']='.activity.SplashActivity'
#         # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
#         self.shouji['unicodeKeyboard']='true'
#         # 是否在测试结束后将键盘重轩为系统默认的输入法。
#         self.shouji['resetKeyboard']='true'
#         # Appium服务器待appium客户端发送新消息的时间。默认为60秒
#         self.shouji['newCommandTimeout']='120'
#         self.shouji['deviceName']='WEENU18907106864'
#         # true:不重新安装APP，false:重新安装app
#
#         self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.shouji)
#         time.sleep(5)
#
#
#
#
#
# Xianxing().shoujixinxi()
# class AppiumTest:
#     def __init__(self):
#         desired_caps = {'platformName': 'Android',
#                         'platformVersion': '8.1',
#                         'deviceName': 'WEENU18907106864',
#                         'appPackage': 'com.tencent.wstt.gt',
#                         'appActivity': '.activity.SplashActivity'}
#
#         self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#         self.driver.implicitly_wait(30)
#
#     def get_driver(self):
#         return self.driver



# shouji = {}
# shouji['platformName']='Android'
# shouji['platformVersion']='8.1'
# shouji['appPackage']='com.yougou'
# shouji['appActivity']='.IndexActivity'
# shouji['appWaitActivity']='.activity.MainActivity'
# Logger().log(shouji['appWaitActivity'])
# shouji['deviceName']='WEENU18907106864'
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", shouji)
#
#
# toast_message = u"请输入3-25位密码"
# message ='//*[@text=\'{}\']'.format(toast_message)
#
# # 获取toast提示框内容
# toast_element = WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath(message))
# print(toast_element.text)


# Logger().log(u"启动完成")

#不支持读取操作
# os.system("adb devices")
#读取并输出
# out=os.popen("adb devices").read()
# print out


#获取app包名
# adb shell logcat|grep START

#获得打开指定页面时间
# adb shell logcat|grep ActivityManager

#查看当前 activity
# adb shell dumpsys window | grep mCurrentFocus


#从设备复制文件
# adb pull remote local


#复制文件到设备
# adb push local remote

# eg:adb push foo.txt /sdcard/foo.txt

# 将日志以文件形式输出到手机设备上，会阻塞，需手动 (Ctrl + C) 停止
# adb logcat -f /sdcard/log.txt



# -- V : Verbose (明细);
# -- D : Debug (调试);
# -- I : Info (信息);
# -- W : Warn (警告);
# -- E : Error (错误);
# -- F : Fatal (严重错误);
# -- S : Silent(Super all output) (最高的优先级, 可能不会记载东西);
# 过滤指定等级以上的日志
# adb logcat "*:<level>"
# eg:adb logcat "*:E"

#统计冷启动app的时间
# adb shell am start -W -S 包名/activity
#eg:adb shell am start -W -S com.yougou/.IndexActivity
#热启动
# adb shell am start -W 包名/activity


#查看设备所有第三方应用包名
# adb shell pm list package -3

# 清除指定应用的所有数据（不卸载应用）
# adb shell pm clear com.package.name

# 强制关闭应用
# adb shell am force-stop com.yougou"


# 查看cpu占用
# adb shell dumpsys cpuinfo |grep 包名

#查看实时内存资源占用情况
# adb shell top

# 查看指定应用的内存信息
#adb shell dumpsys meminfo com.package.name

#查看gpu
# adb shell dumpsys gfxinfo 包名



#查看指定app的pid
# adb shell ps | grep 包名

#根据pid查询流量
#adb shell cat /proc/PID/net/dev


#耗电量
# adb shell dumpsys battery


#指定app的耗电量
# adb shell dumpsys batterystats |grep "包名"
os.system("adb shell dumpsys batterystats |grep com.yougou")
out1=os.popen("adb shell dumpsys batterystats |grep com.yougou").read()
print out1

















