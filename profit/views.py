from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import json, re

def profit_list(request):
	profit_objs = Profit.objects.filter(seller=request.user)
	profit_amount = profit_objs.aggregate(Sum('profit_amount'))['profit_amount__sum']
	if profit_amount is None:
		profit_amount = 0

	now = date.today()
	start_date = now-relativedelta(months=1)
	end_date = now

	if request.GET.get("start_date") is not None and request.GET.get("start_date") != '':
		start_date = datetime.strptime(request.GET.get("start_date"), "%Y-%m-%d")

	if request.GET.get("end_date") is not None and request.GET.get("end_date") != '':
		end_date = datetime.strptime(request.GET.get("end_date"), "%Y-%m-%d")

	start_date = start_date + timedelta(days=1)

	profit_done_objs = ProfitDone.objects.filter(seller=request.user, created_at__range=[start_date, end_date])

	page        = int(request.GET.get('p', 1))
	pagenator   = Paginator(profit_done_objs, 10)
	profit_done_objs = pagenator.get_page(page)

	return render(request, 'profit/profit_list.html', {
		"profit_objs": profit_objs,
		'profit_amount': profit_amount,
		'profit_done_objs': profit_done_objs
	})