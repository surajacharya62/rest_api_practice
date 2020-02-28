from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.views.generic import View
from testapp.mixin import HttpResponseMixin
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

class JsonCBV(HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        emp_data =  json.dumps({'msg ':'This is get method'})
        return self.render_to_http_response(emp_data)

    def post(self,request,*args,**kwargs):
        emp_data =  json.dumps({'msg ':'This is post methond'})
        return HttpResponse(emp_data)

    def put(self,request,*args,**kwargs):
        emp_data =  json.dumps({'msg ':'This is put method'})
        return HttpResponse(emp_data)

    def delete(self,request,*args,**kwargs):
        emp_data =  json.dumps({'msg ':'This is delete method'})
        return HttpResponse(emp_data)
