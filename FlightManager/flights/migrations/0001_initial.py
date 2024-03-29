# Generated by Django 4.1.7 on 2023-02-18 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_location', models.CharField(max_length=20)),
                ('to_location', models.CharField(max_length=20)),
                ('takeoff_time', models.TimeField()),
                ('landing_time', models.TimeField()),
                ('plane_type', models.CharField(max_length=20)),
                ('plane_id', models.CharField(max_length=20)),
                ('pilot_name', models.CharField(max_length=40)),
                ('normal_ticket_count', models.IntegerField()),
                ('business_ticket_count', models.IntegerField()),
                ('normal_ticket_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('business_ticket_price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('EGN', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=12)),
                ('role', models.CharField(default='staff', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('mname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('EGN', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=12)),
                ('nationality', models.CharField(max_length=2)),
                ('ticket_type', models.CharField(max_length=8)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.flight')),
            ],
        ),
    ]
