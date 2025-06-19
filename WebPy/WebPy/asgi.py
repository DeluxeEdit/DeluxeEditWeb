"""
ASGI config for WebPy project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebPy.settings')

application = get_asgi_application()
pathToInstallFiles='/mnt/c/Slask'
installFileExtension='.msix'

def    GetFiles(path, name)
    result=[]

       

    for root, dir, files in os.walk(path)

                                         
        if name in files:
            result.append(os.path.join(root, filename))
return  result








