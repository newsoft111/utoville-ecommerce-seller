from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from django.core.paginator import Paginator
from datetime import datetime, timedelta, date
from django.views.generic import View
import pandas as pd
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


class OrderPreview(View):
	def get(self, request):
		self.end_date = datetime.now() + timedelta(1)

		q = Q()
		q &= Q(product__user=request.user)
		if request.POST.get('start_date'):
			self.start_date = datetime.strptime(request.GET.get("start_date"), "%Y-%m-%d")
		else:
			self.start_date = self.end_date - timedelta(days=7)
		q &= Q(order__paid_at__range = [self.start_date, self.end_date])

		order_items = OrderItem.objects.filter(q)

		if request.GET.get('standard') == 'Monthly':
			self.date_format = "%b"
			chart_data = self.monthly()
		else:
			self.date_format = "%a"
			chart_data = self.weekly()
			
		total_price = 0
		for items in order_items:
			chart_data[items.order.paid_at.strftime(self.date_format)] += 1
			total_price += items.sub_total_price()
			
			
		return JsonResponse({
			"chart_data": [{"x": key, "y": value} for key, value in chart_data.items()],
			'count': order_items.count()
		})

	def weekly(self):
		preview_data = {}
		def daterange(start_date, end_date):
			for n in range(int((end_date - start_date).days)):
				yield self.start_date + timedelta(n)

		for single_date in daterange(self.start_date, self.end_date):
			preview_data[single_date.strftime(self.date_format)] = 0
			
		return preview_data

	def monthly(self):
		preview_data = {}
		month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

		for month in month_list:
			preview_data[month] = 0

		return preview_data

