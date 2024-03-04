from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

prefix_API_v1 = 'api/v1/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(prefix_API_v1, include('core.urls')),
    path(prefix_API_v1, include('movies.urls'))
]
