import os,sys,re,docx
from docx import Document

path_org = "original\\english"
path_otp = "output\\simp_chinese"
path_tmp = "process"

key_f = open( path_tmp + '\\' + 'key.txt' ,'r',encoding="utf-8-sig") 
vaule_f = open( path_tmp + '\\' + 'vaule.txt' ,'r',encoding="utf-8-sig") 
contents_f = open( path_tmp + '\\' + 'contents.txt' ,'r',encoding="utf-8-sig") 

i = 0
count = 0
curr_f = open( path_tmp + '\\' + 'vaule_'+ str(i) +'.txt' ,'w+',encoding="utf-8-sig") 
for line in vaule_f :
    if count + len(line) < 10000:
        curr_f.write(line)
        count += len(line)
    else:
        i += 1
        curr_f = open( path_tmp + '\\' + 'vaule_'+ str(i) +'.txt' ,'w+',encoding="utf-8-sig") 
        count = 0
        curr_f.write(line)
        count += len(line)