from django.shortcuts import render
from website.forms import ContactForm
# Create your views here.

def website_index(request):
    return render(request,'index.html')



def menu_index(request):
    return render(request,'menu.html')



def about(request):
    return render(request,'about.html')



def contact(request):
    message= ""
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Your message has been successfully sent!"
        else:
            message = "There was an error with your submission. Please correct the errors below."

    else:
        form = ContactForm()
    return render(request,'contacts.html',{'form':form,'message':message})




def menu_index_persian(request):
    return render(request,'menu-persian.html')



def about_persian(request):
    return render(request,'about-persian.html')



def contact_persian(request):
    message= ""
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Your message has been successfully sent!"
        else:
            message = "There was an error with your submission. Please correct the errors below."

    else:
        form = ContactForm()
    return render(request,'contact-persian.html',{'form':form,'message':message})