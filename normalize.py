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

curr_f = open( path_bfr + '\\' + 'norm_value'+'.txt' ,'w+',encoding="utf-8-sig") 
nm_f = open( path_bfr + '\\' + 'norm_misc'+'.txt' ,'w+',encoding="utf-8-sig") 

for line in value_f :
    substance = re.findall('\$.+?\$|\[.+?\]|\\\\n|@.+?\!|#[YGRTFE!]{1,2} *',line)
    re_line = re.sub('\$.+?\$|\[.+?\]|\\\\n|@.+?\!','<αωα>',line)
    re_line = re.sub('#[YGRTFE!]{1,2} *','{',re_line)
    nm_f.write('*'.join(substance)+'\n')
    curr_f.write(re_line)




