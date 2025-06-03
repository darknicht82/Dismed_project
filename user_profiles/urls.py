from django.urls import path
from .views import assign_unit_view

urlpatterns = [
    path("", assign_unit_view, name="assign_unit"),
]
