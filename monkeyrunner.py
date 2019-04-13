#-*-coding:utf-8-*-
#循环monkeyrunner进行运行
import os
import time
import math
for i in range(1,6):
    #启动app
    os.system("adb shell am start -n com.yougou/.IndexActivity")
    time.sleep(5)
    print ("第"+str(i)+"次执行")
    os.system("monkeyrunner /Users/yuliguo/Desktop/monkeyrunner/playback.py /Users/yuliguo/Desktop/monkeyrunner/bbb ")
    time.sleep(5)
    #关闭app
    os.system("adb shell am force-stop com.yougou")
    if i==5:
        print u"执行完成"
