from django.db import models

class Articles(models.Model):
    title = models.CharField('Проект', max_length=50)
    anons = models.CharField('Ссылка', max_length=250)
    full_text = models.TextField('Описание проекта')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/projects/{self.id}'

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'