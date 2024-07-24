'''
App-level URLs
'''
from django.urls import path
from .views import views 
# For css and js
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from .forms import *

# URL Configuration
urlpatterns = [
    # path('example/', views.example, name='example'),
    path('', views.index, name='index'),
    # path('login/', views.login_view, name='login'),
]

# if CSS and JS hosted from cloud server, prefix below line with "if settings.DEBUG:"
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
