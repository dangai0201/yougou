#-*-coding:utf-8-*-
import os
class Huoqushebeixinxi():
    #获取版本号
    def getAndroidVersion(self):
        a=os.popen("adb shell getprop ro.build.version.release").readlines()
        return a[0]
# print Huoqushebeixinxi().getAndroidVersion()
    #获取设备名称
    def getAndroidDevicesName(self):
        aa=os.popen("adb devices -l").readlines()
        for tmp in aa:
            if "model" in tmp:
                a=tmp.split(" ")
                for b in a:
                    if "device:" in b:
                        return b.split(":")[1]
    #获取设备唯一识别码
    def getdeviceId(self):
        aaa=os.popen("adb devices -l").readlines()
        return aaa[1].split(" ")[0]
# print Huoqushebeixinxi().getdeviceId()
