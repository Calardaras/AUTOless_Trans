import os,sys,re,docx
from docx import Document

path_org = "original\\english"
path_otp = "output\\simp_chinese"
path_tmp = "process"

# 读取中间文件
key_f = open( path_tmp + '\\' + 'key.txt' ,'r',encoding="utf-8") 
index_f = open( path_tmp + '\\' + 'index.txt' ,'r',encoding="utf-8") 

for indexes in index_f:
    curr_f = open( path_otp  + '\\' + re.search('.+(?=(_l_english))',re.search('^[^,]+', indexes).group(0)).group(0) + '_l_simp_chinese.yml','w+',encoding="utf-8") 
    curr_f.write('l_simp_chinese:')
# document = Document(path_tmp + '\\' + 'tr_va.docx')
# for paragraph in document.paragraphs:
#     print(paragraph.text)

