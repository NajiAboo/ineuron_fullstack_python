import os
def get_file_names(path_dir):
    lst = []
    print(path_dir)
    if os.path.isdir(path_dir):
        for f in os.listdir(path_dir):
            if os.path.isfile(os.path.join(path_dir,f)):
                lst.append(f)
            else:
                l = get_file_names( os.path.join(path_dir,f))
                
                for x in l: # append the base folder with file
                    lst.append(os.path.join(f,x))
                
    return lst
    print(os.listdir(path_dir))
    

l1 = get_file_names('/')
print(l1)
    