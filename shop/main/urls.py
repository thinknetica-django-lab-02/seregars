from django.urls import path

from  main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('goods/', views.ProductListView.as_view(), name='goods'),
    path('goods/<int:pk>/', views.ProductDetailView.as_view(), name='detail_goods'),
    path('accounts/profile/', views.user_profile, name='profile'),
    path('goods/add', views.ProductCreate.as_view(), name='create_product'),
    path('goods/<int:pk>/edit', views.ProductUpdate.as_view(), name='edit_product'),
]
