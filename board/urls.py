
from django.urls import path

from board.views import BoardListAPIView, BoardDetailListAPIView, TaskListAPIView

urlpatterns = [
    path('board', BoardListAPIView.as_view()),
    path('board/<int:pk>', BoardDetailListAPIView.as_view()),

    path('columns/<int:board_id>', TaskListAPIView.as_view()),

]
