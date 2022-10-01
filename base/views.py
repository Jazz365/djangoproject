from django.shortcuts import render
from django.http import HttpResponse
from .models import Home, SavedEmail, Publisher, Advertiser, Company, TrafficPage, ContactPage, LoginPage, SignUpPage


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
    contact, created = ContactPage.objects.get_or_create(id=1)
    context['i'] = contact
    

    return render(request, 'contact.html', context)

def signup(request):
    context = {}
    signup, created = SignUpPage.objects.get_or_create(id=1)
    context['i'] = signup
    
    return render(request, 'signup.html', context)

def login(request):
    
    
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        action = request.POST.get('action')

        r = requests.post('https://198.199.88.236:8000/login.trackier.com', data={'name': name, 'password': password, 'action':action})
        if r.status_code == 200:
            response = r.json()
            token = response['token']
            # Save token to session
            request.session['api_token'] = token
        else:
            messages.error(request, 'Authentication failed')
            return HttpResponseRedirect(reverse('login'))
   
    context = {}
    login, created = LoginPage.objects.get_or_create(id=1)
    context['i'] = login
    

    return render(request, 'login.html', context)

