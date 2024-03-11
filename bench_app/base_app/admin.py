from django.contrib import admin
from .models import CustomUsers, Booking
from import_export import resources

# Register your models here.
class BookingResource(resources.ModelResource):
    class Meta: 
        model = Booking
        fields = ('id', 'resource', 'booked_by', 'booking_date', 'release_date')
        export_order = ('id', 'resource', 'booking_date', 'release_date', 'booked_by')

admin.site.register(CustomUsers)
admin.site.register(Booking)