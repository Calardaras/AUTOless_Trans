import os,sys,re,docx
from docx import Document

path_org = "original\\english"
path_otp = "output\\simp_chinese"
path_tmp = "process"
path_bfr = "tobetrans"
path_aft = "transed"

normed_f = open( path_bfr + '\\' + 'norm_value'+'.txt' ,'r',encoding="utf-8-sig") 
nm_f = open( path_bfr + '\\' + 'norm_misc'+'.txt' ,'r',encoding="utf-8-sig") 

formed_f = open( path_bfr + '\\' + 'form_value'+'.txt' ,'w+',encoding="utf-8-sig") 


for n_line in normed_f:
    substance = re.search('.*(?=\\n)',nm_f.readline()).group(0)
    part_l = re.split('<αωα>', n_line)
    substance_l = re.split('\*', substance)
    re_line = part_l[0]
    if len(part_l) > 1:
        for i in range(len(part_l)-1):
            re_line = re_line + substance_l[i] + part_l[i+1]
    formed_f.write(re_line)
    