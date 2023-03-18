import json,re,os

file = open("raw\\CORE\\simp_chinese\\missions\\kush_missions_l_simp_chinese.yml.json",'r',encoding="utf-8-sig")
data = json.load(file)
for item in data:
    patten1 = '(\$.+?\$|\[.+?\]|@.+?\!)+'
    patten2 = '(#[YGRTFE!]{1,2} *)+'
    patten3 = '(\\\\n)+'
    substance_1 = re.findall( patten1 +'|'+patten2 +'|'+patten3 , item["original"] )
    substance_2 = re.findall( patten1 +'|'+patten2 +'|'+patten3 , item["translation"])
    if substance_1 != substance_2:
        print(item["key"])