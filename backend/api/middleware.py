from django.http import HttpResponse
from django.conf import settings
import os
import mimetypes

class SecureFileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Check if this is a resume download request
        if request.path.startswith('/media/resumes/'):
            # Add security headers
            response['Content-Disposition'] = 'attachment'
            response['X-Content-Type-Options'] = 'nosniff'
            
            # Validate file type
            content_type = response.get('Content-Type', '')
            if content_type not in settings.ALLOWED_UPLOAD_TYPES:
                return HttpResponse(status=403)
        
        return response 