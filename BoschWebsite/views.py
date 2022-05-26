from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Team, Driver, Track


# Create your views here.
def index(request):
    return render(request, 'BoschWebsite/index.html')


# Create your views here.
def overview(request):
    return render(request, 'BoschWebsite/overview.html')


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
