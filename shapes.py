
from datetime import *
import os
import shutil
import time


def right_directory():
    current_directory=os.getcwd()
    if current_directory !='D:\Resume':
        os.chdir('D:\Resume')
        filesort()
    else:
        filesort()

new_directory_name=input("Enter a name of the new Folder: ")
def filesort():
    
    search_directory=os.getcwd()        
    
    os.mkdir(new_directory_name)
    new_directory=os.path.join(search_directory,new_directory_name)
    file_list=os.listdir(search_directory)
    files=list(filter(os.path.isfile,file_list))
    files.sort(key=os.path.getctime,reverse=True)
    search_date_entry=input("Enter the date in MM/DD/YYYY format: ")
    
    
    for index in files:
        file_time=datetime.fromtimestamp(os.path.getctime(index))
        file_time=file_time.strftime("%m/%d/%Y")
        

        if file_time==search_date_entry:  
            shutil.copy(index,new_directory)
            
           
right_directory()
def renaming():
    current_dir='D:\Resume'
    new_directory=os.path.join(current_dir,new_directory_name)
    
    file_num=0
    print (new_directory)
    os.chdir(new_directory)
    new_file_list=os.listdir(new_directory)
    newFiles=list(filter(os.path.isfile,new_file_list))
    for f in newFiles:
        file_time=datetime.fromtimestamp(os.path.getctime(f))
        file_time=file_time.strftime("%m/%d/%Y")
        new_name = new_directory_name+"_"+str(file_num+1)+"_"+file_time+".pdf"
        os.rename(f,new_name)
        file_num+=1
renaming()

        