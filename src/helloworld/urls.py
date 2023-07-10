from django.urls import path, include

urlpatterns = [
    path('', include('helloapp.urls')),
    path('todo/', include('todo.urls')),
]
