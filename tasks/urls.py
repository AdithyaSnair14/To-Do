from django.urls import path
from .views import create_task, task_list,update_task


urlpatterns = [
    path('list/', task_list, name='task_list'),
    path('create/', create_task, name="create_task"),
    path('update/<int:id>/', update_task, name='update_task')
]