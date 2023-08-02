from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView

from board.models import Board, Task, Column
from board.paginations import CustomPageNumberPagination
from board.serializers import BoardSerializer, BoardDetailSerializer, TaskSerializer


class BoardListAPIView(ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardDetailListAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer


class TaskListAPIView(ListAPIView):
    serializer_class = TaskSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        board_id = self.kwargs['board_id']
        return Task.objects.filter(status__board_id=board_id)








