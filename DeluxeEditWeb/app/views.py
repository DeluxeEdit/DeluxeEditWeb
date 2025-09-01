"""
Definition of views.
"""

from asyncio.windows_events import NULL
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.conf import settings
from util import Util
import os

def files(request):
    if os.path.isdir( settings.PathOnPAN):
        pathtouse=settings.PathOnPAN
    else:
        pathtouse=settings.PathOnPI

        files = Util.getFiles( pathtouse, settings.Extension)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/files.html',NULL)
        




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
