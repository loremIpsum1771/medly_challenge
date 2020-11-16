from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound,bad_request
import json
import requests


class CountriesView(APIView):
    '''Returns data for countries
    '''
    def get(self, request):
        rc_api = "https://restcountries.eu/rest/v2/all"
        response_data = requests.get(rc_api).json()

        if 'status' in response_data and response_data['status'] == 404:
            raise NotFound(detail="There are no countries in the system", code=response_data['status'])
        elif 'status' in response_data and response_data['status'] != 404:
            return HttpResponse(response_data['message'], status=response_data['status'])
            
        data = [{"name": res['name'], "capital": res['capital'], "alpha2Code": res['alpha2Code'], "alpha3Code": res['alpha3Code'], "flag": res['flag']} for res in response_data]
        return Response(data=data)

class CountryView(APIView):
    '''Returns data for single country based on passed in country code
    '''
    def get(self, request, code):
        rc_api = "https://restcountries.eu/rest/v2/alpha/" + code
        response_data = requests.get(rc_api).json()

        if 'status' in response_data and response_data['status'] == 404:
            raise NotFound(detail="That country is not in the system", code=response_data['status'])
        elif 'status' in response_data and response_data['status'] == 400:
            raise NotFound(detail="Country codes should be between 2-3 characters", code=response_data['status'])
        elif 'status' in response_data and response_data['status'] != 404:
            return HttpResponse(response_data['message'], status=response_data['status'])

        data = {"name": response_data['name'], "capital": response_data['capital'], "alpha2Code": response_data['alpha2Code'], "alpha3Code": response_data['alpha3Code'], "flag": response_data['flag']}        
        return Response(data=data)

class FlagView(APIView):
    '''Returns flag for single country based on passed in country code
    '''
    def get(self, request, code):
        rc_api = "https://restcountries.eu/rest/v2/alpha/" + code
        response_data = requests.get(rc_api).json()

        if 'status' in response_data and response_data['status'] == 404:
            raise NotFound(detail="That country's flag is not in the system", code=response_data['status'])
        elif 'status' in response_data and response_data['status'] == 400:
            raise NotFound(detail="Country codes should be between 2-3 characters", code=response_data['status'])
        elif 'status' in response_data and response_data['status'] != 404:
            return HttpResponse(response_data['message'], status=response_data['status'])

        flag_data = {"flag":response_data["flag"]}
        return Response(data=flag_data)

