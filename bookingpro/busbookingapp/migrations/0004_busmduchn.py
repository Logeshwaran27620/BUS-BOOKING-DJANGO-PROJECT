# Generated by Django 5.0.6 on 2024-07-05 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busbookingapp', '0003_busdetails_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='busmduchn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busname', models.CharField(max_length=23)),
                ('depaturetime', models.CharField(max_length=30)),
                ('arrivaltime', models.CharField(max_length=40)),
                ('traveltime', models.CharField(max_length=23)),
                ('price', models.CharField(max_length=30)),
                ('bustype', models.CharField(max_length=40)),
                ('busratting', models.CharField(max_length=23)),
                ('bustotalratting', models.CharField(max_length=30)),
                ('depaturelocation', models.CharField(max_length=40)),
                ('arrivallocation', models.CharField(max_length=23)),
                ('windowseat', models.CharField(max_length=30)),
                ('seatavailable', models.CharField(max_length=40)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
