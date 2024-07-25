from django.urls import path

from apps.common import views

app_name = 'common'

urlpatterns = [
    path('', views.index, name='index'),
]
