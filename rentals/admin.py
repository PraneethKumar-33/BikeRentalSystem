from django.contrib import admin
from .models import Customer, Bike, Booking

admin.site.register(Customer)
admin.site.register(Bike)
admin.site.register(Booking)