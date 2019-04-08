#-*-coding:utf-8-*-

from  appium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



shouji = {}
shouji['platformName']='Android'
shouji['platformVersion']='9'
shouji['appPackage']='com.yougou'
shouji['appActivity']='.IndexActivity'
shouji['appWaitActivity']='.activity.MainActivity'
shouji['deviceName']='emulator-5554'
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", shouji)


#点击坐标
time.sleep(5)
driver.tap([(864,1668),(1080,1794)],100)
time.sleep(2)
driver.tap([(356,181),(724,286)],100)
time.sleep(2)
driver.tap([(622,297),(856,370)],100)


# time.sleep(2)
# driver.find_element_by_id("com.yougou:id/rl_toolbar_more").click()
# time.sleep(2)
#
# driver.find_element_by_id("com.yougou:id/login_btn").click()

# driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView").click()
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.EditText").send_keys("15712959187")
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout[3]/android.widget.RelativeLayout[2]").send_keys("1")

# driver.find_element_by_id("com.yougou:id/login").click()


i=0
while i <3:
    driver.find_element_by_id("com.yougou:id/login").click()
    i+=1
    toast_loc = (By.XPATH, ".//*[contains(@text,'请输入3-25位密码')]")

    WebDriverWait(driver, 30, 0.1).until(EC.presence_of_element_located(toast_loc))

    str = driver.find_element_by_xpath(".//*[contains(@text,'请输入3-25位密码')]").text

    print str
    print i















