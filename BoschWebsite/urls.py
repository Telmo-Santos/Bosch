from django.urls import path
from . import views

app_name = 'BoschWebsite'
urlpatterns = [
    # /BoschWebsite/
    path('', views.index, name='index'),
    # /BoschWebsite/2/
    path('<int:pk>/', views.DriverDetail.as_view(), name='driverdetail'),
    # /BoschWebsite/2/Team/
    path('<int:pk>/Team/', views.TeamDetail.as_view(), name='teamdetail'),
    # /BoschWebsite/2/Track/
    path('<int:pk>/Track/', views.TrackDetail.as_view(), name='track'),
]
