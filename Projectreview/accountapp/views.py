from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile
from reviewapp.models import Review

def login_view(request):
	context = {}
	if request.method=="POST":
		user_id = request.POST['username']
		user_pw = request.POST['password']
		user = authenticate(username = user_id, password = user_pw)
		if user is not None:
			login(request, user)
			return redirect('review_index')
		else:
			context = {'error': '아이디나 패스워드를 다시 확인하여주세요.'}
	return render(request, 'account/login.html', context)
	
def logout_view(request):
	logout(request)
	return redirect('login')

def signup_view(request):
	if request.method=="POST":
		user_id = request.POST['username']
		user_email = request.POST['email']
		user_pw1 = request.POST['password1']
		user_pw2 = request.POST['password2']
		if User.objects.filter(username=user_id).exists():
			context = {'error':'이미 존재하는 아이디 입니다'}
			return render(request, 'account/signup.html', context)
		if User.objects.filter(email=user_email).exists():
			context = {'error':'이미 존재하는 이메일 입니다'}
			return render(request, 'account/signup.html', context)
		if user_pw1 != user_pw2:
			context = {'error':'패스워드가 다릅니다'}
			return render(request, 'account/signup.html',context)
		user = User.objects.create_user(user_id, user_email, user_pw1)
		user.save()
		profile = Profile(accuser = user,
						nickname = user.username,
						bio = '초기상태입니다. 변경해주세요.'
			)
		profile.save()
		user = authenticate(username = user_id, password = user_pw1)
		login(request, user)
		return redirect('review_index')
	else:
		return render(request, 'account/signup.html')

def mypage_view(request):
	if not request.user.is_authenticated():
		return redirect('login')
	if request.method=="POST":
		profile = Profile.objects.get(accuser=request.user)
		profile.nickname = request.POST['nickname']
		profile.bio = request.POST['bio']
#이미지 넣는경우
		print(request.FILES)
		if len(request.FILES) != 0:
			profile.profileimg = request.FILES['profileimg']
		profile.save()
		return redirect('mypage')
	else:
		context={'user':request.user,}
		return render(request, 'account/mypage.html', context)


def userpage_view(request, username):
	user = User.objects.get(username=username)
	context = {'user':user,}
	return render(request, 'account/userpage.html', context)


