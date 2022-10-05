
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import library,logs
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


@api_view(['POST'])
def update(request,pk):
    books=library.objects.get(id=pk)
    serialize=lib(instance=books,data=request.data)
    if serialize.is_valid():
        serialize.save()
    return Response(serialize.data)


# @api_view(['DELETE'])
def delete(request,pk):
    books=library.objects.get(id=pk)
    books.delete()
    books=library.objects.all()
    context={'books':books}
    return render(request,'view.html',context)