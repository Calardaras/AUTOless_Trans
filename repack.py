import os,sys,re,docx
from docx import Document

path_org = ""
path_otp = "output\\simp_chinese"
path_tmp = "process"
path_bfr = "tobetrans"
path_aft = "transed"

def file_search_to_list(path):
    L = []
    for root,dirs,files in os.walk(path):
        for file in files:
            all_file_path = os.path.join(root,file)
            file_name_and_format = os.path.splitext(all_file_path)
            if file_name_and_format[1] == '.docx':
                L.append(all_file_path)
    return L

# 读取中间文件
key_f = open( path_tmp + '\\' + 'key.txt' ,'r',encoding="utf-8-sig") 
original_f = open( path_tmp + '\\' + 'value.txt' ,'r',encoding="utf-8-sig") 
key_l = list(key_f)
original_l = list(original_f)
key_f.close()
original_f.close()
contents_f = open( path_tmp + '\\' + 'contents.txt' ,'r',encoding="utf-8-sig") 


#处理目录和引索
file_name =[]
index = []
for content in contents_f:
    file_name.append(re.search('^[^,]+', content).group(0))
    index.append(re.search('[^,]+$', content).group(0))

contents_f.close()
file_docx_name_list = file_search_to_list(path_aft)
for curr_docx_name in file_docx_name_list:
    i = 0
    j = 0
    curr_docx = Document(curr_docx_name)
    curr_json = open( path_otp  + '\\' + re.search('(?<=(\\\\english\\\\))[^.]+', file_name[i]).group(0) + '.json','w+',encoding="utf-8-sig") 
    curr_json.write('[\n')
    for paragraph in curr_docx.paragraphs:
        if paragraph.text != '':
            if j< int(index[i])-1:
                translation = re.sub('"','',paragraph.text)
                translation = '"' + re.sub('\n','',translation) + '"' 
                curr_json.write(
                    ' {\n'+
                    '  \"key\": "' + re.search('^[^(\n)]+',key_l[j]).group(0) +'",\n'+
                    '  \"original\":' + original_l[j] +',\n'+
                    '  \"translation\": ' + translation +',\n'+
                    '  \"stage\":' + str(1) +'\n'+
                    ' },\n'
                )
                j+=1
            else:
                curr_json.write('\]')
                curr_json.close()
                i+=1
                curr_json = open( path_otp  + '\\' + re.search('(?<=(\\\\english\\\\))[^.]+', file_name[i]).group(0) + '.json','w+',encoding="utf-8-sig") 
                curr_json.write(
                    '[\n'+
                    ' {\n'+
                    '  \"key\": "' + re.search('^[^(\n)]+',key_l[j]).group(0) +'",\n'+
                    '  \"original\":' + original_l[j] +',\n'+
                    '  \"translation\": ' + translation  +',\n'+
                    '  \"stage\":' + str(1) +'\n'+
                    ' },\n'
                )
                j+=1


                