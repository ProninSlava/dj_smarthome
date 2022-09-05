from django.urls import path

from measurement.views import ListCreateView, SensUpdateView, SensView, MeasurementCreateView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('listsens/', ListCreateView.as_view()),
    path('sensup/<int:pk>/', SensUpdateView.as_view()),
    path('tempset/', MeasurementCreateView.as_view()),
    path('sens/<int:pk>/', SensView.as_view()),

]
