import os
def function():
    current_dir=os.getcwd()
    print (current_dir)
    desired_dir= "D:\Resume"
    if current_dir != desired_dir:
        os.chdir(desired_dir)
        print(os.getcwd())
    else:
        print (os.getcwd())
    
    