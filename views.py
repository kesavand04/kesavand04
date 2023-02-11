from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
import sqlite3
from pathlib import Path

from .serializers import ngoSerializer,philSerializer,NameSerializer
from .models import NgoDB,philDB
# BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.

class favNgo(APIView):
    def post(self, request, format=None):
        print("Inside viewset")
        ngoNames = ""
        con = sqlite3.connect(r"C:\Varun\Programing\hackathon\newProject\db.sqlite3")
        cur = con.cursor()
        serializer = NameSerializer(data=request.data)
        print("below viewset")
        if serializer.is_valid():
            e = serializer.data.get('cphil')
            print("hellooo")
            areaOfInterest = ""
            for row in cur.execute('SELECT phil_name,phil_interest FROM ngo_phildb;'):
                if e == row[0]:
                    areaOfInterest = row[1]
            print(areaOfInterest + " hello")
            cur1 = con.cursor()
            print("podaa")
            for row in cur1.execute('SELECT ngo_sector,ngo_name FROM ngo_ngodb'):
                print("bye ")
                if row[0] == areaOfInterest:
                    print(row[0])
                    ngoNames = ngoNames + "," + row[1]                
        return Response(ngoNames)
    
def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())


