from product.models import *
from django.db.models import Q


def counter_new_qna(request):
	if request.user.is_authenticated: #로그인 상태면
		q = Q()
		q &= Q(product__user = request.user)
		q &= Q(answered_at = None)
		result = ProductQnA.objects.filter(q).count()
	else:
		result = None
	return {'counter_new_qna':  result}