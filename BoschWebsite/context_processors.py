from .models import Driver, Team, Track


def extras(request):
    # Here we are ordering the drivers by their team
    latest_driver_list = Driver.objects.order_by('team')
    # Ordering Teams by number of wins (descending)
    latest_team_list = Team.objects.order_by('-wins')
    # Ordering Tracks by their schedule in 2021
    latest_track_list = Track.objects.order_by('id')
    return {'latest_driver_list': latest_driver_list,
            'latest_team_list': latest_team_list,
            'latest_track_list': latest_track_list, }
