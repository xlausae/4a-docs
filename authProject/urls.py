"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views

urlpatterns = [
    path('login/',                                  TokenObtainPairView.as_view()),
    path('refresh/',                                TokenRefreshView.as_view()),
    path('user/',                                   views.UserCreateView.as_view()),
    path('user/<int:pk>/',                          views.UserDetailView.as_view()),
    path('product/create/',                         views.ProductCreateView.as_view()), # create a new product
    path('product/<int:user>/',                     views.ProductReadView.as_view()), # view information for all products
    path('product/update/<int:user>/<int:pk>/',     views.ProductUpdateView.as_view()), # update a product
    path('product/remove/<int:user>/<int:pk>/',     views.ProductDeleteView.as_view()), # delete a product
    path('sale/create/',                            views.SaleCreateView.as_view()), # create a new sale
    path('sale/<int:user>/',                        views.SaleReadView.as_view()), # view information for all sales
    path('sale/update/<int:user>/<int:pk>/',        views.SaleUpdateView.as_view()), # update a sale
    path('sale/remove/<int:user>/<int:pk>/',        views.SaleDeleteView.as_view()), # delete a sale
    path('invoice/create/',                         views.InvoiceCreateView.as_view()), # create a new invoice
    path('invoice/<int:user>/',                     views.InvoiceReadView.as_view()), # view information for all invoices
    path('invoice/update/<int:user>/<int:pk>/',     views.InvoiceUpdateView.as_view()), # update a invoice
    path('invoice/remove/<int:user>/<int:pk>/',     views.InvoiceDeleteView.as_view()), # delete a invoice
]

