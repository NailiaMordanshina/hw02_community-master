from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    posts = Post.order_by.all()[:10]
    context = {
        'posts': posts,
        'title': 'Последние обновления на сайте'
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.order_by.all()[:10]
    context = {
        'group': group,
        'title': f'Записи сообщества {slug}',
        'posts': posts,
    }
    return render(request, template, context)
