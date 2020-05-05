"""boardgamebro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
import rest_framework
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from bgb_app import api_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# API Swagger
schema_view = get_schema_view(
    openapi.Info(title='BoardgameBro API', default_version='v1'),
    public=True,
    permission_classes=(rest_framework.permissions.AllowAny, ),
)

# Default API
router = routers.DefaultRouter()
router.register('games', api_views.GameViewSet)
router.register('plays', api_views.PlayViewSet)
router.register('players', api_views.PlayerViewSet)
router.register('scores', api_views.ScoreViewSet)

urlpatterns = [
    # APP
    path('', include('bgb_app.urls'), name='bgb'),
    # ACCOUNT
    path('accounts/login', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/social/', include('social_django.urls'), name='social'),
    # ADMIN
    path('admin/', admin.site.urls),
    # API
    path('api/', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework')),
    path('api-docs/', include_docs_urls()),
]

apipatterns = [
    # API
    path('api/', include(router.urls), name='api'),
    # API DOCS
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework'),
        name='api-auth'),
    path('api-docs/', include_docs_urls(), name='api-docs'),
    path(
        'api-swagger{format}.json/',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    path(
        'api-docs-swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    path(
        'api-docs-redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc-ui'),
]

urlpatterns = urlpatterns + apipatterns

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
