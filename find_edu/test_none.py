import requests
import unittest
import json

class find_edu(unittest.TestCase):

    def test_none(self):
        # 空
        url='http://jzsjb.net.cn:9080/studypaper/app/schoolAdmission/selectSchoolAdmissionById'
        response = requests.get(url,params=None)
        jsondata = response.json()
        # if jsondata['msg']=='ok' and response.status_code==200:
        #     print('接口通过')
        # elif jsondata['data'] is None:
        #     print('接口通过')
        # else:
        #     print('接口有误')
        self.assertEqual(response.status_code,200)
        self.assertEqual(jsondata['msg'],'OK')
        self.assertEqual(jsondata['data'],None)
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest("test_none")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)