# Generated by Django 5.0.1 on 2024-01-28 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy', '0004_alter_kutubxonachi_ish_vaqti_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kutubxonachi',
            name='ish_vaqti',
            field=models.CharField(choices=[('8:00 dan 17:00 gacha', '8:00 dan 17:00 gacha'), ('10:00 dan 21:00 gacha', '10:00 dan 21:00 gacha')], db_default=models.Value('10:00 dan 21:00 gacha'), max_length=50),
        ),
    ]