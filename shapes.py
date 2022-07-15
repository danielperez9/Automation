
from copy import copy
from datetime import *
import os
import copy
import shutil
import time

#checking for the correct directory
def right_directory():
    current_directory=os.getcwd()
    if current_directory !='D:\Resume':
        os.chdir('D:\Resume')
        filesort()
    else:
        filesort()

new_directory_name=input("Enter a name of the new Folder: ")

def filesort():
    
    search_directory=os.getcwd()    #go to the directory stated earlier    
    
    os.mkdir(new_directory_name)# new directory being made
    new_directory=os.path.join(search_directory,new_directory_name)# path for new directory made
    # retrieving and organizing files from most recent to oldest
    file_list=os.listdir(search_directory)
    files=list(filter(os.path.isfile,file_list))
    files.sort(key=os.path.getctime,reverse=True)
    
    search_date_entry=input("Enter the date in MM/DD/YYYY format: ")#date for file search
    
    #comparing eah file in directory to date desired
    for index in files:
        file_time=datetime.fromtimestamp(os.path.getctime(index))
        file_time=file_time.strftime("%m/%d/%Y")
        
        #copyin each file that matches date created with dsied date to new directory
        if file_time==search_date_entry:  
            shutil.copy(index,new_directory)
            
           
right_directory()

def rename_files():
    old_dir=os.getcwd()
    #retrieving path to directory made earlier
    new_directory=os.path.join(old_dir,new_directory_name)
    os.chdir(new_directory)
    print (new_directory)
    fila=os.listdir(new_directory)

    number=0
    #small loop to rename each file in the new directory
    for f in fila:
        print(f)
        filetime=datetime.fromtimestamp(os.path.getctime(f))
        filetime=filetime.strftime("%m/%d/%Y")
        filenames = new_directory_name +'_'+str(number+1)+'_'+filetime+".pdf"
        os.rename(f,filenames)
        number+=1



rename_files()
        
