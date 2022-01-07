import shutil,os

def move(source,destination):
    if os.path.isfile(source) and os.path.isdir(destination):
        path = shutil.move(source,destination)
        return path
    else:
        print("Source should be a file and destination should be a folder")

p = move(" ","")
print(p)

        
        