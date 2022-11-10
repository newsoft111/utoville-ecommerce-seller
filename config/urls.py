from django.contrib import admin
from django.urls import path, include       #new

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('main.urls')),
	path('account/', include('account.urls')),
	path('order/', include('order.urls')),
	path('qna/', include('qna.urls')),
	path('revenue/', include('revenue.urls')),
]