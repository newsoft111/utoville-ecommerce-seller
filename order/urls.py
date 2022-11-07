from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
	path('', views.order_list, name='list'),
	path('preview/', views.OrderPreview.as_view(), name='preview'),
	path('edit/status/', views.order_edit_status, name='edit_status'),
]
