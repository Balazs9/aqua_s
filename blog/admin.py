from django.contrib import admin
from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','posted_date')
    search_fields = ['title', 'content']
    list_filter = ('status', 'posted_date')
    prepopulated_fields = {'slug': ('title',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'chatbox', 'post', 'posted_date', 'approved')
    list_filter = ('posted_date', 'approved')
    search = ('name', 'email', 'chatbox')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(approved=True)
