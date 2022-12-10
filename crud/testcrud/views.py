from django.shortcuts import render, HttpResponse
from datetime import datetime
from testcrud.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("This is homepage")

def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is about page")

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message is received. You will be contacted soon..!')
    return render(request,'contact.html')
    # return HttpResponse("This is contact page")

def services(request):
    return render(request,'services.html')
    # return HttpResponse("This is services page")