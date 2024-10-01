from django.urls import path
from .views import product_list, add_to_cart, checkout, add_product, buy_now, cart_view
from django.contrib.auth import views as auth_views
from . import views
from .views import buy_now, watchlist_view

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', add_product, name='add_product'),
    path('product/<int:product_id>/add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', checkout, name='checkout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('buy-now/<int:product_id>/', views.buy_now, name='buy_now'),
    path('product/<int:product_id>/add-to-watchlist/', views.add_to_watchlist, name='add_to_watchlist'),
    path('cart/', cart_view, name='cart'),
    path('watchlist/', watchlist_view, name='watchlist'),
]
