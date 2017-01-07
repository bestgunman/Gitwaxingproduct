from django.shortcuts import render, redirect
from .models import Comment, Review
from productapp.models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

def make_page_range(current,total_page):
	divn = 10
	range_index=divmod(current-1,divn)[0]
	page_range = range((range_index)*divn+1, (range_index+1)*divn+1)
	page_previous = range_index*divn
	page_next = (range_index+1)*divn+1
	if((range_index+1)*divn>total_page):
		page_range = range((range_index)*divn+1,total_page)
		page_next = 0
	if(range_index == 0):
		page_previous = 0
	return [page_range,page_previous,page_next]

def review_board(request):
	reviewlists = Review.objects.order_by('-regdate')
	paginate = Paginator(reviewlists,10)
	page = request.GET.get('page')
	try:
		reviewlist = paginate.page(page)
	except PageNotAnInteger:
		reviewlist = paginate.page(1)
		page = 1
	except EmptyPage:
		reviewlist = paginate.page(paginate.num_pages)
	page = int(page)
#pagination for divn group
	make_page_range_result = make_page_range(page,paginate.num_pages+1)
	board_range = make_page_range_result[0]
	page_previous = make_page_range_result[1]
	page_next = make_page_range_result[2]
	context = {
		'reviewlist': reviewlist,
		'page_previous':page_previous,
		'page':page,
		'page_next':page_next,
		'board_range':board_range,
		}
	return render(request, 'review/review_list.html', context)

def review_detail(request, review_id):
	review = Review.objects.get(id=review_id)
	context = {'review':review,}
	return render(request, 'review/review_detail.html',context)

def write_board(request, url):
	if not request.user.is_authenticated():
		return redirect('login')
	if request.method=="POST":
		title = request.POST['title']
		content = request.POST['content']
		author = request.user
		score = request.POST['score']
		product = Product.objects.get(url=url)
		reviewboard = Review (title = title,
								content = content,
								author = author,
								score = score,
								product = product,
			)
#이미지 넣는경우
		if len(request.FILES) != 0:
			reviewboard.reviewimg = request.FILES['reviewimg']
		reviewboard.save()
		return redirect('/review')
	else:
		context = {}
		return render(request, 'review/review_write.html', context)

def save_comment(request):
	context = {}
	commentcontent = Comment (guest = request.POST['guest'],
							comment = request.POST['comment'],
							reviews = request.POST['reviews'],
		)
	commentcontent.save()
	return redirect()

def goto_write(request):
	return redirect('/review/writeboard')
