from django.urls import path
from . import views

urlpatterns = [
    path('', views.FeedbackList.as_view(), name='blog'),
]
