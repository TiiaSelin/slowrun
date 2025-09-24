from django.shortcuts import render, get_object_or_404
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Uutinen

def uutiset_view(request):
    uutiset = Uutinen.objects.all().order_by("date")
    return render(request, "uutiset.html", {"uutiset": uutiset})
    
def uutinen_detail(request, uutinen_id):
    uutinen = get_object_or_404(Uutinen, id=uutinen_id)
    return render(request, "uutinen_detail.html", {"uutinen": uutinen})

@receiver(post_delete, sender=Uutinen)
def delete_picture_on_uutinen_deletion(sender, instance, **kwargs):
    if instance.picture:
        instance.picture.delete(save=False)