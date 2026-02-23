from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .serializers import RegisterSerializer, AssignmentSerializer
from .models import Assignment
from rest_framework.response import Response
from rest_framework.views import APIView


# Register API
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


# Assignment CRUD
class AssignmentListCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        assignments = Assignment.objects.filter(student=request.user)
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(student=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AssignmentDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, user, pk):
        return Assignment.objects.get(pk=pk, student=user)

    def put(self, request, pk):
        assignment = self.get_object(request.user, pk)
        serializer = AssignmentSerializer(
            assignment, data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        assignment = self.get_object(request.user, pk)
        assignment.delete()
        return Response(status=204)