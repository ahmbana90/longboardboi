from django.urls import path
from . import views

urlpatterns = [
    path("details/<int:id>", views.route_detail, name="route-detail")
]