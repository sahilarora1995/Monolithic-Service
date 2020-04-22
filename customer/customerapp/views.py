from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import customer
from .serializers import customerSerializers,customerpatchSerializers
from rest_framework.parsers import JSONParser
import requests
import json
from django.http import JsonResponse
# Create your views here.
class customerList(APIView):
    def get(self,request):
        customer1=customer.objects.all()
        serializer=customerSerializers(customer1,many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = customerSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class customerDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, id):
        try:
            return customer.objects.get(id=id)
        except customer.DoesNotExist:
            raise Http404

    def patch(self, request, id):
        print("patch method")
        customer = self.get_object(id)
        print("got data.............")
        serializer = customerSerializers(customer, data=request.data,
                                         partial=True)  # set partial=True to update a data partially
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, id, format=None):
        customer = self.get_object(id)
        prod={}
        p={}
        regitsp={}
        i=0
        l=[]
        print(customer.cart[0])
        for x in customer.cart:
            r = requests.get('http://localhost:8080/product/'+ x + '/', auth=('sahilp', '9555497667sS$'))
            prod={}
            prod["ProductName"]= json.loads(r.text)["productname"]
            prod["ProductId"] = json.loads(r.text)["id"]
            l.append(prod)
            p[i]=prod
            i=i+1
        serializer = customerSerializers(customer)
        resp["customer"]=serializer.data
        resp["customersProductDetails"]= p
        return Response(l)

    def put(self, request, Id, format=None):
        snippet = self.get_object(Id)
        serializer = customerSerializers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        print("inside delete method")
        customer = self.get_object(id)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)