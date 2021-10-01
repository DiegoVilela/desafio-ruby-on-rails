from django.urls import path

from . import views

urlpatterns = [
    path('', views.upload, name='index'),
    path('shop/<int:id>', views.shop_detail, name='shop_detail'),
]
