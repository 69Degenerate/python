from django.shortcuts import render,redirect
from login_page.models import logs

# Create your views here.
def login(request):
    if request.method=="POST":
            name = request.POST.get('username')
            p = request.POST.get('password')
            print(name,p)
            re=logs.objects.filter(uname=p,pas=p)
            print(re)
            if re:
                return redirect("/home")
                # return render(request,"home.html")
            else:
                # return redirect("home")
                return render(request,"log.html")
    else:
        return render(request,"log.html")


def create(request):
    if(request.method=='POST'):
        p = request.POST.get('password')
        e = request.POST.get('email')
        u = request.POST.get('username')
        print(u,e,p)
        # s=logs.objects.filter(uname=p,pas=p,email=e)
        s=logs.objects.filter(uname=p).first()
        print(s)
        if s:
            print('user found')
            # flash("user created")
            # entry = logs(uname=u,email = e,pas=p)
            # db.session.add(entry)
            # db.session.commit()
            return render(request,'create.html')
            # return redirect("")
        else:
            print('no user found')
            # flash("username already exist")
            return render(request,'create.html')
    else:
        # return render("create.html")
        return render(request,'create.html')


def home(request):
    return render(request,'home.html')
