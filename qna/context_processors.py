from product.models import *
from django.db.models import Q


def counter_new_qna(request):
	q = Q()
	q &= Q(product__user = request.user)
	q &= Q(answered_at = None)
	result = ProductQnA.objects.filter(q).count()
	print(result)
	return {'counter_new_qna':  result}