from django.urls import path
from .views import SpatialDataAPI,SpatialQueryAPI,NonSpatialQueryAPI

urlpatterns = [
    path('crud/', SpatialDataAPI.as_view()),
    path('crud/<str:pk>', SpatialDataAPI.as_view()), # to capture our ids
    path('spa/', SpatialQueryAPI.as_view()),
    path('nspa/<str:pk>', NonSpatialQueryAPI.as_view())
]