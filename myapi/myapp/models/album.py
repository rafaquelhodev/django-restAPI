from django.db import models


class Album(models.Model):
    class Meta:
        db_table = "album"

    title = models.CharField(max_length=200)
    band = models.ForeignKey("Band", related_name="albuns", on_delete=models.CASCADE)
    date = models.DateField()
