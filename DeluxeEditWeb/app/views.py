"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import FileInfo
from django.conf import settings

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


def files(request):
    if os.path.isdir( settins.PathOnPAN):
        pathtouse=settins.PathOnPAN
    else:
        pathtouse=settins.PathOnPI

  
    files = getfiles( pathtouse, settins.Extension)
    return render(request, "deluxeedithtml")
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
