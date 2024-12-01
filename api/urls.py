from django.urls import path
from .views import VehicleList, VehicleDetail, LocationList, LocationDetail

urlpatterns = [
    path('vehicle/', VehicleList.as_view()),
    path('vehicle/<int:pk>/', VehicleDetail.as_view()),
    path('locations/', LocationList.as_view()),
    path('locations/<int:pk>/', LocationDetail.as_view())
]
