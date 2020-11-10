from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('reset-celery/', reset_celery, name='reset_celery'),
]
