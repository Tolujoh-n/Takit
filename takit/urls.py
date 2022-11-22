from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import(
    products,
    checkout,
    HomeView
)

app_name = 'takit'

#URLconfig
urlpatterns = [
    path('', HomeView, name='home'),
    path('checkout/' checkout, name='checkout'),
    path('product/' products, name='products')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)