from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', views.index),
    # path('hello/<str:name>/', views.hello),
    path('home/', include('home.urls')),
    path('utils/', include('utils.urls')),

]
