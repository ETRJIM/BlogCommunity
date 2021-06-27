from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.urls import reverse_lazy
from blog.models import BlogPost,BlogComment
from blog.forms import BlogPostForm,BlogCommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self):
        return BlogPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = BlogComment.objects.filter(post=context['blogpost'])
        return context

class BlogPostCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/blogpost_detail.html'
    form_class = BlogPostForm
    model = BlogPost

class BlogPostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/blogpost_detail.html'
    form_class = BlogPostForm
    model = BlogPost

class BlogPostDeleteView(LoginRequiredMixin,DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blogpost_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name ='blog/blogpost_list.html'
    model = BlogPost

    def get_queryset(self):
        return BlogPost.objects.filter(published_date__isnull=True).order_by('created_date')


#Comment
@login_required
def post_publish(request,pk):
    post = get_object_or_404(BlogPost,pk=pk)
    post.publish()
    post.save()
    return redirect('blogpost_detail',pk=pk)

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(BlogPost,pk=pk)
    if request.method == 'POST':
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blogpost_detail',pk=post.pk)
    else:
        form = BlogCommentForm()
        return render(request,'blog/blogcomment.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(BlogComment,pk=pk)
    comment.approve()
    comment.save()
    return redirect('blogpost_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(BlogComment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blogpost_detail',pk=post_pk)
 
def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return render(response,'registration/login.html')
    else:
        form = UserCreationForm()
    return render(response,'registration/register.html',{"form":form})
 