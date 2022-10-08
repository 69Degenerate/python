
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_view/',include("admin_view.urls")),
    path('',include('std_view.urls')),
]
