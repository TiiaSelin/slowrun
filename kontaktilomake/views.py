from django.shortcuts import render
from django.templatetags.static import static
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import Viesti, Etusivukuva, Karttakuva, Osoite

def laheta_viesti(request):
    if request.method == "POST":
        nimi = request.POST.get('nimi')
        sahkoposti = request.POST.get('sahkoposti')
        paikkakunta = request.POST.get('paikkakunta')
        viesti = request.POST.get('viesti')
        
        Viesti.objects.create(
            nimi=nimi,
            sahkoposti=sahkoposti,
            paikkakunta=paikkakunta,
            viesti=viesti
        )
        return True
    return False



def index_view(request):
    front_image = Etusivukuva.objects.last()
    map_image = Karttakuva.objects.last()
    viesti_lahetetty = laheta_viesti(request)
    if front_image:
        img_url = front_image.picture.url
    else:
        img_url = static("images/pexels-drerun-22541351.jpg")

    if map_image:
        validator = URLValidator()
        try:
            validator(map_image.url)
            map_url = map_image.url
        except ValidationError:
            map_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2295.711354875636!2d28.16723845051227!3d61.06314277106505!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x469095fdbaf860b7%3A0x52fa9d54e01c5219!2sSaunarannanpuisto!5e0!3m2!1sfi!2sfi!4v1756575444883!5m2!1sfi!2sfi"
    else:
        map_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2295.711354875636!2d28.16723845051227!3d61.06314277106505!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x469095fdbaf860b7%3A0x52fa9d54e01c5219!2sSaunarannanpuisto!5e0!3m2!1sfi!2sfi!4v1756575444883!5m2!1sfi!2sfi"
        
    return render(request, 'index.html', {'viesti_lahetetty': viesti_lahetetty, "img_url": img_url, "map_url": map_url})

@receiver(post_delete, sender=Etusivukuva)
def delete_file_on_object_deletion(sender, instance, **kwargs):
    instance.picture.delete(save=False)

def yhteystiedot_view(request):
    place = Osoite.objects.last()
    viesti_lahetetty = laheta_viesti(request)

    if place:
        address = place.title
    else:
        address = "Etsinnässä..."
    
    return render(request, "yhteystiedot.html", {"viesti_lahetetty": viesti_lahetetty, "address": address})



        




