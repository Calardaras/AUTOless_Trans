import json,re

single_consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
double_consonants = ["ch", "rh", "th", "sh","gh","dr"
                     "sc", "ck",
                     "ph","ps",
                     "tr",]
end_consonants = ['h','l','r','s','n','ng']
vowels = r"[aeiouAEIOU]{1,2}|(?<=[bcdfghjklmnpqrstvwxyz])y(?<![aeiou])"

def split_string(s):
    # 以空格为分隔符，将字符串分割成若干部分
    parts = s.split(' ')
    # 创建一个空列表，用来存放最终的结果
    result = []
    # 遍历每个部分
    for part in parts:
        # 以连字符为分隔符，将部分分割成若干子串
        substrings = part.split('-')
        # 将子串添加到结果列表中
        result += substrings
    # 返回结果
    return result

def cost(_syllebe):
    if (re.search(vowels,_syllebe) == None):
        return 0
    _cost = 0
    start = re.search(vowels,_syllebe).start()
    end = re.search(vowels,_syllebe).end()
    left = _syllebe[0:start]
    right = _syllebe[end:]
    match len(left):
        case 0:
            _cost += 1
        case 1:
            _cost += 0
        case 2:
            if (left in double_consonants):
                _cost += 0  
            else:
                _cost += 3
        case _:
            _cost += 5
    if right in end_consonants:
        _cost += 0
    return _cost 

def divide(_str,_syllebes,_cost=0):
    if re.search(vowels,_str) == None:
        syllebe = _str
        _syllebes.append(syllebe)
        _cost += cost(syllebe)
        cost_list.append(_cost) # 压栈
        divide_list.append(_syllebes[:])
        _syllebes.pop()  # 出栈
        return
    first = re.search(vowels,_str).end()
    syllebe = _str[0:first]
    if re.search(vowels,_str[first:]) == None:
        syllebe = _str
        _syllebes.append(syllebe)
        _cost += cost(syllebe)
        cost_list.append(_cost) # 压栈
        divide_list.append(_syllebes[:])
        _syllebes.pop()  # 出栈
        return
    _str = _str[first:]
    second = re.search(vowels,_str).start()
    mid = _str[0:second]
    for i in range(len(mid)+1):
        _syllebe = syllebe + mid[0:i]
        _cost += cost(_syllebe)
        _syllebes.append(_syllebe) # 压栈
        __str =_str[i:]
        divide(__str ,_syllebes,_cost)
        _syllebes.pop() # 出栈divide_list

########################
raw_file = open('syllabele\provincenames_l_simp_chinese.yml.json','r',encoding="utf-8-sig")
raw_file1 = open('syllabele\character_names_inv_l_simp_chinese.yml.json','r',encoding="utf-8-sig")
data = json.load(raw_file)
data += json.load(raw_file1)
dicts = []
divides = []
all_map = []
for item in data:
    if item["stage"] == 0:
        _dict = {"original":"","divides":""}
        org_value = item["original"]
        _dict["original"] = org_value
        subs = split_string(org_value)
        opti = []
        for str in subs:
            str = str.lower()
            if (str == ''):
                continue
            syllables = []
            divide_list = []
            cost_list = []
            divide(str,syllables)
            _opti = divide_list[cost_list.index(min(cost_list))]
            opti.extend(_opti)
        _dict["divides"] = opti
        all_map.append(_dict)
        for syllable in opti:
            temp = syllable.lower()
            if temp not in dicts:
                dicts.append(temp)

dicts.sort()
dicts_file = open('syllabele\syllabele.txt','w+',encoding="utf-8-sig")
dicts_file.write('\n'.join(dicts))
# 使用dump()方法将字典保存为json文件
with open ("syllabele\data.json", "w+") as f:
    json.dump(all_map, f)