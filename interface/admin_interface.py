'''
管理员接口
'''

from db import models


# 管理员注册接口
def admin_register_interface(user, pwd):
    # 将用户数据保存到对象中，然后再将对象传给数据层
    #     admin_obj = models.Admin(user,pwd)
    #     print(admin_obj.__dict__)
    #     db_handler.save(admin_obj)
    # 返回注册成功

    # 判断用户是否存在
    admin_obj = models.Admin.select(user)
    if admin_obj:
        return False, '用户已存在'
    # 不存在则创建
    models.Admin(user, pwd)
    return True, '注册成功'


# 管理员登录接口
def admin_login_interface(username, password):
    # 判断用户是否存在
    admin_obj = models.Admin.select(username)

    # 若不存在，证明用户不存在，返回给视图层
    if not admin_obj:
        return False, '用户不存在'
    if password == admin_obj.pwd:
        return True, '登录成功'
    else:
        return False, '密码错误，请重新输入'


# 管理员创建学校接口
def create_school_interface(school_name, school_addr, admin_name):
    # 查看当前学校是否存在
    school_obj = models.School.select(school_name)

    # 若学校存在则返回False,学校已存在
    if school_obj:
        return False, '学校已存在'

    # 若不存在，则创建学校（由管理员来创建）
    admin_obj = models.Admin.select(admin_name)
    # 由管理员来调用创建学校的方法
    admin_obj.create_school(
        school_name, school_addr
    )
    # 返回创建的学校给视图层
    return True, f'[{school_name}]学校创建成功!'


# 管理员创建课程接口
def create_course_interface(school_name, course_name, admin_name):
    # 1.查看课程是否存在，获取学校对象列表中的课程
    school_obj = models.School.select(school_name)
    if school_name in school_obj.course_list:
        return False, '要创建的课程已存在'

    # 若不存在，则调用管理员对象创建课程
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_course(
        school_obj, course_name
    )
    return True, f'[{course_name}]课程创建成功'


# 管理员创建老师接口
def create_teacher_interface(teacher_name, admin_name, teacher_pwd='123'):
    # 判断老师是否存在
    teacher_obj = models.Teacher.select(teacher_name)
    # 若存在，则返回已存在
    if teacher_obj:
        return False, '老师已存在'

    # 不存在，则让管理员创建
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_teacher(teacher_name, teacher_pwd)
    return True, f'[{teacher_name}]老师创建成功！'
