#查询代理商

import requests
import json
url='https://cqatest.rkxch.com:32780/boquan/api/family/findByCellphone?'
data={
    'cellPhone':13412345212,
    'baseId':120
}
response = requests.get(url=url,json=data,headers={'Accept': 'application/json'})

print (response.text)
