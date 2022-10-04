
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import library
from .serializers import lib
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


@api_view(['DELETE'])
def delete(request,pk):
    books=library.objects.get(id=pk)
    books.delete()
    return Response("book is deleted")