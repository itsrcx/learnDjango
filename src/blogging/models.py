from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# form rendering different
status = (
    (0, "Draft"),
    (1, "Publish")
)

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    # goes back to post     
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    category = models.CharField(max_length=50, default='uncatogrised')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=status,default = 1)

    class Meta:
        ordering = ['-created_on'] # - is the sign of descending

    def __str__(self):
        return self.title + '|' + str(self.author)
    # goes back to post     
    def get_absolute_url(self):
        return reverse('home')
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body,self.name)