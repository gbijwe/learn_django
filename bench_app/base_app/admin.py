from django.contrib import admin
from .models import CustomUsers, Booking, Resource
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, BooleanWidget

# Register your models here.
class BookingResource(resources.ModelResource):

    resource = fields.Field(
        column_name = 'resource', 
        attribute = 'resource', 
        widget = ForeignKeyWidget(Resource, field='resource_name')
    )

    res_type = fields.Field(
        column_name='res_type',
        attribute= 'res_type', 
        widget=ForeignKeyWidget(Resource, field='resource_type')
    )
    
    current_status = fields.Field(
        column_name='current_status',
        attribute='get_current_status_display'  # Use the 'get_FIELD_display' method for BooleanField
    )

    # owner = fields.Field(
    #     column_name='owner',
    #     attribute='owner',
    #     widget=ForeignKeyWidget(CustomUsers, field='username')
    # )

    class Meta: 
        model = Booking
        fields = ('id', 'resource', 'res_type', 'owner', 'booking_date', 'release_date', 'current_status')
        export_order = ('id', 'resource', 'res_type', 'booking_date', 'current_status', 'release_date', 'owner')

admin.site.register(CustomUsers)
admin.site.register(Booking)