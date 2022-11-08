from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from django.core.paginator import Paginator
from datetime import datetime, timedelta, date
from django.views.generic import View
import pandas as pd
import json
# Create your views here.

@login_required(login_url="account:login")
def order_list(request):
	seo = {
		'title': "상품 리스트 - 유토빌",
	}
	q = Q()
	q &= Q(product__user = request.user)
	q &= Q(order__payment__is_paid = True)
	order_item_list =  OrderItem.objects.filter(q).order_by( "-id")
	
	page        = int(request.GET.get('p', 1))
	pagenator   = Paginator(order_item_list, 12)
	order_item_list = pagenator.get_page(page)

	return render(request, 'order/order_list.html',{
		"seo":seo,
		'order_item_list': order_item_list
	})

def order_edit_status(request):
	jsonData = json.loads(request.body)
	event_type  = jsonData.get('event_type')
	order_item_id = jsonData.get('order_item_id')

	if event_type == '' or event_type is None:
		return JsonResponse({
			'result': '201',
			'result_text': '유형을 선택해주세요.'
		})

	print(order_item_id)
	print(1)
	order_item_objs = OrderItem.objects.filter(pk__in=order_item_id)
	print(2)

	
	if event_type == '배달완료':
		order_item_objs.update(
			is_delivered = True, 
			delivered_at = datetime.now()
		)
		return JsonResponse({
			'result': '200',
			'result_text': '수정이 완료되었습니다.'
		})

	elif event_type == '주문취소':
		order_item_objs.update(
			is_refund_requested = True, 
			refund_requested_at = datetime.now()
		)
		return JsonResponse({
			'result': '200',
			'result_text': '수정이 완료되었습니다.'
		})

	elif event_type == '주문접수':
		order_item_objs.update(
			is_accepted = True, 
			accepted_at = datetime.now()
		)
		return JsonResponse({
			'result': '200',
			'result_text': '접수가 완료되었습니다.'
		})

	
	else:
		return JsonResponse({
			'result': '201',
			'result_text': '알수 없는 오류입니다. 다시시도 해주세요.'
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

