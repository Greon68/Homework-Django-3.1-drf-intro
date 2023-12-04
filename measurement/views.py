from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, SensorSerializer, MeasurementSerializer, \
    MeasurementDetailSerializer


class List_SensorView(ListAPIView):
    '''Получаем список всех объектов Sensor (всех датчиков) '''
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class Measurement_View(ListAPIView):
    '''Получаем список всех  измерений '''
    queryset = Measurement.objects.all()
    serializer_class = MeasurementDetailSerializer




# 1.Создать датчик. Указываются название и описание датчика.

class CreateSensorView(CreateAPIView):
    '''Создаём новый объект - датчик '''
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# 2. Изменить датчик. Указываются название и описание.

class UpdateSensorView(UpdateAPIView):
    ''' Изменить объект (датчик). Методы PUT и PATCH'''
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# 3. Добавить измерение. Указываются ID датчика и температура.

class CreateMeasurementView(CreateAPIView):
    ''' Запись нового измерения для конкретного датчика '''
    queryset = Measurement.objects.all()
    serializer_class = MeasurementDetailSerializer

# 4.Получить список датчиков.
# Выдаётся список с краткой информацией по датчикам: ID, название и описание.
class SensorView(ListAPIView):
    '''Получаем список всех датчиков с измерениями '''
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# 5.Получить информацию по конкретному датчику.
# Выдаётся полная информация по датчику: ID, название, описание
# и список всех измерений с температурой и временем.
class SensorRetrieveView(RetrieveAPIView):
    '''Показать информацию по конкретному датчику по его id'''
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer




# Работаю через ViewSet (для себя)
class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer