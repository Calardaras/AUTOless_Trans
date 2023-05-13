import re
import os


patterns = [
    r'(\$.+?\$)+',
    r'(\[.+?\])+',
    r'(@.+?!)+',
    r'(#[YGRTFE!]{1,2} *)+',
    r'\n+'
    ]

u_patterns = r'('
for pattern in patterns:
    u_patterns += pattern+'|'
u_patterns = u_patterns.strip('|')+")+"

def normalize(_tonorm):
    i = 0
    _dict = {}
    _totranz = _tonorm
    for pattern in patterns:
        if pattern == r'\n+':
            1
        finds = re.findall(pattern,_tonorm)
        for find in finds:
            key = find
            if key not in _dict:
                _dict[key] = "<m id="+str(i)+">"
                i +=1
    for k, v in _dict.items():
        _totranz = _totranz.replace(k, v)
    return [_totranz,_dict]

def formalize(_toform,_dict):
    for k, v in _dict.items():
        _toform = _toform.replace(v, k)
    return _toform

def file_search_to_list(path,extension):
    L = []
    for root,files in os.walk(path):
        for file in files:
            all_file_path = os.path.join(root,file)
            file_name_and_format = os.path.splitext(all_file_path)
            if file_name_and_format[1] == '.' + extension:
                L.append(all_file_path)
    return L

def get_file_structure(path,extension):
    file_structure = []
    for root,files in os.walk(path):
        for file in files:
            relpath = os.path.relpath(os.path.join(root, file), path)
            file_name_and_format = os.path.splitext(relpath)
            if file_name_and_format[1] == '.' + extension:
                file_structure.append(relpath)
    return file_structure