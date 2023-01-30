from django.shortcuts import render,redirect
from login_page.models import logs
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method=="POST":
            name = request.POST.get('username')
            p = request.POST.get('password')
            print(name,p)
            re=logs.objects.filter(uname=p,pas=p)
            print(re)
            if re:
                request.session['user_id'] = re.id
                return redirect("/home")
                # return render(request,"home.html")
            else:
                # return redirect("home")
                messages.warning(request,'username doesnt exist!')
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
        s=logs.objects.filter(uname=u).first()
        print(s)
        if s:
            print('usernmae found')
            messages.warning(request,'user already exist!')
            return render(request,'create.html')
            # return redirect("")
        else:
            print('no user found')
            entry = logs(uname=u,pas=p,email = e)
            entry.save()
            messages.success(request,'user created')
            return redirect("/")
            # return render(request,'create.html')
    else:
        return render(request,'create.html')


def home(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect(login)
    return render(request,'home.html')
