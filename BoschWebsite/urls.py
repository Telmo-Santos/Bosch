from django.urls import path
from . import views

app_name = 'BoschWebsite'
urlpatterns = [
    # /BoschWebsite/
    path('', views.index, name='index'),
    # /BoschWebsite/2/
    path('<int:driver_id>/', views.driverdetail, name='driverdetail'),
    # /BoschWebsite/2/results/
    path('<int:driver_id>/results/', views.results, name='results'),
    # /BoschWebsite/2/vote/
    path('<int:driver_id>/vote/', views.vote, name='vote'),

    # path('<int: team_id>', views.detail, name='detail'),
    # path('<int: track_id>', views.detail, name='detail'),
]
