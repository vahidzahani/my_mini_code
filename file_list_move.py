from ast import Try
import os
import re
import shutil

path_a=r"\\10.10.1.2\data1"
path_b=r"\\10.10.1.2\data2"
res=[]
for fname in os.listdir(path_a):
    x=re.findall("[0-9]+",fname)
    my_dir_name=x[0]
    print(fname + " - " + my_dir_name)
    b=path_b+"\\"+my_dir_name+" - appk"

    try:
        os.makedirs(b)
    except OSError as e:
        print(e)
    
    try:
        shutil.move(path_a+"\\"+fname,b+"\\"+fname)
    except OSError as e:
            print(e)
        

