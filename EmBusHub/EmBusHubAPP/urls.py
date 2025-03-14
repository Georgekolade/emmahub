from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('stock', views.Product, name='product'),
    path('stock/<int:id>', views.ProductDetail, name='detail'),
    path('login', views.Login, name='login'),
    path('register', views.SignUp, name='register'),
    path('logout', views.Logout, name='logout')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)