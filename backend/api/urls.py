from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProjectViewSet, SkillViewSet, ContactViewSet,
    AboutMeViewSet, TechStackViewSet
)

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'about', AboutMeViewSet)
router.register(r'tech-stack', TechStackViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 