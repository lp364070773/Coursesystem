'''
公共接口
'''
import os
from conf import settings


# 获取所有学校名称接口
def get_all_school_interface():
    school_dir = os.path.join(
        settings.DB_PATH, 'School'
    )

    # 判断文件夹是否存在

    if not os.path.exists(school_dir):
        return False, '没有学校，请联系管理员'

    # 若存在，则获取文件中所有文件的名字

    school_list = os.listdir(school_dir)
    return True, school_list
