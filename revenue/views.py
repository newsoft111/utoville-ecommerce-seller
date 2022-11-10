from django.shortcuts import render
from .models import *
from django.db.models import Q, Sum
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def revenue_list(request):
	now = date.today()
	start_date = now-relativedelta(months=1)
	end_date = now

	if request.GET.get("start_date"):
		start_date = datetime.strptime(request.GET.get("start_date"), "%Y-%m-%d")
		if request.GET.get("end_date"):
			end_date = request.GET.get("end_date")
		

	revenue_seller_objs = RevenueSeller.objects.filter(seller=request.user, date__range=[start_date, end_date])
	payment_amount = revenue_seller_objs.aggregate(Sum('payment_amount'))['payment_amount__sum']
	refund_amount = revenue_seller_objs.aggregate(Sum('refund_amount'))['refund_amount__sum']
	total_payment = payment_amount-refund_amount


	temp = { po.date: {"payment_amount": po.payment_amount, "refunt_amount": po.payment_amount, "order_count":po.order_count} for po in revenue_seller_objs }


	result = []

	for dy in range(0, (end_date-start_date).days):
		loop_date = (now-timedelta(days=dy))
		result.append({
			'date': loop_date,
			'payment_amount': temp[loop_date]['payment_amount'] if loop_date in temp else 0,
			'refunt_amount': temp[loop_date]['refunt_amount'] if loop_date in temp else 0,
			'order_count': temp[loop_date]['order_count'] if loop_date in temp else 0,
		})

	return render(request, 'revenue/revenue_list.html', {
		"revenue_seller_objs": result,
		'payment_amount': payment_amount,
		'refund_amount': refund_amount,
		'total_payment': total_payment
	})