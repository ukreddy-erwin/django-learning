from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """"Test API VIew"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """"Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to a traditional django view',
            'Gives us most control over you application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello','an_apiview': an_apiview})

    # http://url/api/hello-view  a name text field available with post button
    def post(self,request):
        """"Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data) ##to retrieve the stanadard serializer class created: serializer_class

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """"Handle updating an object"""
        return Response({'method':'PUT'})

    #using raw data instead of html form in api page
    def patch(self,request,pk=None):
        """"Handle a partial updating of an object like only last name,etc"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """"Handle deleting an object"""
        return Response({'method':'DELETE'})