'''
用于管理类
'''
from db import db_handler

class Base:
    def save(self):
        db_handler.save_data(self)

    @classmethod
    def select(cls, username):
        obj = db_handler.select_data(cls, username)
        return obj

# 管理员类
class Admin(Base):
    # def save(self):
    #     db_handler.save(self)
    #
    # @classmethod
    # def select(cls,user):
    #     obj = db_handler.select(cls,user)
    #     return obj
    def __init__(self,user,pwd):
        self.user = user
        self.pwd = pwd
        self.save()

    # 创建学校
    def create_school(self,school_name,school_addr):
        school_obj = School(school_name,school_addr)
        school_obj.save()

    # 创建课程
    def create_course(self,school_obj,course_name):
        # 1.调用课程类，实例化课程对象
        course_obj = Course(course_name)
        # 2.获取学校对象，讲课程对象保存到学校里
        school_obj.course_list.append(course_name)
        # 更新学校数据
        school_obj.save()
    # 创建老师
    def create_teacher(self,teacher_name,teacher_pwd):
        teacher_obj = Teacher(teacher_name,teacher_pwd)



# 学校类
class School(Base):
    def __init__(self,name,addr):
        # 必须写self.user,因为db_handler中的select_data统一
        self.user = name
        self.addr = addr
        # 每个学校有自己的课程
        self.course_list = []


class Student(Base):
    pass

class Course(Base):
    def __init__(self,course_name):
        self.user = course_name
        self.student_list = []
        self.save()

class Teacher(Base):
    def __init__(self,teacher_name,teacher_pwd):
        self.user = teacher_name
        self.pwd = teacher_pwd
        self.course_list_from_tea = []
        self.save()