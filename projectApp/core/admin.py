from django.contrib import admin
from .models import Tabs, Item, ProjectList

# Register your models here.
admin.site.register(Tabs)
admin.site.register(Item)
admin.site.register(ProjectList)