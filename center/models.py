from email.policy import default
from turtle import title
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200, null=True)
    post_photo = models.ImageField(upload_to='post_photo', default='post_photo/DSC07477.jpg', null=True)
    slug = models.SlugField(null=True, blank=True)
    # video = models.FileField(upload_to='videos_uploaded', null=True, blank=True)    
    p1 = models.TextField(null=True, blank=True)
    p2 = models.TextField(null=True, blank=True)
    p3 = models.TextField(null=True, blank=True)
    p4 = models.TextField(null=True, blank=True)
    p5 = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='draft')
    # # new
    price = models.IntegerField(default=100, null=True)
    link_href = models.URLField()
    
    create =  models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-create']
    
    def save(self, *aegs, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*aegs, **kwargs)
    
    def get_absolute_url(self):
        return reverse('center:detail', args=[self.slug])
    
class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    create =  models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-create']
        
        
        
        
        
        
        
        
        
        
        
        
        
