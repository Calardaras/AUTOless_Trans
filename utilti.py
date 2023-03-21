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
        root = 'raw_done\\' + check.group(0)
        if not os.path.exists(root):
            os.makedirs(root)
        else:
            shutil.rmtree(root)
            os.makedirs(root)

for file in raw_files:
    raw_file = open(file,'r',encoding="utf-8-sig")
    data = json.load(raw_file)
    done_data = []
    print('正在处理'+ file )
    for item in data:
        patten1 = "The mission task"
        if re.search(patten1, item["original"]) != None:
            patten2 = "#Y .+?#!"
            item["translation"] = "使命任务“"+ re.search(patten2,item["original"]).group(0) +"”现已#G 完成#!！"
            item["stage"]=1
            done_data.append(item)
    if done_data != []:
        done_file = open(re.sub('raw','raw_done',file),'w',encoding="utf-8-sig")
        json.dump(done_data,done_file,ensure_ascii=False)
            


    
                

