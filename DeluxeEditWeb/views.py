from  django.template.loaders.filesystem import Loader
from django.http import HttpResponse
import os
from django.conf import settings
from django.shortcuts import render
"""loader=Loader('deluxeedithtml')
template = loader.get_template('deluxeedithtml')
"""
def    getfiles(path, name):
    result=[]

    for root, dir, files in os.walk(path):
        if name in files:
            fullpath=path=os.path.join(root, filename)
            mod=os.path.getmtime(  fullpath )
            item= FileItem()
            item.path=fullpath
            item.modified=mod
            result.append(item)

    return  result 


def list(request):
    if os.path.isdir( settins.PathOnPAN):
        pathtouse=settins.PathOnPAN
    else:
        pathtouse=settins.PathOnPI

    files = getfiles( pathtouse, settins.Extension)
    return render(request, "deluxeedithtml")



def index(request):
    """atest_question_list = Question.objects.order_by("-pub_date")[:5]
    """
    return render(request, "deluxeedithtml")


    

    
