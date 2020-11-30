# coding=utf-8
import unittest
import time
from highso_pytest.common.HTMLTestRunnerNew import HTMLTestRunner
if __name__=='__main__':
    #定义要运行哪些用例
    test_dir = r"/Users/scwlly/Desktop/automated_test/highso/highso_pytest/testcase"
    now = time.strftime("%Y-%m-%d %H:%M:%S_")
    discover = unittest.defaultTestLoader.discover(test_dir,"test_order_pytest.py")
    runer = HTMLTestRunner( title="Highso_API",
                            description="测试结果:",
                            #定义报告输入路径
                            stream=open(r'/Users/scwlly/Desktop/automated_test/highso/highso_pytest/test_reporter/' + now +"report.html","wb"),
                            #save_last_try=True
                            )
    runer.run(discover)




