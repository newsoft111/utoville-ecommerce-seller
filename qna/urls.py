from django.urls import path
from . import views

app_name = 'qna'

urlpatterns = [
	path('', views.qna_list, name='list'),
	path('<int:qna_id>/', views.qna_detail, name='detail'),
	path('delete/', views.qna_delete, name='delete'),
]