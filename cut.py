import os,sys,re,docx
from docx import Document

path_org = "original\\english"
path_otp = "output\\simp_chinese"
path_tmp = "process"
path_bfr = "tobetrans"
path_aft = "transed"

key_f = open( path_tmp + '\\' + 'key.txt' ,'r',encoding="utf-8-sig") 
value_f = open( path_tmp + '\\' + 'value.txt' ,'r',encoding="utf-8-sig") 
contents_f = open( path_tmp + '\\' + 'contents.txt' ,'r',encoding="utf-8-sig") 

i = 0
count = 0
curr_f = open( path_bfr + '\\' + 'value_'+ str(i) +'.txt' ,'w+',encoding="utf-8-sig") 
curr_d = docx.Document()
for line in value_f :
    re_line = re.sub('\[.+?\]','αντι',line)
    re_line = re.sub('#[A-Z]','',re_line)
    re_line = re.sub('#!','',re_line)
    re_line = re.sub('\\n','',re_line)
    re_line = re_line + '\n'
    if count + len(re_line) < 100000:
        curr_f.write(re_line)
        curr_d.add_paragraph(re_line)
        count += len(re_line)
    else:
        curr_d.save(path_bfr + '\\' + 'value_'+ str(i) +'.docx')
        i += 1
        curr_f = open( path_bfr + '\\' + 'value_'+ str(i) +'.txt' ,'w+',encoding="utf-8-sig") 
        count = 0
        curr_f.write(re_line)
        curr_d.add_paragraph(re_line)
        count += len(re_line)
curr_d.save(path_bfr + '\\' + 'value_'+ str(i) +'.docx')