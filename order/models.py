from statistics import mode
from django.db import models

class I_m(models.Model):
    title = models.CharField('Название', max_length=50)
    img = models.ImageField(upload_to= 'media')
    about = models.TextField('Обо мне')
    date = models.DateTimeField('Дата и время публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'


class Projects(models.Model):
    i_m = models.ForeignKey(I_m, on_delete=models.CASCADE)
    title = models.CharField('Название проекта', max_length=100)
    icons = models.ImageField(upload_to = 'icons-1')
    url = models.URLField('URL', max_length=200)
    date = models.DateTimeField('Дата и время публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'