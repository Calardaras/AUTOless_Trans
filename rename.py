import os,sys
import re
#获取文件列表
path_org = "original"
path_otp = "output"
path_tmp = "process"
path_bfr = "tobetrans"
path_aft = "transed"
path_rnm = "renamed"

Org_dir = []
for root,dirs,files in os.walk(path_org):
    for file in files:
        all_file_path = os.path.join(root,file)
        file_name_and_format = os.path.splitext(all_file_path)
        if file_name_and_format[1] == '.yml':
            Org_dir.append(all_file_path)
            os.renames(all_file_path,re.sub('_english','_simp_chinese',all_file_path))