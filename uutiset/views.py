from django.shortcuts import render

def uutiset_view(request):
    return render(request, "uutiset.html")