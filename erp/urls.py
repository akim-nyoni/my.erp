from django.contrib import admin
from django.urls import path, include
import accounts.views as views
import dashboard.views as views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', views.dashboard, name='home'),
]
