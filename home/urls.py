from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name='home'),
    path('predict_insurance', views.predict_insurance, name='predict_insurance'),
    path('', views.index, name='index')
]