# Generated by Django 4.2 on 2024-11-16 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_workhistory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stat',
            old_name='engagment',
            new_name='engagement',
        ),
    ]