from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
	context = {}
	if request.method=="POST":
		user_id = request.POST['user_name']
		user_pw = request.POST['password']
		user = authenticate(username = userid, password = userpw)
		if user is not None:
			login(request, user)
			return redirect('/review')
		else:
			context = {'check': '아이디나 패스워드가 틀렸습니다'}
	else:
		context = {'check': '아이디와 패스워드를 입력하세요'}
	return render(request, 'loginpage.html', context)
	
def logout_view(request):
	logout(request)
	return redirect('/account/loginview/')

def signup_view(request):
	if request.method=="POST":
		user_id = request.POST['create_id']
		user_email = request.POST['create_email']
		user_pw1 = request.POST['password1']
		user_pw2 = request.POST['password2']
		if User.objects.filter(username=user_id).exists():
			context = {'error':'이미 존재하는 아이디 입니다'}
			return render(request, 'signuppage.html', context)
		if User.objects.filter(email=usere_mail).exists():
			context = {'error':'이미 존재하는 이메일 입니다'}
			return render(request, 'signuppage.html', context)
		if user_pw1 != user_pw2:
			context = {'error':'패스워드가 다릅니다'}
			return render(request, 'signuppage.html',context)

		user = User.objects.create_user(user_id, usere_mail, user_pw1)
		user.save()
		user = authenticate(username = user_id, password = user_pw1)
		login(request, user)
		return redirect('/review')
	else:
		return render(request, 'signuppage.html')
	