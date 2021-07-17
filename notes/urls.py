from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # API paths
    path('', include('api.urls')),
    path('api/', include('rest_framework.urls'))
]
