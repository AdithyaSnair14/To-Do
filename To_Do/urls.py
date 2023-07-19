from django.contrib import admin
from django.urls import path
from tasks.views import create_task, task_list, update_task, delete_task


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', create_task, name='create_task'),
    path('', task_list, name='task_list'),
    path('update/<int:id>/', update_task, name='update_task'),
    path('delete/', delete_task)
]
