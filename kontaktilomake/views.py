from django.shortcuts import render
from .models import Viesti




def index_view(request):
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
        
    
    return render(request, 'index.html', {'viesti_lahetetty': viesti_lahetetty})
