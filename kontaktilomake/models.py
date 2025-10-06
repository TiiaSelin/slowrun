from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

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
        date_str = self.uploaded_at.strftime("%y-%m-%d") if self.uploaded_at else "no-date"
        if self.title == None or self.title == "":
            return f"Kuva lisätty: {date_str}"
        return f"{self.title}: {date_str}"
    
    def save(self, *args, **kwargs):
        if self.pk:
            previous = Etusivukuva.objects.filter(pk=self.pk).first()
            if previous and previous.picture and previous.picture != self.picture:
                previous.picture.delete(save=False)

        super().save(*args, **kwargs)

class Karttakuva(models.Model):
    url = models.CharField(max_length=2000, validators=[URLValidator()])

    def clean(self):
        super().clean()
        if self.url and not self.url.startswith("https://www.google.com/maps/embed"):
            raise ValidationError("Vain google maps kartat käyvät.")