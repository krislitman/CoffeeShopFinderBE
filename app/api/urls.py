from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()

urlpatterns = [
    path('v1/', include(router.urls)),
]
