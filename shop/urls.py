from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import handler404, handler500
from .views import custom_404, custom_500

handler404 = custom_404
handler500 = custom_500

urlpatterns = [
    path("", views.home, name="Home"),
    path("checkout", views.checkout, name="Checkout"),
    path("order", views.orders, name="orders"),
    path("s", views.search, name="Search"),
    path("preorder/<str:queryRes>", views.preorder, name="preorder"),
    path("p/<str:id>", views.details, name="Details"),
    path("preorders/<int:id>", views.preorderdetails, name="preorderdetails"),
    path("order/<int:id>", views.orderdetails, name="orderdetails"),
    path('??add_to_cart/<str:id>/', views.add_to_cart, name='add_to_cart'),
    path("about", views.about, name="About"),
    path("tracker/", views.tracker, name="tracker"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

