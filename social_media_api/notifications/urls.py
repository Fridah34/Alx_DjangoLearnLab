from django.urls import path
from .views import list_notifications, mark_notification_read, mark_all_read

urlpatterns = [
    path('', list_notifications, name='list_notifications'),
    path('<int:pk>/read/', mark_notification_read, name='mark_notification_read'),
    path('read-all/', mark_all_read, name='mark_all_read'),
]
