import os, shutil,re

def file_search_to_list(path):
    L = []
    for root,dirs,files in os.walk(path):
        for file in files:
            all_file_path = os.path.join(root,file)
            file_name_and_format = os.path.splitext(all_file_path)
            if file_name_and_format[1] == '.yml':
                L.append(all_file_path)
    return L

para_files = file_search_to_list("para")
renamed_files = file_search_to_list("renamed")
orginal_key_list = []
orginal_value_list = []

for file in renamed_files:
    org_f = open( file ,'r',encoding="utf-8-sig") 
    for line in org_f:  #通过迭代器访问
        comm_check = re.match('^( *)#+',line)
        if comm_check != None:
            continue
        else:
            key_check = re.search('^( ?)[^#][^:]+?:\d?',line)
            head_check = re.search('l_english',line)
            if key_check != None and head_check == None:
                key = re.search('^( ?)[^#][^:]+?:\d?',line).group(0)
                if re.search('^ +',key) != None:
                    key = re.sub(re.search('^ +',key).group(0),'',key)
                orginal_key_list.append(key)
                value = re.search('".*"',line).group(0)
                orginal_value_list.append(value)

for dir in para_files:
    check = re.search('(?<=para\\\\).+(?=[\\\\])', dir)
    if check:
        root1 = 'diff_org\\' + check.group(0)
        root2 = 'diff_para\\' + check.group(0)
        if not os.path.exists(root1):
            os.makedirs(root1)
        else:
            os.removedirs(root1)
            os.makedirs(root1)
        if not os.path.exists(root2):
            os.makedirs(root2)
        else:
            os.removedirs(root2)
            os.makedirs(root2)

for file in para_files:
    org_f = open( file ,'r',encoding="utf-8-sig")
    diff_ch = re.sub("para","diff_org",file)
    diff_en = re.sub("para","diff_para",file)
    diff_f_data = ''
    diff_f_org_data = ''
    print('正在处理'+ file )
    for line in org_f:  #通过迭代器访问
        comm_check = re.match('^( *)#+',line)
        if comm_check != None:
            continue
        else:
            key_check = re.search('^( ?)[^#][^:]+?:\d?',line)
            head_check = re.search('l_simp_chinese:',line)
            if key_check != None and head_check == None:
                key = re.search('^( ?)[^#][^:]+?:\d?',line).group(0)
                if re.search('^ +',key) != None:
                    key = re.sub(re.search('^ +',key).group(0),'',key)
                value = re.search('".*"',line).group(0)
                if key in orginal_key_list:
                    index = orginal_key_list.index(key)
                    patten1 = '(\$.+?\$|\[.+?\]|@.+?\!)+'
                    patten2 = '(#[YGRTFE!]{1,2} *)+'
                    patten3 = '(\\\\n)+'
                    substance_1 = re.findall( patten1 +'|'+patten2 +'|'+patten3 , value )
                    substance_2 = re.findall( patten1 +'|'+patten2 +'|'+patten3 , orginal_value_list[index] )
                    if len(substance_1) != len(substance_2):
                        diff_f_data += key+value+"\n"
                        diff_f_org_data += key+orginal_value_list[index]+"\n"
    if diff_f_data != '':
        diff_f = open( diff_ch,'w+',encoding="utf-8-sig")
        diff_f.write(diff_f_org_data)
        diff_f_org = open( diff_en,'w+',encoding="utf-8-sig")
        diff_f_org.write(diff_f_data)

    
                

