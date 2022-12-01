from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # if url starts with **/api/ request is handled by urls.py of api app
    path('api/', include('api.urls')), 
    # else req is handled from base app's urls.py file 
    path('', include('base.urls')),
    # default django admin page
    path('admin/', admin.site.urls),
]