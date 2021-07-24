from django.db import models


class Music(models.Model):
    class Meta:
        db_table = "music"

    title = models.CharField(max_length=200)
    seconds = models.IntegerField()
    album = models.ForeignKey(
        "Album", related_name="musics", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.title
