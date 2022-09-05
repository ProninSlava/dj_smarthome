from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=50)

    # def __str__(self):
    #     return self.name


class Measurement(models.Model):
    sensor_id = models.ForeignKey('Sensor', on_delete=models.CASCADE, related_name='measurements')
    temp = models.FloatField()
    date = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return self.sensor_id


