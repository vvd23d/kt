from django.urls import path
from django.urls import re_path

from .views import (
    BitcoinListView,
    LastBtcAPIView,
)


urlpatterns = [
    path('', BitcoinListView.as_view()),
    path('last/', LastBtcAPIView.as_view()),
]
