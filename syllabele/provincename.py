import json,os, shutil,re

raw_file = open('provincenames_l_simp_chinese.yml.json','r',encoding="utf-8-sig")
data = json.load(raw_file)
dicts = {}
for item in data:
    if item["stage"] == 1:
        dicts[item["original"]] = item['translation']
new_data = ''
for item in data:
    if item["stage"] == 0:
        if dicts.get(item["original"],None) != None:
            new_data += item["key"]+" \""+dicts[item["original"]]+"\"\n"

if new_data != '':
    new_f = open('1122.txt','w+',encoding="utf-8-sig")
    new_f.write(new_data)
