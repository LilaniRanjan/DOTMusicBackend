# Generated by Django 5.1.4 on 2025-01-23 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DOTMusiccrudApp', '0006_songs'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='songs_covers/'),
        ),
    ]
