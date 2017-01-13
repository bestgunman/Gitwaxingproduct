from django.shortcuts import render
from .models import Brand, Product
from reviewapp.views import make_page_range
from reviewapp.models import Review
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def brand_list(request):
	brand_list = Brand.objects.order_by('name')
	paginate = Paginator(brand_list,10)
	page = request.GET.get('page')
	try:
		brand_list = paginate.page(page)
	except PageNotAnInteger:
		brand_list = paginate.page(1)
		page = 1
	except EmptyPage:
		brand_list = paginate.page(paginate.num_pages)
	page = int(page)
	make_page_range_result = make_page_range(page,paginate.num_pages+1)
	board_range = make_page_range_result[0]
	page_previous = make_page_range_result[1]
	page_next = make_page_range_result[2]
	context = {
		'brand_list':brand_list,
		'page_previous':page_previous,
		'page':page,
		'page_next':page_next,
		'board_range':board_range,
		}
	return render(request, 'product/brand_list.html', context)

def brand_detail(request, url):
	brand = Brand.objects.get(url=url)
	context = {'brand':brand,}
	return render(request, 'product/brand.html', context)



#인덱스 페이지
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

def product_detail(request, url1):
	product = Product.objects.get(url=url1)
	review_list = Review.objects.filter(product=product)
	total = 0
	if not review_list.exists():
		score_avg = "아직 평가가 없습니다"
	else:
		for review in review_list:
			total += review.score
		score_avg = round(total/review_list.count(),1)
	context = {'product':product,
				'score_avg':score_avg,
	}
	return render(request, 'product/product.html', context)




















