import os,sys
import re
import deepl
auth_key = "f63c02c5-f056-..."  # Replace with your key
translator = deepl.Translator(auth_key)

#获取文件列表
path_org = "original"
path_otp = "output"
path_tmp = "process"
path_bfr = "tobetrans"
path_aft = "transed"

def file_search_to_list(path):
    L = []
    for root,dirs,files in os.walk(path):
        for file in files:
            all_file_path = os.path.join(root,file)
            file_name_and_format = os.path.splitext(all_file_path)
            if file_name_and_format[1] == '.yml':
                L.append(all_file_path)
    return L


# 创建中间文件
key_f = open( path_tmp + '\\' + 'key.txt' ,'w+',encoding="utf-8-sig") 
vaule_f = open( path_tmp + '\\' + 'value.txt' ,'w+',encoding="utf-8-sig") 
contents_f = open( path_tmp + '\\' + 'contents.txt' ,'w+',encoding="utf-8-sig") 
# 读取原始文件
file_name_list = file_search_to_list(path_org)
index = 1 
for crr_file in file_name_list:
    org_f = open( crr_file ,'r',encoding="utf-8-sig") 
    print('正在处理'+crr_file)
    new_name = re.sub('_english','_simp_chinese',crr_file)
    result_f = open(new_name,"w",encoding="utf-8-sig")
    for line in org_f:  #通过迭代器访问
        comm_check = re.match('^( *)#+',line)
        if comm_check != None:
            continue
        else:
            key_check = re.search('^( ?)[^#][^:]+?:\d?',line)
            head_check = re.search('l_english',line)
            if key_check != None and head_check == None:
                key = re.search('^( ?)[^#][^:]+?:\d?',line).group(0)+'\n'
                vaule = re.search('".*"',line).group(0)+'\n'
                result = translator.translate_text(vaule, target_lang="EN")
                result_f.write(key+result)
