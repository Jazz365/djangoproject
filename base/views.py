from django.shortcuts import render
from django.http import HttpResponse
from .models import Home, SavedEmail, Publisher, Advertiser, Company, TrafficPage


# Create your views here.

def index(request):
    context = {}
    home_page, created = Home.objects.get_or_create(id=1)
    context['home_page'] = home_page

    if request.method == 'POST':
        email = request.POST['email']
        saved_email = SavedEmail(email=email)
        if saved_email is not None:
            saved_email.save()
        else:
            return HttpResponse('Something went wrong')

    return render(request, 'index.html', context)


def publishers(request):
    context = {}
    Publishers, created = Publisher.objects.get_or_create(id=1)
    context['p'] = Publishers


    return render(request, 'publishers.html', context)
def advertisers(request):
    context = {}
    advertiser, created = Advertiser.objects.get_or_create(id=1)
    context['i'] = advertiser
    


    return render(request, 'advertiser.html', context)


def company(request):
    context = {}
    company, created = Company.objects.get_or_create(id=1)
    context['i'] = company

    return render(request, 'company.html', context)

def traffic(request):
    context = {}
    traffic, created = TrafficPage.objects.get_or_create(id=1)
    context['i'] = traffic
    
    return render(request, 'traffic.html', context)

def contact(request):
    context = {}
    

    return render(request, 'contact.html', context)

def signup(request):
    context = {}
    
    return render(request, 'signup.html', context)

def login(request):
    context = {}
    

    return render(request, 'login.html', context)

