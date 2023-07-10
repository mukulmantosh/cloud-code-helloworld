from django.urls import path

from .views import TodoAPIView, TodoCreateListAPIView

app_name = "todo"

urlpatterns = [
    path('', TodoCreateListAPIView.as_view(), name="create-todo"),
    path('<int:pk>', TodoAPIView.as_view(), name="update-delete-retrieve-todo")

]
