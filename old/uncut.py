import os,sys,re,docx
from docx import Document

path_org = "original"
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

for root,dirs,files in os.walk(path_aft):
    for file in files:
        all_file_path = os.path.join(root,file)
        file_name_and_format = os.path.splitext(all_file_path)
        if file_name_and_format[1] == '.txt':
            flag = 0
        else:
            flag = 1 

# 处理
file_list = os.listdir(path_aft)
norm_value_f = open( path_tmp + '\\' + 'norm_value zh.txt' ,'w+',encoding="utf-8-sig") 
line_part = '"'
line_count = 1
for name in file_list:
    if flag == 0:
        curr_f = open( path_aft+ '\\' + name ,'r',encoding="utf-8-sig") 
        for line in curr_f:
            if not re.search('^=+',line):
                line_part += line
            else:
                re_line = re.sub('\n','□',line_part)
                re_line = re.search('.+(?=□)',re_line).group(0) +'"\n'
                norm_value_f.write(re_line)
                line_part = '"'
    else:
        curr_d = docx.Document(path_aft+ '\\' + name)
        for line in curr_d.paragraphs:
            if not re.search('^=+',line.text):
                line_part += line.text
            else:
                re_line = re.sub('\n','□',line_part)
                re_line = re.search('.+(?=□)',re_line).group(0) +'"\n'
                norm_value_f.write(re_line)
                line_part = '"'
