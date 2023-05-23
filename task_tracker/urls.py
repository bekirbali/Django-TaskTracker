from django.urls import path
from .views import (
    home,
    get_todos,
    todoMVS
)

urlpatterns = [
    path('', home),
    path('get_todos/', get_todos),
]

from rest_framework import routers

router = routers.DefaultRouter()
router.register('todoMVS', todoMVS)

urlpatterns+=router.urls