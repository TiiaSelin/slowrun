from django.shortcuts import render, get_object_or_404
from .models import Uutinen

def uutiset_view(request):
    uutiset = Uutinen.objects.all().order_by("date")
    return render(request, "uutiset.html", {"uutiset": uutiset})
    
def uutinen_detail(request, uutinen_id):
    uutinen = get_object_or_404(Uutinen, id=uutinen_id)
    return render(request, "uutinen_detail.html", {"uutinen": uutinen})