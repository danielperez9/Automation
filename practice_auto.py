#When the cript is run it will start and ask you to enter a date,
# the date is the date in which the files have been made.
# After it will ask you to enter a naem for the folder in which the files from that day will be placed in.
#this code will edit the files, just copy them in the new directory and rename them
from copy import copy
from datetime import *
import os
import copy
import shutil
import time

def right_directory():
    current_directory=os.getcwd()
    if current_directory !='D:\SampleText':
        os.chdir('D:\SampleText')
        filesort()
    else:
        filesort()

new_directory_name=input("Enter a name of the new Folder: ")
# here a function is taken by the input above to be the name
# after the directory is made it ill sort files out from the original directory 
# to be copied over to the new one
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
# this function will rename the files that were coppied 
# from the directory that was just made
def rename_files():
    old_dir=os.getcwd()
    new_directory=os.path.join(old_dir,new_directory_name)
    os.chdir(new_directory)
    fila=os.listdir(new_directory)

    number=0
    for f in fila:
        filetime=datetime.fromtimestamp(os.path.getctime(f))
        filetime=filetime.strftime("%Y-%m-%d")
        filenames = new_directory_name +'_'+str(number+1)+'_'+filetime+".txt"
        os.rename(f,filenames)
        number+=1

rename_files()
#accesing a differnt direcotry and editing a 
# single line in multiple text files
def edit_file():
    old_dir=os.getcwd()

    fila=os.listdir(old_dir)
    for f in fila:
        with open(f,"r") as file:    
            data=file.readlines()
            # the number determines which line * python starts at 0
            data[1]="I need to get my story straight\n"
        with open(f,'w') as file:
            file.writelines(data)

edit_file()

