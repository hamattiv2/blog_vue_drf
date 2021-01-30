from django.shortcuts import render
from rest_framework import status, viewsets, filters, views
from rest_framework import permissions
from rest_framework.response import Response

class GetTestAPI(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        return Response(data={'status': 'Hello World!'}, status=status.HTTP_200_OK)