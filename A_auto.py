#When the cript is run it will start and ask you to enter a date,
# the date is the date in which the files have been made.
# After it will ask you to enter a naem for the folder in which the files from that day will be placed in.
#this code will not edit the files, just copy them in the new directory and rename them

from copy import copy
from datetime import *
import os
import copy
import shutil
import time

def right_directory():
  #checks if we are int he correct directory in where the file(s) are located
  # the folder in which the file is in
    current_directory=os.getcwd()
    if current_directory !='C:\User\':
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
    #makeing a new direcotry with name inputed in the diretciry win which files are found
    
    #listing files by most recently made
    file_list=os.listdir(search_directory)
    files=list(filter(os.path.isfile,file_list))
    files.sort(key=os.path.getctime,reverse=True)
    search_date_entry=input("Enter the date in MM/DD/YYYY format: ")
    
    #comparing file date of creation to the date inputed
    for index in files:
        file_time=datetime.fromtimestamp(os.path.getctime(index))
        file_time=file_time.strftime("%m/%d/%Y")
        
#if the dates match they will be copied to the new directory made
        if file_time==search_date_entry:  
            shutil.copy(index,new_directory)
            
           
right_directory()
# this function will rename the files that were copied 
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
        #renaming base on direcoty name, adding a sequential number and adding the date
        filenames = new_directory_name +'_'+str(number+1)+'_'+filetime+".txt"
        os.rename(f,filenames)
        number+=1

rename_files()
