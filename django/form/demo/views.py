from django.shortcuts import render
from demo.admin import Contact
from django.http import HttpResponse
from django.contrib import messages
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone)
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,'contact.html')
