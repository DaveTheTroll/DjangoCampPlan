from django.urls import path
from . import views

app_name = 'tents'
urlpatterns = [
    path('', views.index, name='index'),
    path('nations', views.nations, name='nations'),
    path('nation/<int:id>', views.nation, name='nation'),
]
