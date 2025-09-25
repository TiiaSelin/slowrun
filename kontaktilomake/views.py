from django.shortcuts import render
from django.templatetags.static import static
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Viesti, Etusivukuva

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
    viesti_lahetetty = laheta_viesti(request)
    if front_image:
        img_url = front_image.picture.url
    else:
        img_url = static("images/pexels-drerun-22541351.jpg")
        
    return render(request, 'index.html', {'viesti_lahetetty': viesti_lahetetty, "img_url": img_url})

@receiver(post_delete, sender=Etusivukuva)
def delete_file_on_object_deletion(sender, instance, **kwargs):
    instance.picture.delete(save=False)

def yhteystiedot_view(request):
    viesti_lahetetty = laheta_viesti(request)
    
    return render(request, "yhteystiedot.html", {"viesti_lahetetty": viesti_lahetetty})



        




