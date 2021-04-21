from django.shortcuts import render
from . import models

def p1(request):
    c={'fname':'Muhammed','lname':'mousa'}
    return render(request,"index.html",c)



def p2(request):
    c={'fname':'Ahmed','lname':'mousa'}
    return render(request,"test.html",c)

def backend(request):
    c={"videoname":request.POST['videoName']}
    return render(request,"index.html",c)
    # v1=request.POST['videoName']
    # new=models.deepFake(paths=v1)
    # new.save()
    # return HttpResponse('inserted sucssefully')