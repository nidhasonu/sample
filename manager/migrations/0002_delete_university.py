# Generated by Django 5.1.2 on 2024-12-10 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0016_alter_homeview_university_name'),
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='university',
        ),
    ]
