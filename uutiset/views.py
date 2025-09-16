from django.shortcuts import render
from .models import Uutinen

def uutiset_view(request):
    uutiset = Uutinen.objects.all().order_by("date")
    return render(request, "uutiset.html", {"uutiset": uutiset})
    