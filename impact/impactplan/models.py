from django.db import models


# Create your models here.
class Classe(models.Model):
    name = models.CharField(max_length=127)
    classe_groupe = models.CharField(max_length=15)
    prof = models.CharField(max_length=31)
    start = models.DateTimeField()
    end = models.DateTimeField()
    code = models.BigIntegerField(help_text="Le code du cours pour Zoom")
    link = models.CharField(max_length=255)
    posted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
