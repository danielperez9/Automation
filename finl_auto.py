# this project was made with the idea od automating the process of naminig severl files,
#that happend to be same data type, based on the directory it is in

import os
from datetime import *
import time
#This will be to check which directory it is in and if not to change to the
#  one in which all the files you want to edit are in 
def directory_chk():
    current_dir= os.getcwd() #checking what is the current directory is 
    if current_dir != 'D:\Resume': # if it is not in the desire directory 
        os.chdir("D:\Resume") # switch to new or required directory
        time_sorting()# move on
    else:# if it is in the right directory we move on as well
        time_sorting()

def time_sorting():
    
    searchdir_= os.getcwd()# get the directory again
    list1 =os.listdir(searchdir_)# ge all files in the directory
    files=list(filter(os.path.isfile,list1))  #making them into a list 
    files.sort(key=os.path.getctime,reverse=True)# organize them by most recent 
    file_num=0

    for index in files:# a loop to go through each file
        create_time=datetime.fromtimestamp(os.path.getctime(index))# get the time of creation of file
        local_tim=create_time.strftime("%a %b %#d %Y")  #formatting the date
        tuday=date.today()# get current date
        today_date = tuday.strftime("%a %b %#d %Y")# formatting current date to match creation date of file
      
        if local_tim == today_date:# comparing both dates to re name
            newname = "File "+str(file_num+1)+"-"+today_date+".pdf"#format for renaming 
            file_num+=1
            os.rename(index,newname)# renamesfile 
           
directory_chk()