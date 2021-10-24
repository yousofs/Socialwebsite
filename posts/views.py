from django.shortcuts import render, redirect
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import AddPostForm
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required


def all_posts(request):
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/all_posts.html', {'posts': posts})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, created__year=year, created__month=month, created__day=day, slug=slug)
    return render(request, 'posts/post-detail.html', {'post': post})


@login_required
def add_post(request, user_id):
    if request.user.id == user_id:
        if request.method == 'POST':
            form = AddPostForm(request.POST)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.user = request.user
                new_post.slug = slugify(form.cleaned_data['body'][:15])
                new_post.save()
                messages.success(request, 'Your post has successfully submitted!', 'success')
                return redirect('account:dashboard', user_id)
        else:
            form = AddPostForm()
        return render(request, 'posts/add_post.html', {'form': form})
    else:
        return redirect('posts:all_posts')


@login_required()
def post_delete(request, user_id, post_id):
    if user_id == request.user.id:
        Post.objects.filter(pk=post_id).delete()
        messages.success(request, 'Your post deleted successfully!', 'success')
        return redirect('account:dashboard', user_id)
    else:
        return redirect('posts:all_posts')
