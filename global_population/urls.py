from django.urls import path
from .views import GetPopulationView


urlpatterns = [
    path('get_population/', GetPopulationView.as_view(), name='get_population')
]
