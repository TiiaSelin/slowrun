from django.shortcuts import render
from django.templatetags.static import static
from .models import Viesti, Etusivukuva

def index_view(request):
    front_image = Etusivukuva.objects.last()
    viesti_lahetetty = False
    
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
        viesti_lahetetty = True

    if front_image:
        img_url = front_image.picture.url
    else:
        img_url = static("images/pexels-drerun-22541351.jpg")
        
    
    return render(request, 'index.html', {'viesti_lahetetty': viesti_lahetetty, "img_url": img_url})


def yhteystiedot_view(request):
    viesti_lahetetty = False

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
        viesti_lahetetty = True
        
    return render(request, "yhteystiedot.html", {"viesti_lahetetty": viesti_lahetetty})



