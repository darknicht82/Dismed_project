# backup_manager/urls.py
from django.urls import path
from .views import crear_backup, import_backup

urlpatterns = [
    path('', crear_backup, name='crear_backup'),
    path('importar/<str:backup_file>/', import_backup, name='import_backup'),
]
