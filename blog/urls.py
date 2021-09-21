from django.urls import path

from blog import views
from blog.views import HomeView, ArticleDetailView, \
    AddPostView, UpdatePostView, DeletePostView, AddCatetoryView, \
    CategoryPostView, LikeView, AddCommentView, searchPost

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add-post"),
    path('article/<int:pk>/edit', UpdatePostView.as_view(), name="update-post"),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete-post"),
    path('add_category/', AddCatetoryView.as_view(), name = 'add-category' ),
    path('category/<int:pk>', CategoryPostView.as_view(), name="category-posts"),
    path('like/<int:pk>', LikeView, name = 'like_post'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name="add-comment"),
path('search_posts/', searchPost, name="search-post"),

]
