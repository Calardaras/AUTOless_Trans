import os,re
path_list = ["output","process","tobetrans","transed",'renamed']
for root in path_list:
    if not os.path.exists(root):
        os.makedirs(root)
    else:
        os.removedirs(root)