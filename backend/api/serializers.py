from rest_framework import serializers
from .models import Project, Skill, Contact, AboutMe, TechStack, Education

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class AboutMeSerializer(serializers.ModelSerializer):
    education = EducationSerializer(many=True, read_only=True)

    class Meta:
        model = AboutMe
        fields = '__all__'

class TechStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechStack
        fields = '__all__'
 