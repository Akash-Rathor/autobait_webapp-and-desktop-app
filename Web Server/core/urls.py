from django.urls import path, include
from django.contrib.auth import views as auth_views
# from rest_framework import routers
from core import views
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework.routers import Route, DynamicRoute, SimpleRouter,DefaultRouter

# router = CustomReadOnlyRouter()
# router = DefaultRouter()

# router.register(r'', views.TokenViewSet)

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("", views.home, name="home"),
    path('settings/', views.settings,name='settings'),
    path('Create-campaign/<int:val>', views.campaigns,name='campaigns'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)