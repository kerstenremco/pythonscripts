#Bulk copy files and change name
import os
import shutil

for filename in os.scandir():
    if filename.is_file():
        newname = filename.name.split('-')[0]
        filetype = filename.name.split('.')[-1]
        print (f"Copy {filename.name} to {newname}.{filetype}")
        shutil.copyfile(filename.name, f"./output/{newname}.{filetype}")
