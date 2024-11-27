from django.core.management.base import BaseCommand
from api.models import Project

class Command(BaseCommand):
    help = 'Adds sample projects to the database'

    def handle(self, *args, **kwargs):
        projects = [
            {
                'title': 'E-Commerce Platform',
                'description': 'A full-featured online shopping platform with cart management, payment processing, and order tracking. Implements secure user authentication and real-time inventory updates.',
                'technologies': 'React,Django,PostgreSQL,Stripe,Redis',
                'github_link': 'https://github.com/yourusername/ecommerce',
                'live_link': 'https://ecommerce-demo.com',
                'image': 'https://via.placeholder.com/800x600/2563eb/FFFFFF?text=E-Commerce'
            },
            {
                'title': 'AI Chat Assistant',
                'description': 'An intelligent chatbot powered by OpenAI GPT-3, featuring real-time conversation, context awareness, and multi-language support. Includes voice input and custom training capabilities.',
                'technologies': 'Python,OpenAI,WebSocket,React,MongoDB',
                'github_link': 'https://github.com/yourusername/ai-chat',
                'live_link': 'https://ai-chat-demo.com',
                'image': 'https://via.placeholder.com/800x600/059669/FFFFFF?text=AI+Chat'
            },
            {
                'title': 'Task Management System',
                'description': 'A collaborative project management tool with real-time updates, task assignment, progress tracking, and team communication features. Includes calendar integration and file sharing.',
                'technologies': 'React,Node.js,Socket.io,MySQL',
                'github_link': 'https://github.com/yourusername/task-manager',
                'live_link': 'https://task-manager-demo.com',
                'image': 'https://via.placeholder.com/800x600/7C3AED/FFFFFF?text=Task+Manager'
            },
            {
                'title': 'Social Media Dashboard',
                'description': 'A comprehensive analytics dashboard for social media metrics, featuring real-time data visualization, trend analysis, and automated reporting. Supports multiple platforms and custom metrics.',
                'technologies': 'Vue.js,Django,D3.js,PostgreSQL',
                'github_link': 'https://github.com/yourusername/social-dashboard',
                'live_link': 'https://social-dashboard-demo.com',
                'image': 'https://via.placeholder.com/800x600/DC2626/FFFFFF?text=Social+Dashboard'
            },
            {
                'title': 'Weather Forecast App',
                'description': 'A modern weather application with location-based forecasts, interactive maps, and severe weather alerts. Features hourly and weekly predictions with detailed meteorological data.',
                'technologies': 'React Native,Node.js,OpenWeatherAPI',
                'github_link': 'https://github.com/yourusername/weather-app',
                'live_link': 'https://weather-app-demo.com',
                'image': 'https://via.placeholder.com/800x600/2563eb/FFFFFF?text=Weather+App'
            },
            {
                'title': 'Recipe Sharing Platform',
                'description': 'A community-driven recipe sharing platform with user profiles, recipe creation, ratings, and comments. Includes meal planning and grocery list generation features.',
                'technologies': 'React,Firebase,Algolia,Cloudinary',
                'github_link': 'https://github.com/yourusername/recipe-platform',
                'live_link': 'https://recipe-platform-demo.com',
                'image': 'https://via.placeholder.com/800x600/059669/FFFFFF?text=Recipe+Platform'
            }
        ]

        for project_data in projects:
            Project.objects.get_or_create(
                title=project_data['title'],
                defaults={
                    'description': project_data['description'],
                    'technologies': project_data['technologies'],
                    'github_link': project_data['github_link'],
                    'live_link': project_data['live_link'],
                    'image': project_data['image']
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully added sample projects')) 