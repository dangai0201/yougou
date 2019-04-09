#-*-coding:utf-8-*-
from fz.qidong import Qidong
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Shoushi():
    def __init__(self):
        self.driver = Qidong().driver

    def swipe_up(self,n):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.5  # x坐标
        y1 = s['height'] * 0.75  # 起点y坐标
        y2 = s['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2,duration=time.sleep(1))

    # 向下滑动
    def swipe_down(self,n):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.5  # x坐标
        y1 = s['height'] * 0.25  # 起点y坐标
        y2 = s['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, duration=time.sleep(1))


    # 向左滑动
    def swipe_left(self,n):
        s = self.driver.get_window_size()
        x1 = s['width'] * 0.75
        y1 = s['height'] * 0.5
        x2 = s['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, duration=time.sleep(1))

    # 向右
    def swipe_right(self,n):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, duration=time.sleep(1))





    # 获取当前activity的方法
    def getCurrentActivity(self):
        return self.driver.current_activity

    #获取toast
    # def toast_text(self, text):
    #
    #     try:
    #
    #         toast_loc = (By.XPATH, "//*[contains(@text,'" + text + "')]")
    #
    #         ele = WebDriverWait(self.driver, 10, 0.01).until(EC.presence_of_element_located(toast_loc))
    #
    #         print(ele.text)
    #
    #         return ele.text
    #
    #     except:
    #
    #         return None




