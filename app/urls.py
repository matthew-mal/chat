from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.check_view, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.get_messages, name='getMessages'),
]
