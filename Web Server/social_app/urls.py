
# social_app/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', include('core.urls')),
    path('api/', include('apis.urls')),
]