import os,sys,re,docx
from docx import Document

path_org = "original\\english"
path_otp = "output"
path_tmp = "process"
path_bfr = "tobetrans"
path_aft = "transed"

# 读取中间文件
key_f = open( path_tmp + '\\' + 'key.txt' ,'r',encoding="utf-8-sig") 
key_l = list(key_f)
key_f.close()
contents_f = open( path_tmp + '\\' + 'contents.txt' ,'r',encoding="utf-8-sig") 

#处理目录和引索
file_name =[]
index = []
for content in contents_f:
    file_name.append(re.search('^[^,]+', content).group(0))
    index.append(re.search('[^,]+$', content).group(0))
contents_f.close()

# 处理
file_list = os.listdir(path_aft)
norm_value_f = open( path_tmp + '\\' + 'norm_value zh.txt' ,'w+',encoding="utf-8-sig") 
for name in file_list:
    curr_f = open( path_aft+ '\\' + name ,'r',encoding="utf-8-sig") 
    for line in curr_f:
        norm_value_f.write(line)
