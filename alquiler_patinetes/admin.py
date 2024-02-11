from django.contrib import admin

from alquiler_patinetes.models import Patinete, Alquiler, Usuario

# Register your models here.
admin.site.register(Patinete)
admin.site.register(Alquiler)
admin.site.register(Usuario)