# Generated by Django 4.0.6 on 2022-09-13 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='i_m',
            name='img',
            field=models.ImageField(upload_to='static/my_img'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='icons',
            field=models.ImageField(upload_to=''),
        ),
    ]
