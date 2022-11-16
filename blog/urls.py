from django.urls import path
from blog.views import (
    PostListView,
    PostDetailView,
    CategoryPostListView,
    TagPostListView,
    SearchPostListView,
    CommentCreatView,
    CommentDeleteView,
    ReplyCreatView,
    ReplyDeleteView,
)

    

urlpatterns = [
    path("", PostListView.as_view(),name = "post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(),name = "post-detail"),
    path("category/<str:slug>/", CategoryPostListView.as_view(),name = "category-post-list"),
    path("tag/<str:slug>/", TagPostListView.as_view(),name = "tag-post-list"),
    path("Search/", SearchPostListView.as_view(),name = "search-post-list"),
    path("comment/<int:post_pk>/", CommentCreatView.as_view(),name = "comment"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(),name = "comment-delete"),
    path("reply/<int:comment_pk>/", ReplyCreatView.as_view(),name = "reply"),
    path("reply/<int:pk>/delete/", ReplyDeleteView.as_view(),name = "reply-delete"),
]