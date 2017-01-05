from django.shortcuts import render
from .models import Brand, Product

# Create your views here.

def brand_detail(request):
	context = {}
	return render(request, 'product/brand.html', context)

def product_detail(request):
	context = {}
	return render(request, 'product/product.html', context)




