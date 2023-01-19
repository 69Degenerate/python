from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import std
from .serializers import stdapi

def front(request):
    return render(request,'home.html')

@api_view(['GET'])
def read(request):
    data=std.objects.all()
    d=stdapi(data,many=True)
    return Response(d.data)


@api_view(['GET'])
def search(request,c='',val=''):
    print(c,val)
    if c=='n':
        data=std.objects.filter(n=val)
    if c=='r':
        data=std.objects.filter(r=val)
    if c=='e':
        data=std.objects.filter(e=val)
    if c=='d':
        data=std.objects.filter(d=val)
    d=stdapi(data,many=True)
    return Response(d.data)


@api_view(['GET', 'POST'])
def write(request):
    serialize=stdapi(data=request.data)
    print(serialize)
    if serialize.is_valid():
        print("valid")
        serialize.save()
    else:
        print("S")
    return Response(serialize.data)


def delete(request,pk):
    d=std.objects.get(id=pk)
    d.delete()
    return redirect('http://127.0.0.1:8000/')


@api_view(['PUT'])
def update(request,pk):
    d=std.objects.filter(id=pk).first()
    serialize=stdapi(instance=d,data=request.data)
    if serialize.is_valid():
        serialize.save()
    return Response(serialize.data)


@api_view(['DELETE'])
def apidel(request,pk):
    data=std.objects.get(id=pk)
    data.delete()
    if std.objects.filter(id=pk).exists():
        return Response("item not deleted")
    return Response("item deleted")