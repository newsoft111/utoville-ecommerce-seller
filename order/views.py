from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from django.core.paginator import Paginator
from datetime import datetime, timedelta
# Create your views here.

@login_required(login_url="account:login")
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


@login_required(login_url="account:login")
def order_preview(request):
	order_preview_json = {"order_preview":''}
	order_preview_list = []
	today = datetime.now()

	q = Q()
	q &= Q(product__user=request.user)
	if request.POST.get('start_date'):
		start_date = datetime.strptime(request.GET.get("start_date"), "%Y-%m-%d")
	else:
		start_date = today - timedelta(days=7)
	q &= Q(order__paid_at__range = [start_date, today])

	order_items = OrderItem.objects.filter(q)

	total_price = 0
	for items in order_items:
		total_price += items.sub_total_price()

	order_preview_json['total_price'] = format(total_price, ',')
	return JsonResponse(order_preview_json)