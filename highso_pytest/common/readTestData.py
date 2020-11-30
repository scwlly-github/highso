# coding=utf-8
from highso_pytest.common.operationJson import OperationJson
from highso_pytest.common.operationExcelSheet import OperationExcel
from highso_pytest.config.readConfig import ReadConfig
false = False
true = True


class ReadTestData:
    def __init__(self, file_name=None):
        self.open_excel = OperationExcel()
        self.set_excel = ReadConfig()
        if file_name:
            self.open_json = OperationJson(file_name)
        else:
            self.open_json = OperationJson()

    def get_request_data(self, sheet_name, row):
        cell = self.set_excel.get_excel('data')
        request_key = self.open_excel.from_ab_get_data(sheet_name, cell, row)
        # request_list = request_str.split(',')
        # print(request_list)
        request_data = self.open_json.key_get_data(request_key)
        return request_data

    def get_header(self, sheet_name, row):
        cell = self.set_excel.get_excel('header')
        headers_key = self.open_excel.from_ab_get_data(sheet_name, cell, row)
        headers = self.open_json.key_get_data(headers_key)
        return headers

    def get_param(self, sheet_name, row):
        cell = self.set_excel.get_excel('param')
        param = self.open_excel.from_ab_get_data(sheet_name, cell, row)
        request_param = self.open_json.key_get_data(param)
        return request_param

    def get_method(self, sheet_name, row):
        cell = self.set_excel.get_excel('method')
        method = self.open_excel.from_ab_get_data(sheet_name, cell, row)
        return method

    def get_expect_result(self, sheet_name, row):
        cell = self.set_excel.get_excel('expected')
        expect_result = self.open_excel.from_ab_get_data(sheet_name, cell, row)
        expect_result_dict = eval(expect_result)
        return expect_result_dict

    def get_url(self, sheet_name, row):
        cell = self.set_excel.get_excel('url')
        url = self.open_excel.from_ab_get_data(sheet_name, cell, row)
        return url



if __name__ == "__main__":
    file_name = "/Users/scwlly/Desktop/automated_test/highso/highso_pytest/testdatafile/Test_highso.json"
    a = ReadTestData(file_name)
    b = a.get_param('order', 48)
    print(type(b))
    print(b)
