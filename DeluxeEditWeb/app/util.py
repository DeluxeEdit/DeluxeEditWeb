import os
from .models import FileInfo
def    getfiles(path, name):
    result=[]

    for root, dir, files in os.walk(path):
        if name in files:
            fullpath=path=os.path.join(root, name)
            mod=os.path.getmtime(  fullpath )
            item=FileInfo()
            item.path=fullpath
            item.modified=mod
            result.append(item)

    return  result 

