from django.core.management.base import BaseCommand
from api.models import Project, Skill, TechStack, AboutMe, Education
from django.utils import timezone
from datetime import date

class Command(BaseCommand):
    help = 'Adds sample data to the database'

    def handle(self, *args, **kwargs):
        # Create About Me Profile
        about_me = AboutMe.objects.create(
            name='Navneet Yadav',
            title='Full Stack Developer',
            bio='Passionate full-stack developer with expertise in React.js and Django. I love creating efficient, scalable, and user-friendly solutions.',
            email='ynavneet828@gmail.com',
            location='Greater Noida',
            github='https://github.com/yourusername',
            linkedin='https://linkedin.com/in/yourusername',
            years_of_experience=2,
            projects_completed=15
        )

        # Create Education Entries
        education_data = [
            {
                'degree': 'B.Tech in Computer Science',
                'institution': 'Your University',
                'location': 'Greater Noida',
                'start_date': date(2019, 8, 1),
                'end_date': date(2023, 5, 30),
                'grade': '8.5 CGPA',
                'description': 'Specialized in Computer Science and Engineering'
            },
            {
                'degree': '12th Standard',
                'institution': 'Your School',
                'location': 'Your City',
                'start_date': date(2018, 4, 1),
                'end_date': date(2019, 3, 30),
                'grade': '85%',
                'description': 'Science Stream with Computer Science'
            }
        ]

        for edu in education_data:
            education = Education.objects.create(**edu)
            about_me.education.add(education)

        # Create Skills
        skills_data = [
            {
                'name': 'React.js',
                'category': 'frontend',
                'proficiency': 5,
                'order': 1
            },
            {
                'name': 'Django',
                'category': 'backend',
                'proficiency': 5,
                'order': 1
            },
            {
                'name': 'PostgreSQL',
                'category': 'database',
                'proficiency': 4,
                'order': 1
            },
            {
                'name': 'Docker',
                'category': 'devops',
                'proficiency': 4,
                'order': 1
            }
        ]

        for skill in skills_data:
            Skill.objects.create(**skill)

        # Create Tech Stack
        tech_stack_data = [
            {
                'name': 'HTML5/CSS3',
                'category': 'frontend',
                'order': 1
            },
            {
                'name': 'Python',
                'category': 'backend',
                'order': 1
            },
            {
                'name': 'Git',
                'category': 'tools',
                'order': 1
            }
        ]

        for tech in tech_stack_data:
            TechStack.objects.create(**tech)

        # Create Projects
        projects_data = [
            {
                'title': 'E-Commerce Platform',
                'description': 'A full-featured online shopping platform with cart management, payment processing, and order tracking.',
                'technologies': 'React,Django,PostgreSQL,Stripe,Redis',
                'github_link': 'https://github.com/yourusername/ecommerce',
                'live_link': 'https://ecommerce-demo.com',
                'featured': True,
                'order': 1
            },
            {
                'title': 'Portfolio Website',
                'description': 'Personal portfolio website built with React and Django.',
                'technologies': 'React,Django,Tailwind CSS',
                'github_link': 'https://github.com/yourusername/portfolio',
                'live_link': 'https://portfolio-demo.com',
                'featured': True,
                'order': 2
            },
            {
                'title': 'Task Management System',
                'description': 'A collaborative project management tool with real-time updates.',
                'technologies': 'React,Django,WebSocket,PostgreSQL',
                'github_link': 'https://github.com/yourusername/task-manager',
                'live_link': 'https://task-manager-demo.com',
                'featured': True,
                'order': 3
            }
        ]

        for project in projects_data:
            Project.objects.create(**project)

        self.stdout.write(self.style.SUCCESS('Successfully added sample data')) 