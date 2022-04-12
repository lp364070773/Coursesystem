'''
公共方法
'''

# 多用户登录认证装饰器
def auth(role):
    '''

    :param role:角色----》管理员、老师、学生
    :return:
    '''
    from core import admin, student, teacher
    # 登录认证装饰器
    def login_auth(func):

        def inner(*args,**kwargs):
            if role == 'admin':
                if admin.admin_info['user']:
                    res = func(*args,**kwargs)
                    return res
                else:
                    admin.login()

            elif role == 'student':
                if student.student_info['user']:
                    res = func(*args,**kwargs)
                    return res
                else:
                    student.login()
            elif role == 'teacher':
                if teacher.teacher_info['user']:
                    res = func(*args,**kwargs)
                    return res
                else:
                    teacher.login()
            else:
                print('当前角色没有权限')

        return inner
    return login_auth