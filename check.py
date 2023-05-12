########
# 纠错 

import json,os, shutil,re

def file_search_to_list(path):
    L = []
    for root,dirs,files in os.walk(path):
        for file in files:
            all_file_path = os.path.join(root,file)
            file_name_and_format = os.path.splitext(all_file_path)
            if file_name_and_format[1] == '.json':
                L.append(all_file_path)
    return L

raw_files = file_search_to_list("raw")
for dir in raw_files:
    check = re.search('(?<=raw\\\\).+(?=[\\\\])', dir)
    if check:
        root1 = 'diff_org\\' + check.group(0)
        root2 = 'diff_para\\' + check.group(0)
        if not os.path.exists(root1):
            os.makedirs(root1)
        else:
            shutil.rmtree(root1)
            os.makedirs(root1)
        if not os.path.exists(root2):
            os.makedirs(root2)
        else:
            shutil.rmtree(root2)
            os.makedirs(root2)

pattens = ['\$[^\$]+?\$',
          '\[[^\]]+?\]',
          '@.+?\!',
          '#[YGRTFE]{1,2} ',
          '#!',
          '\\\\n']

for file in raw_files:
    raw_file = open(file,'r',encoding="utf-8-sig")
    data = json.load(raw_file)
    diff_ch = re.sub("raw","diff_org",file)
    diff_ch = re.sub(".json",'',diff_ch)
    diff_en = re.sub("raw","diff_para",file)
    diff_en = re.sub(".json",'',diff_en)
    diff_f_data = ''
    diff_f_org_data = ''
    print('正在处理'+ file )
    for item in data:
        if item["stage"]!= -1 and item["stage"]!= 0:
            if item["key"] == "COUNTRY_DESCRIPTIVE_NAME_0":
                1
            org = item["original"]
            trz = item["translation"]
            patten_check = 0
            for pattern in pattens:
                if sorted(re.findall(pattern,org)) != sorted(re.findall(pattern,trz)):
                    patten_check = 1
                    break
            if patten_check:
                diff_f_data += item["key"]+" \""+item["translation"]+"\"\n"
                diff_f_org_data += item["key"]+" \""+item["original"]+"\"\n"
    if diff_f_data != '':
        diff_f = open( diff_ch,'w+',encoding="utf-8-sig")
        diff_f.write(diff_f_org_data)
        diff_f_org = open( diff_en,'w+',encoding="utf-8-sig")
        diff_f_org.write(diff_f_data)

    
                

