from django.db import models


class Band(models.Model):
    class Meta:
        db_table = "band"

    name = models.CharField(max_length=200)
