import os,sys
import re

path_org = "original\\english"
path_list = ["output","process","tobetrans","transed"]
for root in path_list:
    if os.path.exists(root):
        os.remove(root)
    else:
        os.makedirs(root)
for root,dirs,files in os.walk(path_org):
    root = 'output\\' + root
    if os.path.exists(root):
        os.remove(root)
    else:
        os.makedirs(root)