# Generated by Django 4.2 on 2024-11-16 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_workhistory_ratings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='created_at',
            new_name='date_submitted',
        ),
        migrations.AlterField(
            model_name='contact',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
