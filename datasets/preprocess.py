import os
import re
import shutil

def remove_chinese(text):
    # 使用正则表达式匹配中文字符
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    # 用空字符串替换中文字符
    return re.sub(pattern, '', text)

def process_folder(source_folder, target_folder):
    # 获取文件夹中的所有文件
    files = os.listdir(source_folder)
    # 用于跟踪现有文件名，避免重复
    existing_names = set()

    # 收集所有图片文件的名称
    image_names = [file for file in files if file.lower().endswith(('.bmp', '.png', '.jpeg'))]

    for file_name in image_names:
        # 判断文件名是否包含中文
        if re.search('[\u4e00-\u9fa5]', file_name):
            # 去掉中文部分并确保新名称不会与已有的文件名重复
            new_name = remove_chinese(file_name)
            while new_name in existing_names:
                # 如果已存在，加入编号
                new_name = f"{new_name}_1"
            existing_names.add(new_name)

            # 进行重命名
            old_path = os.path.join(source_folder, file_name)
            new_path = os.path.join(target_folder, new_name)
            os.rename(old_path, new_path)
            print(f'Renamed: {file_name} -> {new_name}')

            # 移动重命名后的图片到目标文件夹
            shutil.move(new_path, os.path.join(target_folder, new_name))

# 要处理的文件夹路径和目标文件夹路径
source_folder = 'E:/yolov8/datasets/train/ng'
target_folder = 'E:/yolov8/datasets/train/ng'

# 确保目标文件夹存在
os.makedirs(target_folder, exist_ok=True)

process_folder(source_folder, target_folder)
