import os,sys
import re
#获取文件列表
path_org = "original\\english"
path_otp = "output\\simp_chinese"
path_tmp = "process"

# 创建中间文件
key_f = open( path_tmp + '\\' + 'key.txt' ,'w+',encoding="utf-8") 
vaule_f = open( path_tmp + '\\' + 'vaule.txt' ,'w+',encoding="utf-8") 
contents_f = open( path_tmp + '\\' + 'contents.txt' ,'w+',encoding="utf-8") 
# 读取原始文件
# # os.listdir()方法获取文件夹名字，返回数组
file_name_list = os.listdir(path_org)
index = 1 
for crr_file in file_name_list:
    org_f = open( path_org + '\\' + crr_file ,'r',encoding="utf-8") 
    next(org_f) #跳过首行
    for line in org_f:  #通过迭代器访问
        if re.search('^( ?)#.+',line):
            continue
        else:
            if re.search('^( ?)[^#][^:]+?:[01]?',line):
                key_f.write(re.search('^( ?)[^#][^:]+?:[01]?',line).group(0)+'\n')
                vaule_f.write(re.search('(".*")',line).group(0)+'\n')
                index += 1
    contents_f.write(crr_file+','+str(index)+'\n')
