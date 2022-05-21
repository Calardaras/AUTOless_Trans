import os,sys,re,docx
from docx import Document

path_org = "original\\english"
path_otp = "output\\simp_chinese"
path_tmp = "process"

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
#拆分

# for content in contents_f:
#     curr_f = open( path_otp  + '\\' + re.search('.+(?=(_l_english))',re.search('^[^,]+', content).group(0)).group(0) + '_l_simp_chinese.yml','w+',encoding="utf-8-sig") 
#     curr_f.write('l_simp_chinese:')
#     end = re.search('[^,]+$', content).group(0)
document = Document(path_tmp + '\\' + 'tr_va.docx')
i = 0
j = 0
curr_f = open( path_otp  + '\\' + re.search('.+(?=(_l_english))',re.search('^[^,]+', file_name[i]).group(0)).group(0) + '_l_simp_chinese.yml','w+',encoding="utf-8-sig") 
curr_f.write('l_simp_chinese:\n')
for paragraph in document.paragraphs:
    if j< int(index[i])-1:
        curr_f.write(re.search('^[^(\n)]+',key_l[j]).group(0) +' '+ paragraph.text +'\n')
        j+=1
    else:
        curr_f.close()
        i+=1
        curr_f = open( path_otp  + '\\' + re.search('.+(?=(_l_english))',re.search('^[^,]+', file_name[i]).group(0)).group(0) + '_l_simp_chinese.yml','w+',encoding="utf-8-sig") 
        curr_f.write('l_simp_chinese:\n')