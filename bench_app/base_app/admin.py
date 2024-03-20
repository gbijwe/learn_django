from django.contrib import admin
from .models import CustomUsers, Booking, Resource
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, BooleanWidget


class BookingResource(resources.ModelResource):

    resource = fields.Field(
        column_name='resource',
        attribute='resource',
        widget=ForeignKeyWidget(Resource, field='resource_name')
    )

    resource_type = fields.Field(
        column_name='resource_type',
        # Accessing the 'resource_type' field from the related Resource model
        attribute='resource__resource_type',
    )

    description = fields.Field(
        column_name='description',
        # Accessing the 'resource_type' field from the related Resource model
        attribute='resource__description',
    )

    current_status = fields.Field(
        column_name='current_status',
        # Use the 'get_FIELD_display' method for BooleanField
        attribute='get_current_status_display'
    )

    class Meta:
        model = Booking
        fields = ('resource', 'resource_type', 'description', 'owner',
                  'booking_date', 'release_date', 'current_status')
        export_order = ('resource', 'resource_type', 'description',
                        'booking_date', 'current_status', 'release_date', 'owner')


admin.site.register(CustomUsers)
admin.site.register(Booking)
