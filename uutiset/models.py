from django.db import models
from django.utils import timezone

# Create your models here.
class Uutinen(models.Model):
    """Tietokannan kenttä uutiselle."""

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(upload_to="")

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.pk:
            previous = Uutinen.objects.filter(pk=self.pk).first()
            if previous and previous.picture and previous.picture != self.picture:
                previous.picture.delete(save=False)

        super().save(*args, **kwargs)