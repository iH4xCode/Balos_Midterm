from django.contrib import admin
from django.urls import path, include
from django.urls import path
from .views import  HomepageView, AboutpageView, ContactpageView, ProductpageView, LoginformpageView, ProductsListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomepageView.as_view(), name = 'home'),
    path('about/', AboutpageView.as_view(),name = 'about'),
    path('contact/', ContactpageView.as_view(),name = 'contact'),
    path('product/', ProductpageView.as_view(), name='product'),
    path('loginform/',LoginformpageView.as_view(), name='loginform'),
    path('Product/', ProductsListView.as_view(), name='product'),

]