from django.db import models


class Member(models.Model):
    class Meta:
        db_table = "member"

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    band = models.ForeignKey("Band", related_name="members", on_delete=models.CASCADE)
