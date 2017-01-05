from django.shortcuts import render, redirect
from .models import Comment, Review
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def review_board(request):
	reviewlists = Review.objects.order_by('-regdate')
	paginate = Paginator(reviewlists,5)
	page = request.GET.get('page')
	try:
		reviewlist = paginate.page(page)
	except PageNotAnInteger:
		reviewlist = paginate.page(1)
	except EmptyPage:
		reviewlist = paginate.page(paginate.num_pages)
	context = {'reviewlist': reviewlist,}
	return render(request, 'review/review_list.html', context)

def review_detail(request, review_id):
	review = Review.objects.get(id=review_id)
	context = {'review':review,}
	return render(request, 'review/review_detail.html',context)

def write_board(request):
	context = {}
	return render(request, 'writepage.html', context)

def save_board(request):
	reviewboard = Review (title = request.POST['title'],
							content = request.POST['content'],
							author = request.POST['author'],
							score = request.POST['score'],
							product = request.POST['product'],
		)
	reviewboard.save()
	return redirect('/review')

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
