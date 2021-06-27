from django.urls import path
from blog import views

urlpatterns = [
    path('',views.BlogPostListView.as_view(),name='blogpost_list'),
    path('blogpost/<int:pk>/',views.BlogPostDetailView.as_view(),name='blogpost_detail'),
    path('blogpost/<int:pk>/edit/',views.BlogPostUpdateView.as_view(),name='blogpost_edit'),
    path('blogpost/<int:pk>/remove/',views.BlogPostDeleteView.as_view(),name='blogpost_delete'),
    path('drafts/',views.DraftListView.as_view(),name='blogpost_draft_list'),
    path('blogpost/new/',views.BlogPostCreateView.as_view(),name='blogpost_new'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('blogpost/<int:pk>/comment',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve',views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/remove',views.comment_remove,name='comment_remove'),
    path('blogpost/<int:pk>/publish/',views.post_publish,name='blogpost_publish'),
    path('register/',views.register,name='register'),
]