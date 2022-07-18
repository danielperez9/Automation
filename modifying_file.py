import os
import re
os.chdir('D:\SampleText')
print(os.getcwd())
# the function will replace one word if it matches, throught the file
def rewrite1():
    file=open('newtest.txt','r')
    replace=""
    for i in file:
        i=i.strip()
        change=i.replace("My", 'your')
        replace=replace+change+"\n"
        print(i)
    file.close()

    file_changed=open('newtest.txt','w')
    file_changed.write(replace)
# this function will replace a line in the file
def rewrite2():
    with open('newtest.txt','r') as file:
            
        data=file.readlines()
        print(data)
        # the number determines which line * python starts at 0
        data[1]="I need to get my story straight\n"

    with open('newtest.txt','w') as file:
        file.writelines(data)
# this function indents every n characters
def indenting():
    with open('newtest.txt','r') as file:
        data=file.read()
        # numbr can be modified to liking
        data=re.sub("(.{2})","\\1\n", data,0,re.DOTALL)

    with open('newtest.txt','w') as file:
        file.writelines(data)

indenting()
