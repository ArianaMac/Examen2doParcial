from django import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'ToDoApp')

urlpatterns = [
    path('', include(router.urls)),
]