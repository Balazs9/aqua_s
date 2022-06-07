from django.urls import path
from . import views

urlpatterns = [
    path('', views.FeedbackList.as_view(), name='blog'),
    path('create/', views.BlogCreate.as_view(), name='blog_create'),
    path('edit/<slug:slug>', views.BlogUpdate.as_view(), name='blog_edit'),
    path('comment/<slug:slug>', views.FeedbackDetail.as_view(), name='feedback_detail'),
    path('like/<slug:slug>', views.FeedbackLike.as_view(), name='feedback_like'),
]
