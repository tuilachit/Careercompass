from django.db import models
from django.contrib.auth.models import User


class CareerPath(models.Model):
    """Represents a career path or profession"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=[
        ('technology', 'Technology'),
        ('healthcare', 'Healthcare'),
        ('business', 'Business'),
        ('education', 'Education'),
        ('arts', 'Arts & Creative'),
        ('science', 'Science'),
        ('engineering', 'Engineering'),
        ('finance', 'Finance'),
        ('marketing', 'Marketing'),
        ('other', 'Other'),
    ])
    salary_range_min = models.IntegerField(null=True, blank=True)
    salary_range_max = models.IntegerField(null=True, blank=True)
    education_level = models.CharField(max_length=100, choices=[
        ('high_school', 'High School'),
        ('associates', 'Associate Degree'),
        ('bachelors', 'Bachelor\'s Degree'),
        ('masters', 'Master\'s Degree'),
        ('phd', 'PhD'),
        ('certification', 'Professional Certification'),
    ])
    required_skills = models.JSONField(default=list, blank=True)
    growth_outlook = models.CharField(max_length=50, choices=[
        ('high', 'High Growth'),
        ('medium', 'Medium Growth'),
        ('stable', 'Stable'),
        ('declining', 'Declining'),
    ])
    work_environment = models.CharField(max_length=100, choices=[
        ('office', 'Office'),
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid'),
        ('field', 'Field Work'),
        ('laboratory', 'Laboratory'),
        ('hospital', 'Hospital'),
        ('school', 'School'),
    ])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class CareerAssessment(models.Model):
    """Represents a career assessment or quiz"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructions = models.TextField(blank=True)
    questions = models.JSONField(default=list)  # List of question objects
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class AssessmentResult(models.Model):
    """Stores user assessment results"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    assessment = models.ForeignKey(CareerAssessment, on_delete=models.CASCADE)
    answers = models.JSONField(default=list)  # User's answers
    recommended_careers = models.JSONField(default=list)  # Recommended career paths
    session_id = models.CharField(max_length=100, null=True, blank=True)  # For anonymous users
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-completed_at']

    def __str__(self):
        user_identifier = self.user.username if self.user else f"Anonymous ({self.session_id})"
        return f"{self.assessment.title} - {user_identifier}"


class CareerResource(models.Model):
    """Career-related resources like articles, guides, tools"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    resource_type = models.CharField(max_length=50, choices=[
        ('article', 'Article'),
        ('guide', 'Guide'),
        ('tool', 'Tool'),
        ('video', 'Video'),
        ('course', 'Course'),
        ('book', 'Book'),
    ])
    category = models.CharField(max_length=100, choices=[
        ('resume', 'Resume Building'),
        ('interview', 'Interview Preparation'),
        ('networking', 'Networking'),
        ('skills', 'Skill Development'),
        ('job_search', 'Job Search'),
        ('career_planning', 'Career Planning'),
    ])
    difficulty_level = models.CharField(max_length=50, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])
    estimated_time = models.IntegerField(null=True, blank=True)  # in minutes
    tags = models.JSONField(default=list, blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured', 'title']

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    """Extended user profile for career tracking"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    career_goals = models.JSONField(default=list, blank=True)
    current_career_path = models.ForeignKey(CareerPath, on_delete=models.SET_NULL, null=True, blank=True)
    interests = models.JSONField(default=list, blank=True)
    skills = models.JSONField(default=list, blank=True)
    experience_level = models.CharField(max_length=50, choices=[
        ('student', 'Student'),
        ('entry', 'Entry Level'),
        ('mid', 'Mid Level'),
        ('senior', 'Senior Level'),
        ('executive', 'Executive'),
    ], default='entry')
    preferred_work_environment = models.CharField(max_length=100, choices=[
        ('office', 'Office'),
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid'),
        ('field', 'Field Work'),
    ], blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"