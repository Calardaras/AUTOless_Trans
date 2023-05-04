import json,os, shutil,re
import numpy

class Syl:
    def __init__(self,syllabel,start,end):
        self.syllabele = syllabel
        self.start = start
        self.end = end

syllabele_list = []

strs = "Coropissuisoxydracae"
syllables = []
syllables_list = []

def divide(_str,_syllebes):
    # if _str == '':
    #     syllables_list.append([_syllebes])
    #     return
    first = re.search("[AEIOUYaeiouy]+",_str).end()
    syllebe = _str[0:first]
    if re.search("[AEIOUYaeiouy]+",_str[first:]) == None:
        syllebe = _str
        _syllebes.append(syllebe)
        syllables_list.append([_syllebes])
        _syllebes.pop()
        return
    _str = _str[first:]
    second = re.search("[AEIOUYaeiouy]+",_str).start()
    mid = _str[0:second]
    for i in range(len(mid)+1):
        syllebe += mid[0:i]
        _syllebes.append(syllebe)
        _str =_str[i:]
        divide(_str,_syllebes)
        _syllebes.pop()

divide(strs,syllables)
print(len(syllables_list))