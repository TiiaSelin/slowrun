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
    title = models.CharField(blank=True, max_length=50)
    picture = models.ImageField(upload_to="")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.title == None or self.title == "":
            return f"Kuva lisätty: {self.uploaded_at:%y-%m-%d}"
        return f"{self.title}: {self.uploaded_at:%y-%m-%d}"