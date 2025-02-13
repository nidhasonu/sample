# Generated by Django 5.1.2 on 2025-01-08 21:06

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0021_remove_ratingandreview_item_and_more'),
        ('student', '0009_delete_request'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SeatTransferRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_type', models.CharField(choices=[('SEAT', 'Seat Request'), ('TRANSFER', 'Transfer Request')], max_length=10)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], default='PENDING', max_length=10)),
                ('date_submitted', models.DateTimeField(default=datetime.datetime.now)),
                ('reason', models.TextField(blank=True, null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.collegemodel')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.vacancy')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
