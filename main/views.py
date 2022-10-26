from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	seo = {
		'title': "유토빌",
	}
	if request.user.is_authenticated: #로그인 상태면
		return render(request, 'main/index.html',{"seo":seo})
	else:
		return redirect("account:login")