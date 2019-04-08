#-*-coding:utf-8-*-
#python单例模式
def singleton(cls):
    #定义一个字典
    a={}
    #*args,**kwargs适配符
    def _singleton(*args,**kwargs):
        if cls not in a:
            #将cls添加到字典内
            a[cls]=cls(*args,**kwargs)
        return a[cls]
    #外层函数返回至内层函数
    return  _singleton
#如果cls（修饰的变量），没有在字典内，则将修饰的变量添加到字典里
#无论字典内有无该变量则返回该变量

