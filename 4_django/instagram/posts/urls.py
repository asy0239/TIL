
from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    # Read - 전체글보기
    path('', views.index, name="index"),
    # Create - 포스트 작성하기
    path('create/', views.create, name="create"),
    # Update
    path('<int:post_id>/update/', views.update, name='update'),
    # delete
    path('<int:post_id>/delete/', views.delete, name='delete'),

    # Comment_create
    path('<int:post_id>/comments/create/', views.comment_create, name="comment_create"),

    # like
    path('<int:post_id>/likes/', views.likes, name="likes"),
]

