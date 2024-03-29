# Generated by Django 5.0.1 on 2024-01-15 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kutubxona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=20)),
                ('ish_vaqti', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=20)),
                ('jins', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=20)),
                ('tugilgan_sana', models.DateField()),
                ('Kitoblar_soni', models.PositiveIntegerField()),
                ('tirik', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=20)),
                ('kurs', models.PositiveIntegerField()),
                ('kitob_soni', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('janr', models.CharField(max_length=20)),
                ('sahifa', models.PositiveIntegerField()),
                ('muallif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asosiy.muallif')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olingan_sana', models.DateField()),
                ('qaytardi', models.BooleanField(default=False)),
                ('qaytarish_soni', models.PositiveIntegerField()),
                ('Kitob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asosiy.kitob')),
                ('kutubxonachi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asosiy.kutubxona')),
                ('talaba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asosiy.talaba')),
            ],
        ),
    ]
