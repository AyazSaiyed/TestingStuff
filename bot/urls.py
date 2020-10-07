from django.conf.urls import url
from . import views

urlpatterns = [
    url('',views.index_function,name="index_function"),
    # url(r'^demo/',views.temp,name="temp")
]