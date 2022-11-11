from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'takit'

#URLconfig
urlpatterns = [
    path('', views.item_list, name='item_list')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)