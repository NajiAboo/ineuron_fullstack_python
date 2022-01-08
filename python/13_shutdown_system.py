import os 

def shutdown():
    isShut = input("Do you want to shutdown - yes/no : ")
    
    if isShut == 'yes':
        os.system("shutdown /s /t 1")
    else:
        pass

shutdown()