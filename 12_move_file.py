import shutil,os

def move(source,destination):
    if os.path.isfile(source) and os.path.isdir(destination):
        path = shutil.move(source,destination)
        return path
    else:
        print("Source should be a file and destination should be a folder")

p = move("/home/sfm/comments","/media/sfm/62E4D583E4D559BD6/Users/Naji/Tutorials/ineron_fullstack/assignment/python/ineuron_fullstack_python")
print(p)

        
        