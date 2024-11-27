from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Project, Skill, Contact, AboutMe, TechStack
from .serializers import ProjectSerializer, SkillSerializer, ContactSerializer, AboutMeSerializer, TechStackSerializer
import logging

logger = logging.getLogger(__name__)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class AboutMeViewSet(viewsets.ModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer

class TechStackViewSet(viewsets.ModelViewSet):
    queryset = TechStack.objects.all()
    serializer_class = TechStackSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                # Save the contact message
                contact = serializer.save()
                
                # Prepare email to admin
                admin_subject = f'New Contact from Portfolio: {contact.name}'
                admin_message = f"""
                <html>
                    <body style="font-family: Arial, sans-serif; line-height: 1.6;">
                        <div style="max-width: 600px; margin: 20px auto; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
                            <h2 style="color: #1976d2; margin-bottom: 20px;">New Contact Form Submission</h2>
                            <div style="margin-bottom: 20px;">
                                <p><strong>Name:</strong> {contact.name}</p>
                                <p><strong>Email:</strong> {contact.email}</p>
                                <p><strong>Message:</strong></p>
                                <div style="background-color: #f5f5f5; padding: 15px; border-radius: 4px;">
                                    {contact.message}
                                </div>
                            </div>
                            <div style="color: #666; font-size: 14px; border-top: 1px solid #ddd; padding-top: 15px;">
                                <p>This message was sent from your portfolio website.</p>
                            </div>
                        </div>
                    </body>
                </html>
                """

                # Send email to admin (you)
                try:
                    admin_email = EmailMessage(
                        subject=admin_subject,
                        body=admin_message,
                        from_email=settings.EMAIL_HOST_USER,
                        to=[settings.ADMIN_EMAIL],
                        reply_to=[contact.email]
                    )
                    admin_email.content_subtype = "html"
                    admin_email.send()

                    # Send confirmation email to the sender
                    sender_subject = 'Thank you for contacting me'
                    sender_message = f"""
                    <html>
                        <body style="font-family: Arial, sans-serif; line-height: 1.6;">
                            <div style="max-width: 600px; margin: 20px auto; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
                                <h2 style="color: #1976d2; margin-bottom: 20px;">Thank You for Your Message</h2>
                                <p>Hello {contact.name},</p>
                                <p>Thank you for reaching out. I have received your message and will get back to you as soon as possible.</p>
                                <div style="margin-top: 20px;">
                                    <p>Best regards,</p>
                                    <p><strong>Navneet Yadav</strong></p>
                                </div>
                            </div>
                        </body>
                    </html>
                    """

                    sender_email = EmailMessage(
                        subject=sender_subject,
                        body=sender_message,
                        from_email=settings.EMAIL_HOST_USER,
                        to=[contact.email]
                    )
                    sender_email.content_subtype = "html"
                    sender_email.send()

                    return Response({
                        "message": "Your message has been sent successfully! Please check your email for confirmation."
                    }, status=status.HTTP_201_CREATED)

                except Exception as e:
                    logger.error(f"Email sending failed: {str(e)}")
                    return Response({
                        "message": "Your message was saved but email delivery failed. I'll still receive your message.",
                        "error": str(e)
                    }, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error(f"Contact creation failed: {str(e)}")
            return Response({
                "message": "Failed to process your request. Please try again later.",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 