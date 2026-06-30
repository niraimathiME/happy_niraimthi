
from django.urls import path
from app import views

urlpatterns = [
    path("test/", views.test_mongodb, name="test_mongodb"),
]