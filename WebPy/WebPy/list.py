from django.http import HttpResponse
import datetime



def    GetFiles(path, name)
    result=[]



    for root, dir, files in os.walk(path)


        if name in files:
            result.append(os.path.join(root, filename))
return  result 


def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html lang="en"><body>It is now %s.</body></html>' % now
    return HttpResponse(html)
