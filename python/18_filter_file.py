import os
import glob

def filter(path, extension):
    os.chdir(path)
    files = glob.glob("*."+extension)
    return files

files = filter("","docx")
print(files)