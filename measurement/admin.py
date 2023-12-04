from django.contrib import admin

from measurement.models import Sensor, Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id','name','model']

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    pass
