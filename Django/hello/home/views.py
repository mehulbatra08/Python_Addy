from django.shortcuts import render, HttpResponse
from home.models import Contactus
from django.contrib import messages


# Create your views here.
def index(request):
    # context ={
    #     'variable':'this is sent',
    #     'variable2':'this is variable 2'
    # }
    messages.success(request, "This is a test message")
    return render(request, "index.html")
   

def about(request):
        return render(request, "about.html")
def services(request):
    return render(request, "services.html")
def contact(request):
    if request.method == "POST":
        mypassword = request.POST.get('mypassword')
        myemail = request.POST.get('myemail')
        contact = Contactus(mypassword=mypassword, myemail=myemail)
        contact.save()
        messages.success(request, 'Your Message has been sent')
    return render(request, "contact.html")