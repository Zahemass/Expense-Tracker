from django.contrib import admin
from .models import AddItems

# Register your models here.
class AddItemsadmin(admin.ModelAdmin):
    list_display = ("Purpose","Amount","Reason")

    #register Model
admin.site.register(AddItems,AddItemsadmin)    