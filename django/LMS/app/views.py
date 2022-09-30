# import datetime
from datetime import datetime
import email
from django.shortcuts import render,redirect
from .models import logs,library
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
            re=logs.objects.filter(uname=p,pas=p)|logs.objects.filter(email=name,pas=p)
            if re:
                return redirect("view")
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
    
def view(request):
    books=library.objects.all()
    context={'books':books}
    return render(request,'view.html',context)

def add(request):
    if request.method == 'POST':
        name = request.POST['book_name']
        auth = request.POST['author_name']
        page = request.POST['pages']   
        new_book=library(book_title=name,book_author=auth,book_pages=page)
        new_book.save()
        messages.success(request,'Book added Successfully')
    return render(request,'add.html')

def update(request):
    books=library.objects.all()
    context={'books':books}
    return render(request,'update.html',context)

def update1(request,id=0):
    up=library.objects.filter(id=id).first()
    new={
        'up':up
    }
    if id:
        book=library.objects.get(id=id)
        book.delete()
    if request.method == 'POST':
            name = request.POST['book_name']
            auth = request.POST['author_name']
            page = request.POST['pages']
            new_book=library(book_title=name,book_author=auth,book_pages=page)
            new_book.save()
            return redirect('update')
    # print(new)
    return render(request,'update1.html',new)


def d(request,id=0):
    if id: 
        book=library.objects.get(id=id)
        book.delete()
        return redirect('update1')
    return render(request,'delete.html')
# def delete(request):
def delete(request,id=0):
    books=library.objects.all()
    context={'books':books}
    if id: 
        book=library.objects.get(id=id)
        book.delete()
    return render(request,'delete.html',context)

