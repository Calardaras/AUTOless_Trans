import json
import os
import deepl
import autotranz.utils as utils
import re


def autotrans(_dir,_type,_auth_key):
    translator = deepl.Translator(_auth_key)
    match _type:
        case "yml":
            flag = 0
        case "json":
            flag = 1
        case _:
            return 'Unknown type'
    file_name_list = utils.file_search_to_list(_dir,_type)
    if flag == 0:
        for crr_file_name in file_name_list:
            crr_file = open( crr_file_name ,'r',encoding="utf-8-sig")
            print('正在处理' + crr_file_name)
            new_name = re.sub('input','output',crr_file)
            result_f = open(new_name,"w",encoding="utf-8-sig")
            for line in crr_file:
                comm_check = re.match('^( *)#+',line) #注释
                if comm_check != None:
                    continue
                else:
                    head_check = re.search('l_english',line)
                    key_check = re.search('^( ?)[^#][^:]+?:\d?',line) #键
                    if key_check != None and head_check == None:
                        key = re.search('^( ?)[^#][^:]+?:\d?',line).group(0)
                        tonorm = re.search('".*"',line).group(0)
                        [totranz,dict] = utils.normalize(tonorm.strip('"'))
                        toform = translator.translate_text(totranz, target_lang="EN")
                        result = utils.formalize(toform,dict)
                        result_f.write(key+result+'\n')
        return True
    if flag == 1:
        for crr_file_name in file_name_list:
            crr_file = open( crr_file_name ,'r',encoding="utf-8-sig")
            items = json.load(crr_file)
            print('正在处理' + crr_file_name)
            for item in items:
                if item["stage"] == 0:
                    [totranz,dict] = utils.normalize(item["original"])
                    toform = translator.translate_text(totranz, source_lang="EN", target_lang="ZH")
                    result = utils.formalize(toform.text,dict)
                    print(item["original"]+":\n"+result)
                    item["translation"] = result
                    item["stage"] == 1
            new_dir = re.sub("input","output",crr_file_name)
            new_dir = re.sub("english","simp_chinese",new_dir)
            if not os.path.exists(re.sub(r'[^\\/]+$', '', new_dir)):
                os.makedirs(re.sub(r'[^\\/]+$', '', new_dir))
            with open (new_dir, "w+",encoding="utf-8-sig") as f:
                json.dump(items, f,ensure_ascii=False)
        return True
