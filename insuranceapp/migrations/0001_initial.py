# Generated by Django 5.0.4 on 2024-06-21 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('qualification', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('place', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('annual_income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('aadhar_card_number', models.CharField(max_length=50)),
                ('pan_card_number', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insuranceapp.agent')),
            ],
        ),
    ]