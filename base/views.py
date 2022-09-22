from django.shortcuts import render
from django.http import HttpResponse
from .models import Home, SavedEmail, Publisher


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
    


    return render(request, 'advertiser.html', context)
