from django.shortcuts import render
from django.http import HttpResponse,QueryDict,JsonResponse
from django.views.generic import View,TemplateView,DetailView
from . import models 
import json 
from .models import TodosInfo
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import requests
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
# Create your views here.

    
class Indexview(TemplateView):
    print('Hey Vasu')
    template_name = 'first_app/index.html'


class Todos(View):
    def get(self,request):
        # print("Inside GET")
        fetch_url = (request.path)
        fetch_url = fetch_url.split('/')
        print(fetch_url)
        model = models.TodosInfo
        if(fetch_url[3]==''):
            # print("Fetching Parent")
            my_data = serializers.serialize('json',model.objects.all())
            # print(type(my_data))
            my_data = json.loads(my_data)
            my_json = {'message':'OK','payload':my_data}
            response = HttpResponse(json.dumps(my_json),content_type= 'application/json',status = status.HTTP_200_OK)
            response['Access-Control-Allow-Origin'] = '*'
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            return response
        else:
            print("Fetching Child")
            my_data = serializers.serialize('json',model.objects.all().filter(id=fetch_url[3]))
            # print("ID TYPE = ",type(eval(my_data)))
            if(len(my_data)>2): 
                # print("Response Length not 0")
                my_data = json.loads(my_data)
                my_json = {'message':'OK','payload':my_data}
                response = HttpResponse(json.dumps(my_json), content_type = 'application/json',status = status.HTTP_200_OK)
                response['Access-Control-Allow-Origin'] = '*'
                response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
                return response
            else:
                # print("Response Length = 0")
                my_json = {'message':'FAILED'}
                response = HttpResponse(json.dumps(my_json), content_type= 'application/json',status=status.HTTP_404_NOT_FOUND)
                response['Access-Control-Allow-Origin'] = '*'
                response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
                return response
    
    def option(self,request):
        print('there')
        response = HttpResponse("This is Integration")
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        response["Access-Control-Allow-Methods"] = "PUT, DELETE, POST, GET, OPTIONS"
        return response


    @csrf_exempt
    def post(self,request):
        print("Inside POST")
        fetch_url = (request.path)
        fetch_url = fetch_url.split('/')
        # print("Vasu is posting something")
        print(request.body)
        print(type(request.body))
        if(fetch_url[3]==''):
            mydata = json.loads(request.body)
            print(mydata)
            new_todo = models.TodosInfo
            new_todo = models.TodosInfo(title=mydata['title'],completed=False)
            new_todo.save()
            my_id = new_todo.id
            print(my_id)
            my_json = {'status':'OK','payload':{'id':my_id}}
            response = HttpResponse(json.dumps(my_json), content_type = 'application/json',status = status.HTTP_200_OK)
            response['Access-Control-Allow-Origin'] = '*'
            # response.Headers("Access-Control-Allow-Origin":"*")

            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            return response
        else:
            my_json = {'message':'FAILED'}
            response = HttpResponse(json.dumps(my_json), content_type = 'application/json',status = status.HTTP_400_BAD_REQUEST)
            response['Access-Control-Allow-Origin'] = '*'
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            return response


    def delete(self,request):
        print('Inside Delete')
        fetch_url = request.path
        fetch_url = fetch_url.split('/')
        my_id = fetch_url[3]
        if(fetch_url[3]==''):
            print("ID not specified")
            my_json = {'message':'ID_NOT_SPECIFIED'}
            response = HttpResponse(json.dumps(my_json),content_type = 'application/json',status = status.HTTP_400_BAD_REQUEST)
            response['Access-Control-Allow-Origin'] = '*'
            # response.Headers("Access-Control-Allow-Origin":"*")
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            return response
        else:
            my_obj = models.TodosInfo.objects.filter(id=my_id)
            if(len(my_obj)>0):
                new_obj = my_obj[0]
                new_obj.delete()
                my_json = {'id':'1','title':'Todo Deleted','completed':True}
                response = HttpResponse(json.dumps(my_json), content_type = 'application/json',status = status.HTTP_200_OK)
                response['Access-Control-Allow-Origin'] = '*'
                response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
                return response
            else:
                my_json = {'message':'FAILED'}
                response = HttpResponse(json.dumps(my_json), content_type = 'application/json',status = status.HTTP_400_BAD_REQUEST)
                response['Access-Control-Allow-Origin'] = '*'
                response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
                return response

    def put(self,request,*args,**kwargs):
        print('Inside Put')
        my_dict = json.loads(request.body)
        fetch_url = request.path
        fetch_url = fetch_url.split('/')
        my_id = fetch_url[3]
        print(my_id)
        if(my_id==''):
            print("No ID Specified")
            my_json = {'message':'Bad Request'}
            response = HttpResponse(json.dumps(my_json), content_type = 'application/json',status = status.HTTP_400_BAD_REQUEST)
            response['Access-Control-Allow-Origin'] = '*'
            response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
            return response
        else:
            print("ID Specified")
            my_obj = models.TodosInfo.objects.get(id=my_id)
            if(my_obj):
                print("Object Found of given ID")
                for key, value in my_dict.items():
                    setattr(my_obj, key, value)
                my_obj.save()
                my_json = {'message':'Todd Updated','payload':{'id':my_obj.id }}
                response = HttpResponse(json.dumps(my_json), content_type = 'application/json',status = status.HTTP_200_OK)
                response['Access-Control-Allow-Origin'] = '*'
                response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
                return response
            else:
                print("Object Not Found of given ID")
                my_json = {'message':'Invalid DATA'}
                response = HttpResponse(json.dumps(my_json), content_type = 'application/json',status = status.HTTP_400_BAD_REQUEST)
                response['Access-Control-Allow-Origin'] = '*'
                response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
                return response