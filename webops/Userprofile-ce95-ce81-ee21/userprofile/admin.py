from django.contrib import admin
from userprofile.models import *

class MyModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Userprofile, MyModelAdmin)
