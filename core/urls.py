from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('scan/',views.network_scan_view,name="scan"),
    path('about/',views.about,name="about"),
]
