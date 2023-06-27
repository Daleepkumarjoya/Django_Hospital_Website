
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
admin.site.site_header = "DK Hospital Admin"
admin.site.site_title = "DK Hospital Admin Panel"
admin.site.index_title = "Welcome to DK Hospital Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("HospitalManagement.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
