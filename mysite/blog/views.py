from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse

from .models import Post, Tag
from .utils import *
from .forms import *

from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q


class PostDetail(ObjectDetailMixin, View):

    # метод get по умолчанию обрабатывает get запросы. переопределили
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):

    model_form = PostForm
    template = 'blog/post_create_form.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):

    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):

    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exception = True


class PostsList(View):

    def get(self, request):
        search_query = request.GET.get('search', '')

        if search_query:
            # если без Q, то в результате получаем посты,
            # в title И! в body которых есть query, для норм поиска нужен класс Q
            posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
        else:
            posts = Post.objects.all()

        page, is_paginated, next_url, prev_url = BlogPaginator.pag_posts(request=request, posts=posts)

        context = {
            'page_object': page,
            'is_paginated': is_paginated,
            'next_url': next_url,
            'prev_url': prev_url
        }

        return render(request, "blog/index.html", context=context)


class TagDetail(ObjectDetailMixin, View):

    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):

    model_form = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):

    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'
    raise_exception = True


class TagsList(View):

    def get(self, request):
        tags = Tag.objects.all()
        return render(request, 'blog/tags_list.html', context={'tags': tags})
