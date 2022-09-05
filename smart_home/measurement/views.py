# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer,  SensorDetailSerializer


# Создать датчик. Указываются название и описание датчика.
# Получить список датчиков.
class ListCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# Изменить датчик. Указываются название и/или описание.
class SensUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# Добавить измерение. Указываются ID датчика и температура.
class MeasurementCreateView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


# Получить информацию по конкретному датчику.
class SensView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer



