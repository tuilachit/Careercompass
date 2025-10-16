from django.core.management.base import BaseCommand
from api.models import CareerPath, CareerAssessment, CareerResource


class Command(BaseCommand):
    help = 'Populate the database with sample career data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample career data...')

        # Create sample career paths
        career_paths_data = [
            {
                'title': 'Software Developer',
                'description': 'Design, develop, and maintain software applications and systems.',
                'category': 'technology',
                'salary_range_min': 60000,
                'salary_range_max': 120000,
                'education_level': 'bachelors',
                'required_skills': ['Programming', 'Problem Solving', 'Teamwork', 'Communication'],
                'growth_outlook': 'high',
                'work_environment': 'office'
            },
            {
                'title': 'Data Scientist',
                'description': 'Analyze complex data to help organizations make informed decisions.',
                'category': 'technology',
                'salary_range_min': 70000,
                'salary_range_max': 130000,
                'education_level': 'masters',
                'required_skills': ['Statistics', 'Python', 'Machine Learning', 'Data Visualization'],
                'growth_outlook': 'high',
                'work_environment': 'office'
            },
            {
                'title': 'UX Designer',
                'description': 'Create user-friendly and intuitive digital experiences.',
                'category': 'technology',
                'salary_range_min': 50000,
                'salary_range_max': 100000,
                'education_level': 'bachelors',
                'required_skills': ['Design Thinking', 'Prototyping', 'User Research', 'Collaboration'],
                'growth_outlook': 'high',
                'work_environment': 'hybrid'
            },
            {
                'title': 'Registered Nurse',
                'description': 'Provide patient care and support in healthcare settings.',
                'category': 'healthcare',
                'salary_range_min': 50000,
                'salary_range_max': 80000,
                'education_level': 'bachelors',
                'required_skills': ['Patient Care', 'Medical Knowledge', 'Empathy', 'Critical Thinking'],
                'growth_outlook': 'high',
                'work_environment': 'hospital'
            },
            {
                'title': 'Marketing Manager',
                'description': 'Develop and execute marketing strategies to promote products and services.',
                'category': 'marketing',
                'salary_range_min': 55000,
                'salary_range_max': 110000,
                'education_level': 'bachelors',
                'required_skills': ['Strategic Thinking', 'Communication', 'Analytics', 'Creativity'],
                'growth_outlook': 'medium',
                'work_environment': 'office'
            },
            {
                'title': 'Financial Analyst',
                'description': 'Analyze financial data to help organizations make investment decisions.',
                'category': 'finance',
                'salary_range_min': 55000,
                'salary_range_max': 95000,
                'education_level': 'bachelors',
                'required_skills': ['Financial Modeling', 'Excel', 'Analytical Thinking', 'Attention to Detail'],
                'growth_outlook': 'medium',
                'work_environment': 'office'
            }
        ]

        for path_data in career_paths_data:
            career_path, created = CareerPath.objects.get_or_create(
                title=path_data['title'],
                defaults=path_data
            )
            if created:
                self.stdout.write(f'Created career path: {career_path.title}')
            else:
                self.stdout.write(f'Career path already exists: {career_path.title}')

        # Create sample career assessment
        assessment_data = {
            'title': 'Career Interest Assessment',
            'description': 'Discover your career interests and find matching career paths.',
            'instructions': 'Answer each question honestly based on your preferences and interests.',
            'questions': [
                {
                    'id': 1,
                    'question': 'What type of work environment do you prefer?',
                    'type': 'multiple_choice',
                    'options': [
                        'Office setting with regular hours',
                        'Remote work with flexible schedule',
                        'Field work with travel',
                        'Hospital or clinical setting',
                        'Laboratory or research facility'
                    ]
                },
                {
                    'id': 2,
                    'question': 'What activities do you enjoy most?',
                    'type': 'multiple_choice',
                    'options': [
                        'Solving complex problems',
                        'Creating and designing',
                        'Helping and caring for others',
                        'Analyzing data and numbers',
                        'Leading and managing teams'
                    ]
                },
                {
                    'id': 3,
                    'question': 'What is your preferred level of education?',
                    'type': 'multiple_choice',
                    'options': [
                        'High school diploma',
                        'Associate degree',
                        'Bachelor\'s degree',
                        'Master\'s degree',
                        'PhD or professional degree'
                    ]
                },
                {
                    'id': 4,
                    'question': 'Which skills do you feel most confident in?',
                    'type': 'multiple_select',
                    'options': [
                        'Programming and coding',
                        'Communication and writing',
                        'Mathematical analysis',
                        'Creative design',
                        'Medical knowledge',
                        'Leadership and management'
                    ]
                },
                {
                    'id': 5,
                    'question': 'What salary range are you targeting?',
                    'type': 'multiple_choice',
                    'options': [
                        '$30,000 - $50,000',
                        '$50,000 - $70,000',
                        '$70,000 - $90,000',
                        '$90,000 - $120,000',
                        '$120,000+'
                    ]
                }
            ]
        }

        assessment, created = CareerAssessment.objects.get_or_create(
            title=assessment_data['title'],
            defaults=assessment_data
        )
        if created:
            self.stdout.write(f'Created assessment: {assessment.title}')
        else:
            self.stdout.write(f'Assessment already exists: {assessment.title}')

        # Create sample career resources
        resources_data = [
            {
                'title': 'How to Write a Winning Resume',
                'content': 'A comprehensive guide to crafting a professional resume that stands out to employers.',
                'resource_type': 'guide',
                'category': 'resume',
                'difficulty_level': 'beginner',
                'estimated_time': 60,
                'tags': ['resume', 'job search', 'career'],
                'is_featured': True
            },
            {
                'title': 'Interview Preparation Checklist',
                'content': 'Essential steps to prepare for any job interview and increase your chances of success.',
                'resource_type': 'tool',
                'category': 'interview',
                'difficulty_level': 'beginner',
                'estimated_time': 30,
                'tags': ['interview', 'preparation', 'tips'],
                'is_featured': True
            },
            {
                'title': 'Building Your Professional Network',
                'content': 'Strategies for networking effectively and building meaningful professional relationships.',
                'resource_type': 'article',
                'category': 'networking',
                'difficulty_level': 'intermediate',
                'estimated_time': 45,
                'tags': ['networking', 'career development', 'relationships'],
                'is_featured': False
            },
            {
                'title': 'Career Planning Worksheet',
                'content': 'A step-by-step worksheet to help you plan your career goals and track your progress.',
                'resource_type': 'tool',
                'category': 'career_planning',
                'difficulty_level': 'beginner',
                'estimated_time': 90,
                'tags': ['career planning', 'goals', 'worksheet'],
                'is_featured': True
            },
            {
                'title': 'Technical Skills Assessment',
                'content': 'Evaluate your technical skills and identify areas for improvement.',
                'resource_type': 'tool',
                'category': 'skills',
                'difficulty_level': 'intermediate',
                'estimated_time': 60,
                'tags': ['skills', 'assessment', 'technical'],
                'is_featured': False
            }
        ]

        for resource_data in resources_data:
            resource, created = CareerResource.objects.get_or_create(
                title=resource_data['title'],
                defaults=resource_data
            )
            if created:
                self.stdout.write(f'Created resource: {resource.title}')
            else:
                self.stdout.write(f'Resource already exists: {resource.title}')

        self.stdout.write(
            self.style.SUCCESS('Successfully populated sample data!')
        )
