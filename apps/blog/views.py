from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import BlogPost, BlogTag
from .forms import BlogPostForm, BlogTagForm

@login_required
def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'admin_panel/blog/list.html', {'posts': posts, 'page_title': 'Blog Posts'})

@login_required
def blog_add(request):
    form = BlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        if post.published and not post.published_at:
            post.published_at = timezone.now()
        post.save()
        form.save_m2m()
        messages.success(request, 'Blog post created.')
        return redirect('blog:list')
    return render(request, 'admin_panel/blog/form.html', {'form': form, 'page_title': 'Create Post'})

@login_required
def blog_edit(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    form = BlogPostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        if post.published and not post.published_at:
            post.published_at = timezone.now()
        post.save()
        form.save_m2m()
        messages.success(request, 'Blog post updated.')
        return redirect('blog:list')
    return render(request, 'admin_panel/blog/form.html', {'form': form, 'post': post, 'page_title': 'Edit Post'})

@login_required
def blog_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Blog post deleted.')
        return redirect('blog:list')
    return render(request, 'admin_panel/blog/delete.html', {'post': post, 'page_title': 'Delete Post'})

@login_required
def blog_toggle_publish(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    post.published = not post.published
    if post.published and not post.published_at:
        post.published_at = timezone.now()
    post.save()
    messages.success(request, f'Post is now {"published" if post.published else "draft"}.')
    return redirect('blog:list')
