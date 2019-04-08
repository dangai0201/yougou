#-*-coding:utf-8-*-
from fz.qidong import Qidong
import time
import os



class Jietu():
    def __init__(self):
        self.driver = Qidong().driver

    def jietu(self):
        img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//jietu//'
        time1 = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        screen_save_path = img_folder + time1 + '.png'
        self.driver.get_screenshot_as_file(screen_save_path)
        pass


