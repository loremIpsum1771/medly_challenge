from django.test import TestCase,Client
from django.urls import reverse
from rest_framework.test import RequestsClient
from rest_framework import status
import requests

class GetAllCountriesTest(TestCase):
    """ Test class for GET all countries API """

    def test_get_all_countries(self):
        client = Client()
        response = client.get(
            reverse('countries'))
        
        self.assertEqual(len(response.data), 250)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleCountryTest(TestCase):
    """ Test class for GET single country API """
    def test_get_valid_alpha2_code(self):
        client = Client()
        response = client.get(
            reverse('country', kwargs={'code': 'co'}))

        rc_api = "https://restcountries.eu/rest/v2/alpha/co" 
        response_data = requests.get(rc_api).json()
        test_data = {"name": response_data['name'], "capital": response_data['capital'], "alpha2Code": response_data['alpha2Code'], "alpha3Code": response_data['alpha3Code'], "flag": response_data['flag']}        

        self.assertEqual(response.data, test_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_valid_alpha3_code(self):
        client = Client()
        response = client.get(
            reverse('country', kwargs={'code': 'col'}))

        rc_api = "https://restcountries.eu/rest/v2/alpha/col" 
        response_data = requests.get(rc_api).json()
        test_data = {"name": response_data['name'], "capital": response_data['capital'], "alpha2Code": response_data['alpha2Code'], "alpha3Code": response_data['alpha3Code'], "flag": response_data['flag']}        

        self.assertEqual(response.data, test_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_long_country_code(self):
        client = Client()
        response = client.get(
            reverse('country', kwargs={'code': 'cold'}))


        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_get_invalid_nonexistent_country_code(self):
        client = Client()
        response = client.get(
            reverse('country', kwargs={'code': 'aa'}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class GetSingleFlagTest(TestCase):
    """ Test class for GET a single country's flag API """
    def test_get_valid_alpha2_code(self):
        client = Client()
        response = client.get(
            reverse('flag', kwargs={'code': 'co'}))

        rc_api = "https://restcountries.eu/rest/v2/alpha/co" 
        response_data = requests.get(rc_api).json()
        flag_data = {"flag":response_data["flag"]}

        self.assertEqual(response.data, flag_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_valid_alpha3_code(self):
        client = Client()
        response = client.get(
            reverse('flag', kwargs={'code': 'col'}))

        rc_api = "https://restcountries.eu/rest/v2/alpha/col" 
        response_data = requests.get(rc_api).json()
        flag_data = {"flag":response_data["flag"]}

        self.assertEqual(response.data, flag_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_long_country_code(self):
        client = Client()
        response = client.get(
            reverse('flag', kwargs={'code': 'cold'}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_get_invalid_nonexistent_country_code(self):
        client = Client()
        response = client.get(
            reverse('flag', kwargs={'code': 'aa'}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)