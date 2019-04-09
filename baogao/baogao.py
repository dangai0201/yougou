#-*-coding:utf-8-*-
import os,sys
os.getcwd()
sys.path.append(os.getcwd())
import HTMLTestRunner

import time
from fz.qidong import Qidong




class Baogao():
    def __init__(self):
        self.driver=Qidong().driver

    def getbaogao(self,file,title,desc,ceshitaojian):

        #1.打开或者创建一个新的测试报告
        #将测试结果写入到测试报告内
        time1 = time.strftime("%Y-%m-%d %H-%M", time.localtime())
        print (time1)

        filename="../baogao/"+time1+file+".html"


        with open(filename,'wb') as aa:
            HTMLTestRunner.HTMLTestRunner(stream=aa, verbosity=1, title=title, description=desc).run(ceshitaojian)
