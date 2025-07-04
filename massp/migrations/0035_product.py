# Generated by Django 5.0.2 on 2024-04-10 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('massp', '0034_appointment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='product_photos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
