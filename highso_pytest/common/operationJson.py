import json
import os

proDir = os.path.split(os.path.realpath(__file__))[0]
jsonPath = r'/Users/scwlly/Desktop/automated_test/highso/highso_pytest/testdatafile/Header.json'

class OperationJson:
    def __init__(self, file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = jsonPath

    def open_json(self):
        """打开json文件
        :return:返回json文件数据
        """
        with open(self.file_name, 'r') as fp:
            data = json.load(fp)
            return data
            #fp.close()

    def key_get_data(self, key):
        """通过key值获取数据
        :param key: 需要获取的值对应的key
        :return:
        """
        data = self.open_json()[key]
        return data

if __name__ == "__main__":
    a = OperationJson()
    b = a.key_get_data("header")
    print(type(b))
    print(b)