from django.shortcuts import render,redirect
from fpage.models import nlogs

# Create your views here.
def home(request):

        # return redirect("")
    return render(request,'home.html')

def login(request):
    return render(request,'log.html')


def index(request):
    if request.method=="POST":
            name = request.POST.get('username')
            p = request.POST.get('password')
            print(name,' ',p)
            re=nlogs.objects.filter(uname=p,pas=p)
            print(re)
            if re:
                # return redirect("")
                return render(request,"home.html")
            else:
                # return redirect("home")
                return render(request,"log.html")
    else:
        return render(request,"log.html")
            

