import tablib

# data=[
#     ['百度','get','pass']
# ]
# headers=['url','method','expected']
# data = tablib.Dataset(*data,headers=headers,title='测试用例')
# print(data)
# print(data.json)
# # print(data.xlsx)
# print(data.xls)
#
# with open('data.xlsx','wb') as fp:
#     fp.write(data.xlsx)
# def api_tester():
#     print(
#         "正在测试{},请求方法{},响应结果".format(
#             url,method,expected
#         )
#     )

with open('data.xlsx','rb') as fp:
    data = tablib.import_set(fp.read(),format='xlsx')
    print(data[0])
    print(data.dict['url'])
    data.append(['手机报','post','fail'])
    # 插入一列
    data.append_col(['fail','fail'],headers='实际结果')
    # print(data)
    # print(data.json)
    #
    # for i in data.dict:
    #     print(data.dict)
    #     api_tester(*i.values())