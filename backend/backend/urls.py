from django.urls import path, include
from django.contrib import admin
from django.urls import path


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('blog/', include('blog.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]