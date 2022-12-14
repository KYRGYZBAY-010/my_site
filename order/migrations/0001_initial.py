# Generated by Django 4.0.6 on 2022-07-15 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='I_m',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('about', models.TextField(verbose_name='Обо мне')),
                ('date', models.DateTimeField(verbose_name='Дата и время публикации')),
            ],
            options={
                'verbose_name': 'Обо мне',
                'verbose_name_plural': 'Обо мне',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название проекта')),
                ('icons', models.ImageField(blank=True, null=True, upload_to='')),
                ('url', models.URLField(verbose_name='URL')),
                ('date', models.DateTimeField(verbose_name='Дата и время публикации')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
    ]
