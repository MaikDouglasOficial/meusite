from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('rascunhos/', views.post_draft_list, name='post_draft_list'),
    path('sobre/', views.sobre, name='sobre'),
    path('sugestao/', views.sugestao, name='sugestao'),
    path('post/<int:pk>/publicar/', views.post_publicar, name='post_publicar'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('comment_added/', views.comment_added, name='comment_added'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
