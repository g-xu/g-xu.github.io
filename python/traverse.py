
import os
import os.path
import re

#Breadth-First
def list_files_breadth(dir):
    for root,dirs,files in os.walk(dir): 
        for d in dirs:
            full = os.path.join(root, d)
            base = os.path.basename(full)
            rdir = os.path.dirname(full)
            print('\n+++\n%s\n%s\n%s\n+++\n' %(full, base,rdir))
        for f in files:
            full = os.path.join(root, f)
            fname = os.path.basename(full)
            ext = os.path.splitext(f)[-1]
            rdir = os.path.dirname(full)
            print('\n---\n%s\n%s,ext:%s\n%s\n---\n' %(full, fname, ext, rdir))

#Depth-first
def list_files_depth(dir):
    for lists in os.listdir(dir):
        path = os.path.join(dir, lists)
        print path
        if os.path.isdir(path):
            list_all_files_2(path)

if "__main__" == __name__:
    list_files_breadth('.')
    #list_files_depth('/home/root/dev')
