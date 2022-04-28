from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .models import Feedback


class FeedbackList(generic.ListView):
    model = Feedback
    queryset = Feedback.objects.filter(status=1).order_by('-posted_date')
    paginate_by = 6
