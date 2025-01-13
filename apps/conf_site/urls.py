from django.urls import path

from apps.conf_site.views import (
    ServiceCarouselListAPIView, ServiceListAPIView, PlaceOrderCreateAPIView, SeoDetailsListView, ContactsListView
)

urlpatterns = [
    path('service-carousel/', ServiceCarouselListAPIView.as_view(), name='service-carousel-list'),
    path('services/', ServiceListAPIView.as_view(), name='service-list'),
    path('place-order/', PlaceOrderCreateAPIView.as_view(), name='place-order-create'),
    path('seo-details/', SeoDetailsListView.as_view(), name='seo-details-list'),
    path('contact/', ContactsListView.as_view(), name='contact'),
]
