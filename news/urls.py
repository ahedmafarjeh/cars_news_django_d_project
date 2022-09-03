from django.urls import path
from . import views
urlpatterns = [
    path("news/<news_id>/",views.News, name='news_page'),
    #path("news/<news_id>/",views.NewsListView.as_view(), name='news_page'),
    path("news/<news_id>/New News",views.NewNews, name='new_news'),
    path("news/<news_id>/topics/<topic_id>", views.topic_posts, name='topic_posts'),
    path("news/<news_id>/topics/<topic_id>/create_comment", views.comment, name='comment'),
    path("news/<news_id>/topics/<topic_id>/posts/<post_id>/Edit", views.PostUpdateView.as_view(), name='edit_post'),

]