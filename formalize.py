import os,sys,re,docx
from docx import Document

path_org = "original"
path_otp = "output"
path_tmp = "process"
path_bfr = "tobetrans"
path_aft = "transed"

normed_f = open( path_tmp  + '\\' + 'norm_value zh'+'.txt' ,'r',encoding="utf-8-sig") 
on_f = open( path_tmp  + '\\' + 'norm_value'+'.txt' ,'r',encoding="utf-8-sig") 
original_f = open( path_tmp  + '\\' + 'value'+'.txt' ,'r',encoding="utf-8-sig") 
nm_f = open( path_tmp + '\\' + 'norm_misc'+'.txt' ,'r',encoding="utf-8-sig") 

formed_f = open( path_tmp + '\\' + 'form_value zh'+'.txt' ,'w+',encoding="utf-8-sig") 
check_f = open( path_tmp + '\\' + 'check'+'.txt' ,'w+',encoding="utf-8-sig") 
check_f.write('=======删除原文保存，运行fixer=======\n')
substance_L = nm_f.readlines()
original_L = original_f.readlines()
normed_L = normed_f.readlines()
on_L =  on_f.readlines()
error_count = 0
line_count = 0
for n_line in normed_L:
    n_line_re = re.search('.+(?=\n)', n_line)
    n_line = n_line_re.group(0)
    substance = re.search('.*(?=\\n)',substance_L[line_count]).group(0)
    substance_l = re.split('\*', substance)
    if substance_l != ['']:
        part_l = re.split('■|□|▲ *', n_line)
        re_line = part_l[0]
        if len(substance_l) == len(re.findall('■|□|▲ *',n_line)):
            for i in range(len(part_l)-1):
                re_line = re_line + substance_l[i] + part_l[i+1]
            formed_f.write(re_line + '"\n')
        else:
            print(str(line_count+1) +'行对应失败,保留原文')
            formed_f.write('⚠')
            check_f.write('参考:'+ on_L[line_count])
            check_f.write(str(line_count)+'|'+n_line+'\n')
            error_count += 1
    else:
        formed_f.write( n_line + '\n' )
    line_count += 1
print('共有'+str(error_count)+'个格式错误,占比'+ str(error_count/(line_count+1)*100) +'%。' )
print('可以忽略，也可以去check.txt内手动核对后运行fixer')