from django.shortcuts import render
from django.http import HttpResponse
from .models import std
# Create your views here.
def sub(request):
    data=std.objects.all()
    d={'data':data}
    try:
        if request.method=='POST':
            name = request.POST.get('name')
            roll = request.POST.get('roll')
            email = request.POST.get('mail')
            dept = request.POST.get('dept')
            std(n=name,r=roll,e=email,d=dept).save()
        if request.method=='GET':
            c=request.GET.get('c')
            s=request.GET.get('s')
            print(c,s)
            if c=='n':
                data=std.objects.filter(n=s)
            if c=='r':
                data=std.objects.filter(r=s)
            if c=='e':
                data=std.objects.filter(e=s)
            if c=='d':
                data=std.objects.filter(d=s)
            dd={'data':data}
            return render(request,'form.html',dd)
    except:
        pass
    return render(request,'form.html',d)