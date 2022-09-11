from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api'
router = DefaultRouter()
router.register('task-list', views.TodoListView,basename='task_list')
# router.register('task-detail/<int:todo_id>/', views.TodoDetailApiView,basename='task_detail')
urlpatterns = router.urls
