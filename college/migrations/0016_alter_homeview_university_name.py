# Generated by Django 5.1.2 on 2024-12-10 18:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0015_remove_collegemodel_coures'),

    ]

    operations = [
        migrations.AlterField(
            model_name='homeview',
            name='university_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='universityapp.university'),
        ),
    ]
