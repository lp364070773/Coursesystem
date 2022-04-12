# 保存数据
import os,pickle
from conf import settings

def save_data(obj):
    # 获取对象的类，在获取类名
    class_name = obj.__class__.__name__
    user_dir_path = os.path.join(
        settings.DB_PATH,class_name
    )
    # 判断文件夹是否存在，没有则创建
    if not os.path.isdir(user_dir_path):
        os.mkdir(user_dir_path)
# 拼接文件 用户文件路径，以用户名作为文件名字

    user_path = os.path.join(
        user_dir_path,obj.user
    )
    # 保存对象 pickle数据
    with open(user_path ,'wb') as f:
        pickle.dump(obj,f)
# 查看数据
def select_data(cls,username):
    user_dir = os.path.join(
        settings.DB_PATH, cls.__name__,username
    )

    if os.path.exists(user_dir):
        # 查找对象 数据
        with open(user_dir, 'rb') as f:
            obj = pickle.load(f)
            return obj