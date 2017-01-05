from django.shortcuts import render
from .models import Brand, Product

# Create your views here.

def brand_detail(request):
	context = {}
	brands = request.GET.get('name')
	return render(request, 'brandpage.html', context)




def product_detail(request):
	context = {}
	products = request.GET.get('title')
	return render(request, 'productpage.html', context)





