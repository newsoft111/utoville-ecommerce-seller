from django.contrib import admin
from django.urls import path, include       #new
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('main.urls')),
	path('account/', include('account.urls')),
	path('order/', include('order.urls')),
	path('qna/', include('qna.urls')),
	path('revenue/', include('revenue.urls')),
	path('profit/', include('profit.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)