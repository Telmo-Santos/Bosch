from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Driver


# Create your views here.
def index(request):
    latest_driver_list = Driver.objects.order_by('name_text')

    # context is here so that we can access variables in html
    context = {
        'latest_driver_list': latest_driver_list,
    }
    return render(request, 'BoschWebsite/index.html', context)


# return HttpResponse("Hello World. You´re at the BoschWebsite index.")


# Details about Driver are shown here
# If Driver does not exist, Exception is thrown
def driverdetail(request, driver_id):
    driver = get_object_or_404(Driver, pk=driver_id)
    return render(request, 'BoschWebsite/driverdetail.html', {'driver': driver})


# From tutorial
def results(request, driver_id):
    response = "You´re looking at the response of Driver %s."
    return HttpResponse(response % driver_id)


# From tutorial
def vote(request, driver_id):
    return HttpResponse("You´re voting on Driver %s." % driver_id)
