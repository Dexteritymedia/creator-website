# Generated by Django 4.2 on 2024-11-17 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_youtubevideo_alter_content_image_alter_content_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubevideo',
            name='youtube_code',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
