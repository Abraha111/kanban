from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)

    
class Board(models.Model):
    title = models.CharField(max_length=255)

    @property
    def get_columns(self):
        return self.column_set.all()


class Column(models.Model):
    title = models.CharField(max_length=255)
    board = models.ForeignKey('board.Board', models.CASCADE)


class Task(models.Model):
    class ImportanceChoice(models.TextChoices):
        HIGH = 'High', 'high'
        MEDIUM = 'Medium', 'medium'
        LOW = 'Low', 'low'

    title = models.CharField(max_length=255)
    description = models.TextField()
    importance = models.CharField(max_length=255, choices=ImportanceChoice.choices)

    status = models.ForeignKey('board.Column', models.CASCADE)
    user = models.ForeignKey('user.User', models.CASCADE)


class SubTask(models.Model):
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)

    task = models.ForeignKey('board.Task', models.CASCADE)







