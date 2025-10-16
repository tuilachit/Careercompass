from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CareerPath, CareerAssessment, AssessmentResult, CareerResource, UserProfile


class CareerPathSerializer(serializers.ModelSerializer):
    """Serializer for Career Path model"""
    
    class Meta:
        model = CareerPath
        fields = [
            'id', 'title', 'description', 'category', 
            'salary_range_min', 'salary_range_max', 'education_level',
            'required_skills', 'growth_outlook', 'work_environment',
            'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class CareerAssessmentSerializer(serializers.ModelSerializer):
    """Serializer for Career Assessment model"""
    
    class Meta:
        model = CareerAssessment
        fields = [
            'id', 'title', 'description', 'instructions',
            'questions', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class AssessmentResultSerializer(serializers.ModelSerializer):
    """Serializer for Assessment Result model"""
    assessment_title = serializers.CharField(source='assessment.title', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = AssessmentResult
        fields = [
            'id', 'user', 'assessment', 'answers', 'recommended_careers',
            'session_id', 'completed_at', 'assessment_title', 'user_username'
        ]
        read_only_fields = ['id', 'completed_at', 'assessment_title', 'user_username']


class CareerResourceSerializer(serializers.ModelSerializer):
    """Serializer for Career Resource model"""
    
    class Meta:
        model = CareerResource
        fields = [
            'id', 'title', 'content', 'resource_type', 'category',
            'difficulty_level', 'estimated_time', 'tags', 'is_featured',
            'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class UserSerializer(serializers.ModelSerializer):
    """Basic user serializer"""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for User Profile model"""
    user = UserSerializer(read_only=True)
    current_career_path = CareerPathSerializer(read_only=True)
    current_career_path_id = serializers.IntegerField(write_only=True, required=False)
    
    class Meta:
        model = UserProfile
        fields = [
            'id', 'user', 'career_goals', 'current_career_path',
            'current_career_path_id', 'interests', 'skills',
            'experience_level', 'preferred_work_environment',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def update(self, instance, validated_data):
        # Handle career path assignment
        if 'current_career_path_id' in validated_data:
            career_path_id = validated_data.pop('current_career_path_id')
            if career_path_id:
                try:
                    instance.current_career_path = CareerPath.objects.get(id=career_path_id)
                except CareerPath.DoesNotExist:
                    pass
            else:
                instance.current_career_path = None
        
        return super().update(instance, validated_data)


class AssessmentSubmissionSerializer(serializers.Serializer):
    """Serializer for submitting assessment answers"""
    assessment_id = serializers.IntegerField()
    answers = serializers.JSONField()
    session_id = serializers.CharField(required=False, allow_blank=True)
    
    def validate_assessment_id(self, value):
        try:
            CareerAssessment.objects.get(id=value, is_active=True)
        except CareerAssessment.DoesNotExist:
            raise serializers.ValidationError("Assessment not found or inactive")
        return value


class CareerRecommendationSerializer(serializers.Serializer):
    """Serializer for career recommendations based on assessment"""
    career_paths = CareerPathSerializer(many=True, read_only=True)
    confidence_scores = serializers.JSONField(read_only=True)
    reasoning = serializers.CharField(read_only=True)
