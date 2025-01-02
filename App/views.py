from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Product
class HomepageView(TemplateView):
      template_name = 'home.html'

class AboutpageView(TemplateView):
      template_name = 'about.html'

class ContactpageView(TemplateView):
      template_name = 'contact.html'


class ProductpageView(TemplateView):
      template_name = 'product.html'


class  LoginformpageView(TemplateView):
       template_name = 'loginform.html'


class ProductsListView(ListView):
     model = Product
     template_name = 'Product.html'
     context_object_name = 'product_list'