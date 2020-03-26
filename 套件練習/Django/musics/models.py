from django.db import models
# Create your models here.
class Music(models.Model):
    song = models.TextField(default="song")
    singer = models.TextField(default="default_singer")
    last_modifty_date=models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "music"
