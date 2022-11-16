from .models import *
from django.db.models import Q


def counter_new_order(request):
	q = Q()
	q &= Q(is_responded=False)
	q &= Q(product__user = request.user)
	q &= Q(order__payment__is_paid = True)
	result = OrderItem.objects.filter(q).count()
	print(result)
	return {'counter_new_order':  result}