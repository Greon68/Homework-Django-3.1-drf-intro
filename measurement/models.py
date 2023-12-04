from django.db import models

class Sensor(models.Model):
    ''' Модель датчиков'''
    name = models.CharField(max_length=100)
    model= models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['id']
        db_table='sensor'
        verbose_name = "Датчик"
        verbose_name_plural = "Датчики"
    def __str__(self):
        return f'{self.name}'

class Measurement(models.Model):
    ''' Модель измерений '''
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=6, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add= True)


    class Meta:
        ordering = ['sensor']
        db_table = 'measurement'
        verbose_name = "Измерение"
        verbose_name_plural = "Измерения"

    def __str__(self):
        return f'{self.sensor.name} : {self.created_at}'



