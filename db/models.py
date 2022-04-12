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
    def create_course(self):
        pass
    # 创建老师
    def create_teacher(self):
        pass

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
    pass

class Teacher(Base):
    pass