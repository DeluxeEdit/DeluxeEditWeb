from django.http import HttpResponse
import os
from django.conf import settings

def    getfiles(path, name)
    result=[]


    for root, dir, files in os.walk(path)


        if name in files:
            result.append(os.path.join(root, filename))
return  result 


def list(request):
    now = datetime.datetime.now()
if os.path.isdir( settins. PathOnPAN)
    pathtouse=    settins.PathOnPAN
else
    pathtouse=    settins.PathOnPI

   result = getfiles( pathtouse=



    html = '<html lang="en"><body>It is now %s.</body></html>' % now
    return HttpResponse(html)
