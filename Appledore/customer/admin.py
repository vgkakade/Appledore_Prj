from django.contrib import admin
from .models import Customer, Address

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','user','mobile_number']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id','customer','default_address']

