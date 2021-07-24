# Generated by Django 3.2.5 on 2021-07-24 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_create_tables_album_band_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='musics', to='myapp.album'),
        ),
    ]