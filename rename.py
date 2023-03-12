import os,sys
import re
from shutil import copy
#获取文件列表
path_org = "original"
path_rename = 'renamed'
filename = ""
Org_dir = []
all_files = os.walk(path_org)
for root,dirs,files in all_files:
    for file in files:
        all_file_path = os.path.join(root,file)
        file_name_and_format = os.path.splitext(all_file_path)
        if file_name_and_format[1] == '.yml':
            Org_dir.append(all_file_path)
            old_name = all_file_path
            new_name = re.sub('_english','_simp_chinese',all_file_path)
            new_name = re.sub('original',path_rename,new_name)
            copy(old_name,new_name)