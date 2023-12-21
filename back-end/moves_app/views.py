from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Move  # Import your Move model

# Create your views here.
class A_move(APIView):
    def get(self, request, name):
        move = Move.objects.get(name = name.title())
        return Response(MoveSerializer(move).data)
class A_move(APIView):
    def get(self, request, name):
        move = Move.objects.get(name = name.title())
        return Response(MoveSerializer(move).data)