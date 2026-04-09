from django.contrib import admin
from django.urls import path, include
import accounts.views as views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.login_view, name='home'),
]
