#-*-coding:utf-8-*-




from  appium import webdriver
import time




shouji = {}
shouji['platformName']='Android'
shouji['platformVersion']='8.1'
shouji['appPackage']='com.yougou'
shouji['appActivity']='.IndexActivity'
shouji['appWaitActivity']='.activity.MainActivity'
shouji['deviceName']='emulator-5554'
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", shouji)
time.sleep(5)
#点击首页的满299减30按钮，先定位大框架，在定位其中元素
driver.find_elements_by_id("com.yougou:id/ll_module")[2].find_element_by_id("com.yougou:id/imageView3").click()



#利用xpath定位，找到对应的classname,和对应的文本进行定位

# driver.find_element_by_xpath("//classname[@text='文本']").click()



