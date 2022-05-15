from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Team, Driver, Track


# Create your views here.
def index(request):
    # Here we are ordering the drivers by their team
    latest_driver_list = Driver.objects.order_by('team')
    # Ordering Teams by number of wins (descending)
    latest_team_list = Team.objects.order_by('-wins')
    # Ordering Tracks by their schedule in 2021
    latest_track_list = Track.objects.order_by('id')

    # context is here so that we can access variables in html
    context = {
        'latest_driver_list': latest_driver_list,
        'latest_team_list': latest_team_list,
        'latest_track_list': latest_track_list,
    }
    return render(request, 'BoschWebsite/index.html')


# Details about the Drivers are shown here
class IndexDetail(generic.DetailView):
    template_name = 'BoschWebsite/index.html'


# Details about the Drivers are shown here
class DriverDetail(generic.DetailView):
    model = Driver
    template_name = 'BoschWebsite/driverdetail.html'


# Details about the Teams are shown here
class TeamDetail(generic.DetailView):
    model = Team
    template_name = 'BoschWebsite/teamdetail.html'


# Details about the Tracks are shown here
class TrackDetail(generic.DetailView):
    model = Track
    template_name = 'BoschWebsite/track.html'


# Static file needed for css to work
def css(request):
    return render(request, 'BoschWebsite/index.html')
