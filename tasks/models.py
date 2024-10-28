from django.db import models

class Task(models.Model):
    class TaskStatus(models.TextChoices):
        ADDED = 'added', 'Добавлена'
        IN_PROGRESS = 'in_progress', 'В работе'
        COMPLETED = 'completed', 'Выполнена'

    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    status = models.CharField(
        'Статус',
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.ADDED
    )
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_at']

    def __str__(self):
        return self.name