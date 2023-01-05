from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import library
from std_view.models import log as logs
from .serializers import lib,log
from django.shortcuts import render,redirect


@api_view(['GET'])
def users(request):
    books=logs.objects.all()
    serialize=log(books,many=True)
    return Response(serialize.data)

@api_view(['POST'])
def newuser(request):
    serialize=log(data=request.data)
    if serialize.is_valid():
        serialize.save()
    return Response(serialize.data)

@api_view(['GET'])
def read(request):
    books=library.objects.all()
    serialize=lib(books,many=True)
    return Response(serialize.data)

@api_view(['GET'])
def read2(request,pk):
    books=library.objects.get(id=pk)
    serialize=lib(books,many=False)
    return Response(serialize.data)

@api_view(['POST'])
def create(request):
    serialize=lib(data=request.data)
    if serialize.is_valid():
        serialize.save()
    return Response(serialize.data)



# perform CRUD operations on library database
# read all available records with api
def readall(request):
    books=library.objects.all()
    context={'books':books}
    return render(request,'view.html',context)

# update books details
def update(request,pk=0):
    up=library.objects.filter(id=pk).first()
    new={
        'up':up
    }
    if request.method == 'POST':
            name = request.POST['book_name']
            auth = request.POST['author_name']
            page = request.POST['pages']
            avail = request.POST['avail']
            library.objects.filter(id=pk).update(book_title=name,book_author=auth,book_pages=page,book_avail=avail)
            return redirect('readall')
    return render(request,'update.html',new)

# add books to record
def add(request):
    if request.method == 'POST':
        name = request.POST['book_name']
        auth = request.POST['author_name']
        page = request.POST['pages']   
        avail = request.POST['avail']
        data={
             "book_title": name,
             "book_author": auth,
             "book_pages": page,
             "book_avail": avail
            }
        serialize=lib(data=data)
        if serialize.is_valid():
            serialize.save()
            return redirect('readall')
    return render(request,'add.html')
 
# delete the records using api
def delete(request,pk):
    books=library.objects.get(id=pk)
    books.delete()
    books=library.objects.all()
    return redirect('readall')


