# Generated by Django 4.2 on 2024-11-14 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_content_alter_stat_engagment_alter_stat_subscribers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='engagment',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='subscribers',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='views',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]