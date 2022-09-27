from django.contrib import admin
from .models import Home,SavedEmail, Publisher, Advertiser, Company
# Register your models here.
admin.site.register(Home)
admin.site.register(SavedEmail)
admin.site.register(Publisher)
admin.site.register(Advertiser)

admin.site.register(Company)
