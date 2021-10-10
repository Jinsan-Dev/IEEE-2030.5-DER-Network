from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('monitor/', views.monitor, name='monitor'),
    path('post/', views.systemDataList),
    path('getCommand/<int:pk>/', views.getCommand)
]