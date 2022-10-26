from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from django.core.paginator import Paginator
# Create your views here.

@login_required(login_url="acount:login")
def order_list(request):
	seo = {
		'title': "상품 리스트 - 유토빌",
	}
	q = Q()
	q &= Q(product__user = request.user)
	q &= Q(order__is_paid = True)
	order_item_list =  OrderItem.objects.filter(q).order_by( "-id")
	
	page        = int(request.GET.get('p', 1))
	pagenator   = Paginator(order_item_list, 12)
	order_item_list = pagenator.get_page(page)

	return render(request, 'order/order_list.html',{
		"seo":seo,
		'order_item_list': order_item_list
	})
	