# Generated by Django 4.2 on 2024-11-19 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_youtubevideo_youtube_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatordetail',
            name='date_submitted',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='creatordetail',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='youtubevideo',
            name='youtube_link',
            field=models.URLField(blank=True),
        ),
    ]
