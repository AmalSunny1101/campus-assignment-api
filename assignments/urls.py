from django.urls import path
from .views import RegisterView, AssignmentListCreate, AssignmentDetail
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('assignments/', AssignmentListCreate.as_view()),
    path('assignments/<int:pk>/', AssignmentDetail.as_view()),
]