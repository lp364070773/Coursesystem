'''
管理员视图
'''
# 管理员注册
from interface import admin_interface
from lib import common

admin_info = {
    'user': None
}
def register():
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        re_password = input('请确认密码：').strip()
        if password == re_password:
#             调用管理员接口进行注册
            flag,msg = admin_interface.admin_register_interface(
                username,password
            )
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致，请重新输入！')
            continue

# 管理员登录
def login():
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()

        # 调用管理员登录接口

        flag,msg = admin_interface.admin_login_interface(
            username,password
        )

        if flag:
            print(msg)
            # 记录用户登录状态（可变类型不需要global）
            admin_info['user'] = username
            break
        else:
            print(msg)
# 管理员创建学校
@common.auth('admin')
def create_school():
    while True:
        # 让用户输入学校名称和地址

        school_name = input('请输入学校名称：').strip()
        school_addr = input('请输入学校地址：').strip()

        # 调用接口，保存学校
        flag,msg = admin_interface.create_school_interface(
            # 学校名、学校地址、创建学校的管理员
            school_name,school_addr,admin_info.get('user')
        )
        if flag:
            print(msg)
        else:
            print(msg)
# 管理员创建课程

@common.auth('admin')
def create_course():
    pass

# 管理员创建老师
@common.auth('admin')
def create_teacher():
    pass



func_dict = {
    '1':register,
    '2':login,
    '3':create_school,
    '4':create_course,
    '5':create_teacher,

}
'''
管理员视图 函数
'''
def admin_view():
    while True:
        print('''
        1.管理员注册
        2.管理员登录
        3.创建学校
        4.创建课程
        5.创建老师
        ''')
        choice = input('请选择功能编号：').strip()
        if choice == 'q':
            break

        if choice not in func_dict:
            print('输入有误，请重新输入')
            continue
        func_dict.get(choice)()