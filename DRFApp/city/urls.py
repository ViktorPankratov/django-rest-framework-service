from django.urls import path

from .views import *

urlpatterns = [
    path('city/', CityViewSet.as_view()),
    path('city/<int:pk>/', CityDetail.as_view()),
    path('city/create/', CityCreateView.as_view()),
    path('city/<int:city_id>/street/', StreetViewSet.as_view()),
    path('street/create/', StreetCreateView.as_view()),
    path('shop/', ShopViewSet.as_view()),
    path('shop/create/', ShopCreateView.as_view()),
]
