#系统入口
from common.commongoodcard import _register,_login,goodCarFun

if __name__ == '__main__':
    flag = True
    while flag:
        #1. 进入系统首页，打印功能菜单
        print('=================欢迎进入购物车系统=====================')
        print('*********************系统功能***************************')
        print('1、账号注册')
        print('2、登录')
        print('q、退出')
        print('=======================================================')

        #2. 获取用户输入
        cmd = input('请选择功能：')

        #3. 判断用户输入
        if cmd =='1':
            #注册
            _register()

        elif cmd == '2':
            #登录
            name = input('请输入账号：')
            pwd = input('请输入密码：')
            reslut = _login(name,pwd)
            if reslut==0:
                print('登录失败！')
            else:
                print('登录成功！')
                #进入购物车
                goodCarFun()

        elif cmd == 'q':
            #退出系统
            flag = False

        else:

            print('您的输入有误，请重新输入，请输入1,2或q!')



















