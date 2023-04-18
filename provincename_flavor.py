import json,os, shutil,re
import numpy

raw_file = open('provincenames_l_simp_chinese.yml.json','r',encoding="utf-8-sig")
data = json.load(raw_file)
no_right = 1
total = 99

class Syl:
    def __init__(self):
        self.syllabele = ''
        self.start = 0
        self.end = 0

syllabele_list = []

for item in data:
    if item["stage"] == 0:
        raw_value = item["original"]
        Vowel_list = re.findall("[AEIOUYaeiouy]+?",item["original"])
        Syllables = []
        for Vowel in Vowel_list:
            temp = Syl()
            temp.syllabele = Vowel
            temp.start = re.search(Vowel,raw_value).start()
            temp.end = re.search(Vowel,raw_value).end()
            Syllables.append(temp)
            raw_value = raw_value[:temp.start] +'*'*(temp.end-temp.start) + raw_value[temp.end:]
        j = 0
        while True:
            for syl in Syllables:
                if syl.start == 0:
                    continue
                left_char = raw_value[syl.start - 1]
                if raw_value[syl.start - 1] != '*':
                    syl.start -= 1
                    syl.syllabele = left_char + syl.syllabele
                    raw_value = raw_value[:syl.start] +'*'*(syl.end-syl.start) + raw_value[syl.end:]
                
            if re.findall("[A-Za-z]",raw_value) == []:
                break
            if not no_right:
                for syl in Syllables:
                    if syl.end == len(raw_value):
                        continue
                    right_char = raw_value[syl.end]
                    if raw_value[syl.end] != '*':
                        syl.end += 1
                        syl.syllabele = syl.syllabele + right_char
                        raw_value = raw_value[:syl.start] +'*'*(syl.end-syl.start) + raw_value[syl.end:]
                if re.findall("[A-Za-z]",raw_value) == []:
                    break
            j+=1
            if j>= total:
                break
        for syl in Syllables:
            if syl.syllabele.lower().strip(' ') not in [x.lower() for x in syllabele_list]:
                syllabele_list.append(syl.syllabele.strip(' '))
syllabele_list.sort()
syllabele_file = open('syllabele.txt','w+',encoding="utf-8-sig")
syllabele_file.write('\n'.join(syllabele_list))
