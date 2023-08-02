from django.contrib import admin
from board.models import Board, Column, Task, SubTask

admin.site.register(Board)
admin.site.register(Column)
admin.site.register(Task)
admin.site.register(SubTask)
