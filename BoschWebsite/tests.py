from django.urls import reverse
from django.test import TestCase

from .models import Driver, Team, Track


# Create your tests here.
def create_driver(name_text, team, age, wins, poles, titles, start_date, driver_image):
    return Driver.objects.create(name_text=name_text, team=team, age=age, wins=wins, poles=poles, titles=titles,
                                 start_date=start_date, driver_image=driver_image)


def create_team(name_text, symbol, wins, poles, titles, titles_drivers, titles_constructors, boss, start_date,
                boss_image):
    return Team.objects.create(name_text=name_text, symbol=symbol, wins=wins, poles=poles, titles=titles,
                               titles_drivers=titles_drivers, titles_constructors=titles_constructors, boss=boss,
                               start_date=start_date, boss_image=boss_image)


def create_track(name_text, laps, lapRecord, sector1, sector2, sector3, length, layout):
    return Track.objects.create(name_text=name_text, laps=laps, lapRecord=lapRecord, sector1=sector1, sector2=sector2,
                                sector3=sector3,
                                length=length, layout=layout)


class DriverIndexViewTest(TestCase):

    # Testing if 'No Driver available' is returned when driver does not exist
    def test_no_driver(self):
        response = self.client.get(reverse('BoschWebsite:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Driver available")
        self.assertQuerysetEqual(response.context['latest_driver_list'], [])

    # Testing if 'No Team available' is returned when team does not exist
    def test_no_team(self):
        response = self.client.get(reverse('BoschWebsite:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Team available")
        self.assertQuerysetEqual(response.context['latest_team_list'], [])

    # Testing if 'No Track available' is returned when track does not exist
    def test_no_track(self):
        response = self.client.get(reverse('BoschWebsite:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Track available")
        self.assertQuerysetEqual(response.context['latest_track_list'], [])


class TeamIndexViewTest(TestCase):

    # Testing if 'No Driver available' is returned when driver does not exist
    def test_no_driver(self):
        response = self.client.get(reverse('BoschWebsite:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Driver available")
        self.assertQuerysetEqual(response.context['latest_driver_list'], [])

    # Testing if 'No Team available' is returned when team does not exist
    def test_no_team(self):
        response = self.client.get(reverse('BoschWebsite:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Team available")
        self.assertQuerysetEqual(response.context['latest_team_list'], [])

    # Testing if 'No Track available' is returned when track does not exist
    def test_no_track(self):
        response = self.client.get(reverse('BoschWebsite:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Track available")
        self.assertQuerysetEqual(response.context['latest_track_list'], [])


class TrackIndexViewTest(TestCase):
    # Testing if 'No Driver available' is returned when driver does not exist
    def test_no_driver(self):
        response = self.client.get(reverse('BoschWebsite:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Driver available")
        self.assertQuerysetEqual(response.context['latest_driver_list'], [])

    # Testing if 'No Team available' is returned when team does not exist
    def test_no_team(self):
        response = self.client.get(reverse('BoschWebsite:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Team available")
        self.assertQuerysetEqual(response.context['latest_team_list'], [])

    # Testing if 'No Track available' is returned when track does not exist
    def test_no_track(self):
        response = self.client.get(reverse('BoschWebsite:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Track available")
        self.assertQuerysetEqual(response.context['latest_track_list'], [])


class OverviewIndexViewTest(TestCase):

    # Testing if 'No Driver available' is returned when driver does not exist
    def test_no_driver(self):
        response = self.client.get(reverse('BoschWebsite:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Driver available")
        self.assertQuerysetEqual(response.context['latest_driver_list'], [])

    # Testing if 'No Team available' is returned when team does not exist
    def test_no_team(self):
        response = self.client.get(reverse('BoschWebsite:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Team available")
        self.assertQuerysetEqual(response.context['latest_team_list'], [])

    # Testing if 'No Track available' is returned when track does not exist
    def test_no_track(self):
        response = self.client.get(reverse('BoschWebsite:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Track available")
        self.assertQuerysetEqual(response.context['latest_track_list'], [])
