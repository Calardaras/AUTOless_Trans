import json,re,os

raw_file = open(file,'r',encoding="utf-8-sig")
data = json.load(raw_file)
diff_f_data = ''
diff_f_org_data = ''
for item in data:
    patten1 = '(\$.+?\$|\[.+?\]|@.+?\!)+'
    patten2 = '(#[YGRTFE!]{1,2} *)+'
    patten3 = '(\\\\n)+'
    substance_1 = re.findall( patten1 +'|'+patten2 +'|'+patten3 , item["original"] )
    substance_2 = re.findall( patten1 +'|'+patten2 +'|'+patten3 , item["translation"])
    if substance_1 != substance_2:
        diff_f_data += item["key"]+item["translation"]+"\n"
        diff_f_org_data += item["key"]+item["original"]+"\n"
if diff_f_data != '':
    diff_f = open( diff_ch,'w+',encoding="utf-8-sig")
    diff_f.write(diff_f_org_data)
    diff_f_org = open( diff_en,'w+',encoding="utf-8-sig")
    diff_f_org.write(diff_f_data)