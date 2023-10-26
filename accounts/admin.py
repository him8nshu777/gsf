from django.contrib import admin
from .models import Customer,Employee, UserProfile

# Register your models here.
# admin.site.register()
admin.site.register(UserProfile)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user']
