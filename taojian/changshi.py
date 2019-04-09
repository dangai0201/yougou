#-*-coding:utf-8-*-
import unittest
from  danyuan.shouye import Denglu
from baogao.baogao import Baogao


class Taojian():
    def test_001(self):
        # 1.创建一个空的测试套件
        # 2.添加测试用例
        # 3.执行测试套件
        nba = unittest.TestSuite()

        #执行该模块下方的所有用例
        nba.addTest(unittest.makeSuite(Denglu))
        #unittest.TextTestRunner().run(nba)
        Baogao().getbaogao(u"报告", u"优购", u"移动端首页",nba)

        pass



if __name__ == '__main__':
    Taojian().test_001()
