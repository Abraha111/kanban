from rest_framework import serializers

from board.models import Board, Column, Task, SubTask


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

    def to_representation(self, instance: Task):
        rep = super().to_representation(instance)
        sub_tasks = instance.subtask_set.all()
        rep['sub_tasks'] = SubTaskSerializer(sub_tasks, many=True).data
        return rep


# class ColumnParentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Column
#         fields = ('id', 'title')
#
#     def to_representation(self, instance: Column):
#         rep = super().to_representation(instance)
#         tasks = instance.task_set.all()
#         rep['tasks'] = TaskSerializer(tasks, many=True).data
#         return rep


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ('id', 'title')


class BoardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'title')

    def to_representation(self, instance: Board):
        rep = super().to_representation(instance)
        columns = instance.column_set.all()
        rep['columns'] = ColumnSerializer(columns, many=True).data
        return rep


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'




















