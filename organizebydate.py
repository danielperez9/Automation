from datetime import datetime
import os
from directory_chck import*

function()
current_dir=os.getcwd()
try:
    fil_list=os.listdir(current_dir)
    for i in fil_list:
        fil_tim=datetime.fromtimestamp(os.path.getctime(i))
        fil_tim=fil_tim.strftime("%a %b %#d %Y")
        print(fil_tim,i)
        
except:
    print()