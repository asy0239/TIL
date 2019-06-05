from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),

    # create
    path('new/', views.new_article),  # /board/new/
    path('create/', views.create_article),

    # read
    path('', views.article_list),
    path('<int:article_id>', views.article_detail),

    # update
    path('<int:article_id>/edit/', views.edit_article),
    path('<int:article_id>/update/', views.update_article),

    # delete
    path('<int:article_id>/delete/', views.delete_article),

]