from django.urls import path
from rest_framework.routers import DefaultRouter

from measurement.views import SensorViewSet, List_SensorView, CreateSensorView, UpdateSensorView, Measurement_View, \
    CreateMeasurementView, SensorView, SensorRetrieveView

# r= DefaultRouter()
# r.register('sensors',SensorViewSet)

urlpatterns = [
    path('sensor/',List_SensorView.as_view()),
    path('sensor/create/',CreateSensorView.as_view()),
    path('sensor/update/<int:pk>/',UpdateSensorView.as_view()),
    path('measurements/',Measurement_View.as_view()),
    path('measurements/create/',CreateMeasurementView.as_view()),
    path('sensor/full_list/', SensorView.as_view()),
    path('sensor/<int:pk>/', SensorRetrieveView.as_view()),


]
# urlpatterns = r.urls