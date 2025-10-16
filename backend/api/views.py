from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import CareerPath, CareerAssessment, AssessmentResult, CareerResource, UserProfile
from .serializers import (
    CareerPathSerializer, CareerAssessmentSerializer, AssessmentResultSerializer,
    CareerResourceSerializer, UserProfileSerializer, AssessmentSubmissionSerializer,
    CareerRecommendationSerializer
)


class CareerPathViewSet(viewsets.ModelViewSet):
    """ViewSet for Career Path operations"""
    queryset = CareerPath.objects.filter(is_active=True)
    serializer_class = CareerPathSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'education_level', 'growth_outlook', 'work_environment']
    search_fields = ['title', 'description', 'required_skills']
    ordering_fields = ['title', 'created_at', 'salary_range_min']
    ordering = ['title']

    @action(detail=False, methods=['get'])
    def categories(self, request):
        """Get all available career categories"""
        categories = CareerPath.objects.filter(is_active=True).values_list('category', flat=True).distinct()
        return Response(list(categories))

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured career paths"""
        featured_paths = self.get_queryset().order_by('?')[:6]  # Random 6 featured paths
        serializer = self.get_serializer(featured_paths, many=True)
        return Response(serializer.data)


class CareerAssessmentViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for Career Assessment operations (read-only)"""
    queryset = CareerAssessment.objects.filter(is_active=True)
    serializer_class = CareerAssessmentSerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=['post'])
    def submit(self, request, pk=None):
        """Submit assessment answers and get recommendations"""
        assessment = self.get_object()
        serializer = AssessmentSubmissionSerializer(data=request.data)
        
        if serializer.is_valid():
            # Create assessment result
            result_data = {
                'assessment': assessment,
                'answers': serializer.validated_data['answers'],
                'session_id': serializer.validated_data.get('session_id'),
            }
            
            # Add user if authenticated
            if request.user.is_authenticated:
                result_data['user'] = request.user
            
            result = AssessmentResult.objects.create(**result_data)
            
            # Generate recommendations (simplified logic)
            recommendations = self.generate_recommendations(assessment, serializer.validated_data['answers'])
            result.recommended_careers = [r['id'] for r in recommendations]
            result.save()
            
            response_serializer = AssessmentResultSerializer(result)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def generate_recommendations(self, assessment, answers):
        """Generate career recommendations based on answers (simplified logic)"""
        # This is a simplified recommendation engine
        # In a real application, you'd have more sophisticated logic
        
        # Get all career paths
        career_paths = CareerPath.objects.filter(is_active=True)
        
        # Simple scoring based on answers (this would be more complex in reality)
        scored_careers = []
        for career in career_paths:
            score = 0
            
            # Example scoring logic based on answer patterns
            # You'd implement more sophisticated matching here
            if len(answers) > 0:
                score = len([a for a in answers if 'technology' in str(a).lower()]) * 2
            
            scored_careers.append({
                'id': career.id,
                'title': career.title,
                'score': score,
                'category': career.category
            })
        
        # Sort by score and return top recommendations
        scored_careers.sort(key=lambda x: x['score'], reverse=True)
        return scored_careers[:5]


class AssessmentResultViewSet(viewsets.ModelViewSet):
    """ViewSet for Assessment Result operations"""
    serializer_class = AssessmentResultSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        """Filter results based on user authentication"""
        if self.request.user.is_authenticated:
            return AssessmentResult.objects.filter(user=self.request.user)
        else:
            session_id = self.request.query_params.get('session_id')
            if session_id:
                return AssessmentResult.objects.filter(session_id=session_id)
            return AssessmentResult.objects.none()
    
    def perform_create(self, serializer):
        """Automatically assign user if authenticated"""
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)


class CareerResourceViewSet(viewsets.ModelViewSet):
    """ViewSet for Career Resource operations"""
    queryset = CareerResource.objects.filter(is_active=True)
    serializer_class = CareerResourceSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['resource_type', 'category', 'difficulty_level', 'is_featured']
    search_fields = ['title', 'content', 'tags']
    ordering_fields = ['title', 'created_at', 'estimated_time']
    ordering = ['-is_featured', 'title']

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured resources"""
        featured_resources = self.get_queryset().filter(is_featured=True)[:6]
        serializer = self.get_serializer(featured_resources, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def categories(self, request):
        """Get all available resource categories"""
        categories = CareerResource.objects.filter(is_active=True).values_list('category', flat=True).distinct()
        return Response(list(categories))


class UserProfileViewSet(viewsets.ModelViewSet):
    """ViewSet for User Profile operations"""
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Users can only access their own profile"""
        return UserProfile.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """Automatically assign user when creating profile"""
        serializer.save(user=self.request.user)
    
    @action(detail=False, methods=['get', 'patch'])
    def me(self, request):
        """Get or update current user's profile"""
        try:
            profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            profile = UserProfile.objects.create(user=request.user)
        
        if request.method == 'GET':
            serializer = self.get_serializer(profile)
            return Response(serializer.data)
        
        elif request.method == 'PATCH':
            serializer = self.get_serializer(profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)