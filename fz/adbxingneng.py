#-*-coding:utf-8-*-
import os,time
class Xingneng():
    def __init__(self):
        self.packagename="com.yougou"
        self.activity=".IndexActivity"


        #冷启动手机三个time
    # def getlengqidong(self,Time):
    def getlengqidong(self):
        a=os.popen("adb shell am start -W -S "+self.packagename+"/"+self.activity).readlines()
        print type(a[4])
        print a[4],a[5],a[6]
        return a[4],a[5],a[6]
        # for tmp in a:
        #     if Time in tmp:
        #         print tmp.split(":")[1]


    def getreqidong(self,Time):
        os.popen("adb shell am start -W -S " + self.packagename + "/" + self.activity).readlines()
        time.sleep(1)
        #点击home键
        os.popen("adb shell input keyevent 3")
        time.sleep(1)
        a = os.popen("adb shell am start -W " + self.packagename + "/" + self.activity).readlines()
        for tmp in a:
            if Time in tmp:
                return tmp.split(":")[1]


    def getCpu(self):
        a=os.popen("adb shell dumpsys cpuinfo|grep "+self.packagename).readlines()
        for tmp in a:
            return tmp.split(" ")[2]

    def getMen(self):
        a=os.popen("adb shell dumpsys meminfo|grep "+self.packagename).readlines()
        # print a[0]
        b=a[0].split(":")[0]
        return b

print Xingneng().getlengqidong()





# i=1
# while  i<8:
#     print "getMen" + Xingneng().getMen()
#     print "getCpu"+"  "+Xingneng().getCpu()
#     i += 1




# print "getMen"+Xingneng().getMen()
#
#
#
# print "getCpu"+"  "+Xingneng().getCpu()




# print "ThisTime"+Xingneng().getreqidong("ThisTime")
# print "TotalTime"+Xingneng().getreqidong("TotalTime")
# print "WaitTime"+Xingneng().getreqidong("WaitTime")


