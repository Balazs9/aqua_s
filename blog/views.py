from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .models import Feedback
from .forms import CommentForm


class FeedbackList(generic.ListView):
    model = Feedback
    queryset = Feedback.objects.filter(status=1).order_by('-posted_date')
    paginate_by = 6
    template_name = 'blog/blog.html'


class BlogCreate(CreateView):
    model = Feedback
    fields = ['title', 'user']
    template_name = 'blog/create_blog.html'


class FeedbackDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Feedback.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-posted_date')

        return render(
            request,
            'blog/comment_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Feedback.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-posted_date')
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'blog/comment_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'comment_form': comment_form
            },
        )


class FeedbackLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Feedback, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
    
        return HttpResponseRedirect(reverse('feedback_detail', args=[slug]))