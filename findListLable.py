import requests
import unittest
import json

class findListLable(unittest.TestCase):

    #为空时
    def test_null(self):
        url='https://cqatest.rkxch.com:32780/boquan/api/label/findListLabel?labelType=0'
        response = requests.get(url=url,headers={'Accept': 'application/json'})
        res = response.text
        # print(response.text)
        self.assertEqual(0,res['code'],'pass')
    #输入特殊字符
    def test_num1(self):
        pass
    #输入正常数字0
    def test_num2(self):
        pass
    #输入正常输入1
    def test_num3(self):
        pass

if __name__ == '__main__':
    unittest.main()