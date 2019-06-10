from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    # Read
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),

    # Create
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    #Delete
    path('<int:article_id>/delete/', views.delete, name='delete'),

    # update
    # path('<int:article_id>/edit/', views.edit, name='edit'),
    path('<int:article_id>/update/', views.update, name='update'),
]