from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # utils/
    path('art/<str:keyword>/', views.artii),  # utils/art/<KEYWORD>
    path('stock_input/', views.stock_input),  # utils/stock_input/
    path('stock_output/', views.stock_output),  # utils/stock_output/
]