from django.urls import path

from measurement.views import ListCreateView, SensUpdateView, TempCreateView, SensView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('listsens/', ListCreateView.as_view()),
    path('sensup/<int:pk>/', SensUpdateView.as_view()),
    path('sensset/<int:pk>/', TempCreateView.as_view()),
    path('sens/<int:pk>/', SensView.as_view()),

]
