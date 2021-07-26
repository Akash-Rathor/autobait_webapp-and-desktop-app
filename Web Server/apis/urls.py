from django.urls import path, include
from apis import views

urlpatterns = [
    path('GetLinkedinCredentials/', views.GetLinkedinCredentials,name='GetLinkedinCredentials'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]