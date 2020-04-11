from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import product
from .serializers import productSerializers

# Create your views here.

class productList(APIView):
    def get(self,request):
        product1=product.objects.all()
        serializer=productSerializers(product1,many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = productSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class productDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, id):
        try:

            return product.objects.get(id=id)
        except product.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        print("hhhhhhhhhhhhhhhh")
        product = self.get_object(id)
        serializer = productSerializers(product)
        return Response(serializer.data)

    def put(self, request, Id, format=None):
        snippet = self.get_object(Id)
        serializer = productSerializers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        print("inside delete method")
        product = self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

