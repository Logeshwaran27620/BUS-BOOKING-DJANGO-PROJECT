from django.contrib import admin
from busbookingapp.models import buschndpm, busdetails, busdpmchn, busmduchn  

class busadmin(admin.ModelAdmin):
    list_display = (    'busname',
    'depaturetime',
    'arrivaltime',
    'traveltime',
    'price',
    'bustype',
    'busratting',
    'bustotalratting',
    'depaturelocation',
    'arrivallocation',
    'windowseat',
    'seatavailable',
)
admin.site.register(busdetails,busadmin)

class busadmin(admin.ModelAdmin):
    list_display = (    'busname',
    'depaturetime',
    'arrivaltime',
    'traveltime',
    'price',
    'bustype',
    'busratting',
    'bustotalratting',
    'depaturelocation',
    'arrivallocation',
    'windowseat',
    'seatavailable',
)
admin.site.register(busmduchn,busadmin)

class busadmin(admin.ModelAdmin):
    list_display = (    'busname',
    'depaturetime',
    'arrivaltime',
    'traveltime',
    'price',
    'bustype',
    'busratting',
    'bustotalratting',
    'depaturelocation',
    'arrivallocation',
    'windowseat',
    'seatavailable',
)
admin.site.register(buschndpm,busadmin)

class busadmin(admin.ModelAdmin):
    list_display = (    'busname',
    'depaturetime',
    'arrivaltime',
    'traveltime',
    'price',
    'bustype',
    'busratting',
    'bustotalratting',
    'depaturelocation',
    'arrivallocation',
    'windowseat',
    'seatavailable',
)
admin.site.register(busdpmchn,busadmin)


# admin.py
from django.contrib import admin
from .models import  Bookingselection 


class BookingAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination')
    search_fields = ('origin', 'destination')
admin.site.register(Bookingselection,BookingAdmin)
