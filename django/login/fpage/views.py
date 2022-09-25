from django.shortcuts import render,redirect
from django.contrib import messages
from fpage.models import nlogs

# Create your views here.
def home(request):

        # return redirect("")
    return render(request,'home.html')

def login(request):
    if request.method=="POST":
            name = request.POST.get('username')
            p = request.POST.get('password')
            print(name,' ',p)
            re=nlogs.objects.filter(uname=p,pas=p)
            print(re)
            if re:
                return redirect("home")
            else:
                return render(request,"log.html")
    else:
        return render(request,"log.html")


def create(request):
    if(request.method=='POST'):
        u = request.POST.get('username')
        p = request.POST.get('password')
        e = request.POST.get('email')
        print(u,e,p)
        # s=logs.objects.filter(uname=p,pas=p,email=e)
        s=nlogs.objects.filter(uname=u).first()
        print(s)
        if s:
            print('usernmae found')
            messages.warning(request,'user already exist!')
            return render(request,'create.html')
            # return redirect("")
        else:
            print('no user found')
            entry = nlogs(uname=u,pas=p,email = e)
            entry.save()
            messages.success(request,'user created')
            return redirect("/")
            # return render(request,'create.html')
    else:
        return render(request,'create.html')


