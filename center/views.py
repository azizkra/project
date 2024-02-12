from pyexpat.errors import messages
from django.shortcuts import render, get_object_or_404
# from django.core.mail import send_mail
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
    posts = Post.objects.filter(status='published')
    post_id = Post.objects.get(id=4)
    # sent messages
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     message = request.POST.get('message')
    #     send_mail('newsteller', message, email, ['ahmed059kh@gmail.com'], fail_silently=True)
    #     # send_mail('newsteller', message, 'iv.7l@live.com', ['ahmed059kh@gmail.com'], fail_silently=True)
        
        # messages.success(request, 'Inquiry message sent.')
        
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        ssuccess_message_me = f"Message sent successfully. Thank you for contacting us {name}."
        messages.success(request, ssuccess_message_me)
        
    nav=True
    context = {
        'posts': posts,
        'nav': nav,
        'post_id': post_id,
    }
    return render(request, 'pages/home.html', context)

#لعرض جميع النشاطات 
def activities(request):
    posts = Post.objects.filter(status='published').order_by('-create')
    context = {
        'posts': posts,
    }
    return render(request, 'pages/activities.html', context)


# لعرض تقرير لكل نشاط 
def post_detail(request, post):
    posts = get_object_or_404(Post, slug=post, status='published' )
    context = {
        'posts': posts,
    }
    return render(request, 'pages/detail.html', context)

# عن المركز
def about(request):

    return render(request, 'pages/about.html')

# صفحة الدعم
def supportus(request):
    
    return render(request, 'pages/supportus.html')
