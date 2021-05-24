from django.contrib import admin
from django.urls import path
from api.views import TaskList, TaskDetail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', TaskList.as_view()),
    path('api/tasks/<int:pk>/', TaskDetail.as_view()),
]
