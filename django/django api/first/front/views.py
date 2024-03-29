
from django.shortcuts import render,redirect

from api.models import library,logs
from django.contrib import messages



def home(request):

    books=library.objects.all()
    context={
        'books':books,
    }
    return render(request,'home.html',context)

def signin(request):
    if request.method=="POST":
            name = request.POST.get('username')
            p = request.POST.get('password')
            print(name,' ',p)
            re=logs.objects.filter(uname=name,pas=p)|logs.objects.filter(email=name,pas=p)
            if re:
                return redirect("http://127.0.0.1:8000/api/readall")
            else:
                print(re)
                messages.warning(request,'user doesnt exist!')
                return render(request,"signin.html")
    else:
        return render(request,"signin.html")


def signup(request):
    if(request.method=='POST'):
        u = request.POST.get('username')
        p = request.POST.get('password')
        e = request.POST.get('email')
        print(u,e,p)
        s=logs.objects.filter(uname=u).first()
        print(s)
        if s:
            print('usernmae found')
            messages.warning(request,'user already exist!')
            return render(request,'signup.html')
        else:
            print('no user found')
            entry = logs(uname=u,pas=p,email = e)
            entry.save()
            messages.success(request,'user created')
            return redirect("signin")
    else:
        return render(request,'signup.html')



