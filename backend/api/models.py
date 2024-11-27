from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    technologies = models.CharField(max_length=200, help_text="Comma separated list of technologies")
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0, help_text="Order of appearance")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='skills/')
    proficiency = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    category = models.CharField(max_length=50, choices=[
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('devops', 'DevOps'),
        ('other', 'Other')
    ])
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.email}"

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    grade = models.CharField(max_length=50, blank=True)
    is_current = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_date']
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} from {self.institution}"

    def clean(self):
        if self.end_date and self.end_date < self.start_date:
            raise ValidationError('End date cannot be before start date')

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, help_text="e.g., Full Stack Developer")
    profile_image = models.ImageField(upload_to='profile/')
    bio = models.TextField()
    resume = models.FileField(
        upload_to='resumes/',
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['pdf', 'doc', 'docx']
            )
        ]
    )
    
    # Social Links
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    email = models.EmailField()
    location = models.CharField(max_length=100)

    # Experience
    years_of_experience = models.IntegerField(default=0)
    projects_completed = models.IntegerField(default=0)

    # Education
    education = models.ManyToManyField(Education, related_name='about_me', blank=True)
    
    class Meta:
        verbose_name_plural = "About Me"
    
    def clean(self):
        super().clean()
        if self.resume:
            if self.resume.size > 5 * 1024 * 1024:  # 5MB limit
                raise ValidationError('Resume file size cannot exceed 5MB.')

    def __str__(self):
        return f"{self.name}'s Profile"

class TechStack(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('tools', 'Tools & Others')
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='tech_icons/')
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['category', 'order']
        verbose_name_plural = "Tech Stack"

    def __str__(self):
        return f"{self.name} ({self.category})" 