from django.urls import path

from .views import *

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'),
    path('add/', BookmarkCV.as_view(), name='create'),
    path('update/<int:pk>', BookmarkUV.as_view(), name='update'),
    path('detail/<int:pk>', BookmarkDV.as_view(), name='detail'),
    path('delete/<int:pk>', BookmarkRV.as_view(), name='delete'),
]