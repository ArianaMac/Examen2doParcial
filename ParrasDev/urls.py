from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ToDoViewSet

router = DefaultRouter()
router.register(r'ToDoList', ToDoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
