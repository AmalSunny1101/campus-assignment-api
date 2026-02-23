from rest_framework import serializers
from .models import Student, Assignment
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = ['username', 'email', 'password', 'department', 'year']

    def create(self, validated_data):
        user = Student.objects.create_user(**validated_data)
        return user


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'
        read_only_fields = ['student', 'created_at']