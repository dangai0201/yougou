#-*-coding:utf-8-*-
from fz.shoushicaozuo import Shoushi

from appium.webdriver.common.touch_action import TouchAction
from  appium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



shouji = {}
shouji['platformName']='Android'
shouji['platformVersion']='8.1'
shouji['appPackage']='com.yougou'
shouji['appActivity']='.IndexActivity'
shouji['appWaitActivity']='.activity.MainActivity'
shouji['deviceName']='WEENU18907106864'
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", shouji)
time.sleep(5)
#点击首页的满299减30按钮，先定位大框架，在定位其中元素
driver.find_elements_by_id("com.yougou:id/ll_module")[2].find_element_by_id("com.yougou:id/imageView3").click()
time.sleep(10)

driver.find_elements_by_id("com.yougou:id/product_name")[2].click()
# a =driver.find_elements_by_id("com.yougou:id/product_name")[2]
# for tmp in a:
#     print tmp.text
#长按
# TouchAction(driver).long_press(a).perform()
# #
# time.sleep(5)
#
# driver.find_element_by_id("com.yougou:id/iv_simiblargrid_btn").click()



time.sleep(5)
driver.find_element_by_id("com.yougou:id/tv_buy_now").click()





