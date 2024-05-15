from django.urls import  path

from malling import views


app_name='malling'

urlpatterns = [
    path(' ',views.malling, name='index'),

]