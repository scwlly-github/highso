#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import allure
import sys
sys.path.append(r"/Users/scwlly/Desktop/automated_test/highso")
import os,json
import unittest
from highso_pytest.common.readTestData import ReadTestData
from highso_pytest.common.myLog import MyLog
from highso_pytest.config.readConfig import ReadConfig
from highso_pytest.common.httpSet import HttpMethod

proDir = os.path.split(os.path.realpath(__file__))[0]
file_name = os.path.join(proDir,r"/Users/scwlly/Desktop/automated_test/highso/highso_pytest/testdatafile/Test_highso.json")

# @allure.feature("下单")
class Test_order(unittest.TestCase):
    def setUp(self):
        self.http = HttpMethod()
        self.config = ReadConfig()
        self.data = ReadTestData(file_name)
        self.hea_data = ReadTestData()
        self.sheet = 'order'
        # 2,4代表读取excel的开始行数和结束行数
        self.row = list(range(2, 4))
        self.log = MyLog()
        self.log.info(message="--测试开始--",name="test_order_pytest.py")

    def tearDown(self):
        self.log.info(message="--测试结束--",name="test_order_pytest.py")
    # @allure.story("test_01")
    def test_01(self):
        u"正确参数下单"
        # 获取参数
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[0])
        header = self.hea_data.get_header(self.sheet, self.row[0])
        data = self.data.get_request_data(self.sheet, self.row[0])
        expect = self.data.get_expect_result(self.sheet, self.row[0])
        method = self.data.get_method(self.sheet, self.row[0])
        data["crmOrderCreateRequest"] = json.dumps(data["crmOrderCreateRequest"])
        self.log.info(message="获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        # 发送请求
        status_code,self.res = self.http.http_method(method=method,url=url, data=data,headers=header)
        # 断言
        assert status_code == 200,"实际返回值为：%s" % status_code
        assert self.res['success'] == expect['success'] ,"实际返回值为：%s" % self.res['success']
        self.log.info(message="断言")

    def test_02(self):
        u"错误商品ID下单"
        # 获取参数
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[1])
        header = self.hea_data.get_header(self.sheet, self.row[1])
        data = self.data.get_request_data(self.sheet, self.row[1])
        expect = self.data.get_expect_result(self.sheet, self.row[1])
        method = self.data.get_method(self.sheet, self.row[1])
        data["crmOrderCreateRequest"] = json.dumps(data["crmOrderCreateRequest"])
        self.log.info(message="获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="请求接口：%s" % url)
        self.log.info(message="请求数据：%s" % data)
        # 发送请求
        status_code,self.res = self.http.http_method(method=method,url=url, data=data,headers=header)
        # 断言
        assert status_code == 200,"实际返回值为：%s" % status_code
        assert self.res['success'] == expect['success'] ,"实际返回值为：%s" % self.res['success']
        assert self.res['msg'] == expect['msg'],"实际返回值为：%s" % self.res['msg']
        self.log.info(message="断言")

if __name__ == '__main__':
    unittest.main()
