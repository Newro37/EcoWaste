

from django.contrib import admin
from django.urls import path, include
from waste_management import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('reports/', include('reports.urls')),
]
