from django.contrib import admin

# Register your models here.
from .models import basic_details

# admin.site.register(basic_details)

class basic_details_display(admin.ModelAdmin):    #We define this class for changing how the data gets displayed on the page
    list_display = ("full_name","mobile_number", "email_id",)

admin.site.register(basic_details, basic_details_display)