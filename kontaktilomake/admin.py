from django.contrib import admin
from .models import Viesti, Etusivukuva, Karttakuva

admin.site.register(Viesti)
admin.site.register(Etusivukuva)
admin.site.register(Karttakuva)