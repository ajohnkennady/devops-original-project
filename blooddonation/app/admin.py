from django.contrib import admin
from .models import Blood,Hospital,Confirmrequest


# Register your models here.

admin.site.register(Hospital)
admin.site.register(Blood)
admin.site.register(Confirmrequest)

