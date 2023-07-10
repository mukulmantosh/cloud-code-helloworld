from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response

from . import serializers
from .models import TodoList


class TodoCreateListAPIView(ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = serializers.TodoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"status": "success", "message": "Data Received ! Thank You"},
                        status=status.HTTP_201_CREATED, headers=headers)


class TodoAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = serializers.TodoSerializer


