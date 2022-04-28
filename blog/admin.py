from django.contrib import admin
from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status' ,'posted_date')
    search_fields = ['title', 'content']
    list_filter = ('status', 'posted_date')
    prepopulated_fields = {'slug': ('title',)}
