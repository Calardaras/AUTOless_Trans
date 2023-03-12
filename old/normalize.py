import os,sys,re,docx
from docx import Document

path_org = "original"
path_otp = "output"
path_tmp = "process"
path_bfr = "tobetrans"
path_aft = "transed"

key_f = open( path_tmp + '\\' + 'key.txt' ,'r',encoding="utf-8-sig") 
value_f = open( path_tmp + '\\' + 'value.txt' ,'r',encoding="utf-8-sig") 
contents_f = open( path_tmp + '\\' + 'contents.txt' ,'r',encoding="utf-8-sig") 

nv_f = open( path_tmp + '\\' + 'norm_value'+'.txt' ,'w+',encoding="utf-8-sig") 
nm_f = open( path_tmp + '\\' + 'norm_misc'+'.txt' ,'w+',encoding="utf-8-sig") 

for line in value_f :
    patten1 = '(\$.+?\$|\[.+?\]|@.+?\!)+'
    patten2 = '(#[YGRTFE!]{1,2} *)+'
    patten3 = '(\\\\n)+'
    substance = re.findall( patten1 +'|'+patten2 +'|'+patten3 , line )
    re_line = re.sub( patten1 ,'■',line)
    re_line = re.sub( patten2 ,'▲',re_line)
    re_line = re.sub( patten3, '□',re_line)
    L = []
    for n in re.finditer( patten1 +'|'+patten2 +'|'+patten3 , line ):
        L.append(n.group(0))
    nm_f.write('*'.join(L)+'\n')
    nv_f.write(re_line)




