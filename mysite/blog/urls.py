from django.urls import path

from .views import *

# as_view() - имя метода, совпадающее с именем класса? или запустить стандартный метод get()?
urlpatterns = [
    path('', PostsList.as_view(), name='posts_list_url'),  # имя урла можно вставлять в шаблоны, так правильно
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),

    path('tags/', TagsList.as_view(), name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url')


]
