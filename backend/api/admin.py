from django.contrib import admin
from django.utils.html import format_html
from .models import Project, Skill, Contact, AboutMe, TechStack, Education

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_image', 'featured', 'order', 'created_at', 'display_links')
    list_editable = ('featured', 'order')
    list_filter = ('featured', 'technologies')
    search_fields = ('title', 'description', 'technologies')
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'image')
        }),
        ('Technical Details', {
            'fields': ('technologies', 'github_link', 'live_link')
        }),
        ('Display Options', {
            'fields': ('featured', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />', obj.image.url)
        return "No Image"
    display_image.short_description = 'Image'

    def display_links(self, obj):
        links = []
        if obj.github_link:
            links.append(format_html('<a href="{}" target="_blank">GitHub</a>', obj.github_link))
        if obj.live_link:
            links.append(format_html('<a href="{}" target="_blank">Live Demo</a>', obj.live_link))
        return format_html(' | '.join(links)) if links else '-'
    display_links.short_description = 'Links'

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_icon', 'category', 'proficiency', 'order')
    list_editable = ('category', 'proficiency', 'order')
    list_filter = ('category', 'proficiency')
    search_fields = ('name',)
    ordering = ('order', 'name')

    def display_icon(self, obj):
        if obj.icon:
            return format_html('<img src="{}" width="30" height="30" />', obj.icon.url)
        return "No Icon"
    display_icon.short_description = 'Icon'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)
    list_editable = ('is_read',)
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"

    actions = [mark_as_read]

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'location', 'start_date', 'end_date', 'is_current', 'order')
    list_editable = ('order', 'is_current')
    list_filter = ('is_current',)
    search_fields = ('degree', 'institution', 'location')
    ordering = ('order', '-start_date')
    fieldsets = (
        ('Basic Information', {
            'fields': ('degree', 'institution', 'location')
        }),
        ('Timeline', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Details', {
            'fields': ('description', 'grade', 'order')
        }),
    )

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'display_profile_image', 'email', 'has_resume')
    readonly_fields = ('display_profile_image', 'display_resume_link')
    filter_horizontal = ('education',)
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'title', 'profile_image', 'display_profile_image', 'bio')
        }),
        ('Resume', {
            'fields': ('resume', 'display_resume_link'),
            'description': 'Upload your resume (PDF, DOC, or DOCX format, max 5MB)'
        }),
        ('Contact Information', {
            'fields': ('email', 'location')
        }),
        ('Social Links', {
            'fields': ('github', 'linkedin', 'twitter')
        }),
        ('Experience', {
            'fields': ('years_of_experience', 'projects_completed')
        }),
        ('Education', {
            'fields': ('education',),
            'description': 'Select education entries from the list below'
        }),
    )

    def display_profile_image(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" width="100" height="100" style="border-radius: 50%; object-fit: cover;" />', obj.profile_image.url)
        return "No Image"
    display_profile_image.short_description = 'Profile Preview'

    def has_resume(self, obj):
        return bool(obj.resume)
    has_resume.boolean = True
    has_resume.short_description = 'Has Resume'

    def display_resume_link(self, obj):
        if obj.resume:
            return format_html(
                '<a href="{}" target="_blank">View Current Resume</a>',
                obj.resume.url
            )
        return "No resume uploaded"
    display_resume_link.short_description = 'Current Resume'

@admin.register(TechStack)
class TechStackAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'display_icon', 'order')
    list_editable = ('category', 'order')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('category', 'order')

    def display_icon(self, obj):
        if obj.icon:
            return format_html('<img src="{}" width="30" height="30" />', obj.icon.url)
        return "No Icon"
    display_icon.short_description = 'Icon'
    