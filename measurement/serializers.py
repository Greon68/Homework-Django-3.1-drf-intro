from rest_framework import serializers

from measurement.models import Measurement, Sensor


class SensorSerializer(serializers.ModelSerializer):
    '''Только сенсоры'''
    class Meta:
        model = Sensor
        fields = '__all__'



class MeasurementSerializer(serializers.ModelSerializer):
    '''Измерения без указания id сенсора (для списка сенсоров)'''
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    ''' Сенсор с измерениями '''
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class MeasurementDetailSerializer(serializers.ModelSerializer):
    ''' Измерения с указанием id сенсора (для списка измерений) '''
    class Meta:
        model = Measurement
        # fields = ['temperature', 'created_at','sensor']
        fields = '__all__'