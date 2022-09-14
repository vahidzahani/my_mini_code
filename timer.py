import time
import os
from os import system,name
print(name)
system("cls")
file_path =os.path.abspath(os.path.dirname(__file__))

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


counter=0
f=open(os.path.abspath(os.path.dirname(__file__))+"\\tt.txt",'r')
counter=int(f.read())
f.close()
while(1):
    counter=counter+1
    clear()
    print("Runed Trade training: " + str(counter) + " Minutes")
    f2=open(os.path.abspath(os.path.dirname(__file__))+"\\tt.txt",'w')
    f2.write(str(counter))
    f2.close()
    time.sleep(60)


    