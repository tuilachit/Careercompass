from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CareerPathViewSet, CareerAssessmentViewSet, AssessmentResultViewSet,
    CareerResourceViewSet, UserProfileViewSet
)

# Create router and register viewsets
router = DefaultRouter()
router.register(r'career-paths', CareerPathViewSet, basename='careerpath')
router.register(r'assessments', CareerAssessmentViewSet, basename='assessment')
router.register(r'assessment-results', AssessmentResultViewSet, basename='assessmentresult')
router.register(r'resources', CareerResourceViewSet, basename='resource')
router.register(r'profiles', UserProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
]
