from django.shortcuts import render
from .models import Brand, Product
from reviewapp.views import make_page_range
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def brand_detail(request):
	context = {}
	return render(request, 'product/brand.html', context)

def product_list(request):
	product_list = Product.objects.order_by('title')
	paginate = Paginator(product_list,10)
	page = request.GET.get('page')
	try:
		product_list = paginate.page(page)
	except PageNotAnInteger:
		product_list = paginate.page(1)
		page = 1
	except EmptyPage:
		product_list = paginate.page(paginate.num_pages)
	page = int(page)
#pagination for divn group
	make_page_range_result = make_page_range(page,paginate.num_pages+1)
	board_range = make_page_range_result[0]
	page_previous = make_page_range_result[1]
	page_next = make_page_range_result[2]
	context = {
		'product_list': product_list,
		'page_previous':page_previous,
		'page':page,
		'page_next':page_next,
		'board_range':board_range,
		}
	return render(request, 'product/product_list.html', context)

def product_detail(request, url):
	product = Product.objects.get(url=url)
	context = {'product':product,}
	return render(request, 'product/product.html', context)

