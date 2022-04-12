'''
老师视图
'''
from lib import common

teacher_info = {
    'user':None
}
# 老师登录
def login():
    pass

# 查看教授课程
@common.auth('teacher')
def check_course():
    pass


# 选择教授课程
@common.auth('teacher')
def choose_course():
    pass

# 查看课程下的学生
@common.auth('teacher')
def check_stu_from_course():
    pass

# 修改学生分数
@common.auth('teacher')
def change_score_from_student():
    pass


func_dict = {
    '1':login,
    '2':check_course,
    '3':choose_course,
    '4':check_stu_from_course,
    '5':change_score_from_student,

}

def teacher_view():
    while True:
        print('''
        1.登录
        2.查看授课教程
        3.选择授课教程
        4.查看课程下的学生
        5.修改学生分数
        ''')
        choice = input('请选择功能编号：').strip()
        if choice == 'q':
            break

        if choice not in func_dict:
            print('输入有误，请重新输入')
            continue
        func_dict.get(choice)()