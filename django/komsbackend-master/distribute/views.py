from django.shortcuts import render, redirect
from django.http import Http404
# Create your views here.


def sections(request,sect_code):
    code = request.GET.get("code")
    if code not in ['0','1','2','3','4']:
        raise Http404("room code does not exist")
    context = {
        "section_code":sect_code
    }
    return context