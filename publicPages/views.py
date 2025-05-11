from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
# Create your views here.
from django.http import HttpResponse

from lavaroWebApp import settings

def index(request):
       return render(request, 'index.html')

def contact(request):
       return render(request, 'contact.html')
   
def services(request):
       return render(request, 'services.html')
   
def about(request):
       return render(request, 'portfolio.html')
def testimonials(request):
       return render(request, 'testimonials.html')

def send_email(request):
   
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        
        # Validate email format
        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'message.html', {'error': 'Invalid email format.'})
        
        # Email subject and content
        subject = f'Web Site Contact from {name}'
        
        # Render plain text message
        message_content = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        """
        
        # Render HTML message
        html_message_content = render_to_string('contactEmailTemplate.html', {
            'name': name,
            'email': email,
            'phone': phone,
            'message': message,
        })
        
        # Send email using Django's EmailMultiAlternatives class
        email_message = EmailMultiAlternatives(subject, message_content, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])
        email_message.attach_alternative(html_message_content, "text/html")
        email_message.send()
        
        
        context = {'message': 'Your inquiry is sent successfully', 'status': 'ok'}        
        # Redirect after successful submission
        return render(request, 'message.html', context)
    
    return render(request, 'error.html', {'error': 'Method not allowed.'})
