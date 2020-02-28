from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.views.generic import View

# Create your views here.

def emp_data_view(request):
    emp_data = {
    'eno': 100,
    'ename':'Suraj Acharya',
    'esal':1000,
    'eaddr':"Taulihawa"
    }
    resp = '<h1>Employee Number:{}</br> Employee Name:{}</br> Employee Salary:{}</br> Employe Address:{}</br></h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
    return HttpResponse(resp)


def emp_data_jasonview(request):
    emp_data = {
    'eno': 100,
    'ename':'Suraj Acharya',
    'esal':1000,
    'eaddr':"Taulihawa"
    }
    emp_data_jason = json.dumps(emp_data)
    return HttpResponse(emp_data_jason, content_type='application/json')

class JsonCBV(View):
    def get(self,request,*args,**kwargs):
        emp_data = {
        'eno': 100,
        'ename':'Suraj Acharya',
        'esal':1000,
        'eaddr':"Taulihawa"
        }

        return JsonResponse(emp_data)
