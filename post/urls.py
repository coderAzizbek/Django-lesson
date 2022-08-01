from django.urls import path
from .views import Yangilik,YangilikCraeteView,YangilikDetailView,YangilikUpdateView

urlpatterns = [
    path('',Yangilik.as_view(),name='home'),
    path('new/',YangilikCraeteView.as_view(),name='post'),
    path('detail/<int:pk>',YangilikDetailView.as_view(),name='detail'),
    path('update/<int:pk>',YangilikUpdateView.as_view(),name='update'),
]