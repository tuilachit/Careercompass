from django.contrib import admin
from .models import CareerPath, CareerAssessment, AssessmentResult, CareerResource, UserProfile


@admin.register(CareerPath)
class CareerPathAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'education_level', 'growth_outlook', 'is_active']
    list_filter = ['category', 'education_level', 'growth_outlook', 'work_environment', 'is_active']
    search_fields = ['title', 'description']
    list_editable = ['is_active']
    ordering = ['title']


@admin.register(CareerAssessment)
class CareerAssessmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_active']
    ordering = ['-created_at']


@admin.register(AssessmentResult)
class AssessmentResultAdmin(admin.ModelAdmin):
    list_display = ['assessment', 'user', 'session_id', 'completed_at']
    list_filter = ['assessment', 'completed_at']
    search_fields = ['user__username', 'session_id']
    readonly_fields = ['completed_at']
    ordering = ['-completed_at']


@admin.register(CareerResource)
class CareerResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'resource_type', 'category', 'difficulty_level', 'is_featured', 'is_active']
    list_filter = ['resource_type', 'category', 'difficulty_level', 'is_featured', 'is_active']
    search_fields = ['title', 'content']
    list_editable = ['is_featured', 'is_active']
    ordering = ['-is_featured', 'title']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'experience_level', 'current_career_path', 'created_at']
    list_filter = ['experience_level', 'current_career_path', 'created_at']
    search_fields = ['user__username', 'user__email']
    ordering = ['-created_at']