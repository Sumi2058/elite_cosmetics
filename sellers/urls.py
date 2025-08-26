from django.urls import path
from . import views

urlpatterns = [
    path('sellers/', views.seller_list, name='seller_list'),
    path('sellers/create/', views.seller_create, name='seller_create'),
    path('sellers/<int:pk>/', views.seller_detail, name='seller_detail'),
    path('sellers/<int:pk>/update/', views.seller_update, name='seller_update'),
    path('sellers/<int:pk>/delete/', views.seller_delete, name='seller_delete'),
]
