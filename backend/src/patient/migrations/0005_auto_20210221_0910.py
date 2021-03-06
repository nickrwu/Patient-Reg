# Generated by Django 3.1.6 on 2021-02-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_auto_20210219_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='dob',
            field=models.DateField(max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='photo_license',
            field=models.ImageField(blank=True, null=True, upload_to='id_images'),
        ),
    ]
