from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.

"""
✨✨ INFORMATION ✨✨ #
--------------------------------------------------------------------------------------
HttpResponse -> When we want to return a string to the client, we use HttpResponse.
--------------------------------------------------------------------------------------
render -> When we want to return a HTML file to the client, we use render.
--------------------------------------------------------------------------------------
context -> When we want to pass a variable from views.py to HTML file, we use context.
           context is a dictionary and variable is a key-value pair. and variable name 
           should be same in both files that is views.py and HTML file.We need to pass
           context as a third parameter in render function. Following is not how to pass
           context. Normally we fetch data from database/model and pass it to HTML file.  
           
def index(request):
    # return HttpResponse("Hello, world. You're at the home page.")
    context = {
        'variable1': 'Krish',
        'variable2': 'Gopani'
    }
    return render(request, 'index.html', context)
--------------------------------------------------------------------------------------
request -> When we want to get some information from the client, we use request.
--------------------------------------------------------------------------------------
✨✨ INFORMATION ✨✨ 
"""

def index(request):
    # return HttpResponse("Hello, world. You're at the home page.")
    context = {
        'variable1': 'Krish',
        'variable2': 'Gopani'
    }
    return render(request, 'index.html', context)

def about(request):
    # return HttpResponse("Hello, world. You're at the about page.")
    return render(request, 'about.html')

def services(request):
    # return HttpResponse("Hello, world. You're at the services page.")
    return render(request, 'services.html')

def contact(request):
    # return HttpResponse("Hello, world. You're at the contact page.")
    
    '''
    If somebody fills the contact form and click on submit button
    and if the method is POST then we will get the data from the 
    contact form and store it in the variables. '.get()' method 
    will get the data from the contact form.
    '''
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        # Contact ka object banaya
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        
        # Once the data is saved in the database, we will show a message to the user that his/her message has been sent.
        # success is a class of messages and it will show a green color message.
        messages.success(request, 'Your message has been sent!')

        
    return render(request, 'contact.html')

