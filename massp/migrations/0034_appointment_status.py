# Generated by Django 5.0.2 on 2024-04-04 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('massp', '0033_remove_appointment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(default='PENDING', max_length=100),
        ),
    ]
