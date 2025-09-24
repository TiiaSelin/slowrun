from django.db import models

class Viesti(models.Model):
    nimi = models.CharField(max_length=100)
    sahkoposti = models.EmailField()
    paikkakunta = models.CharField(max_length=200)
    viesti = models.TextField()
    luotu = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nimi

class Etusivukuva(models.Model):
    picture = models.ImageField(upload_to="")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Kuva lisätty: {self.uploaded_at:%y-%m-%d}"