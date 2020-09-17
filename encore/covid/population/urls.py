from django.urls import path
from population import views


app_name = 'population'
urlpatterns = [
    path('bar-chart', views.main_view1, name='bar-chart'),
    path('bar-chart2', views.main_view2, name='bar-chart2'),
]
