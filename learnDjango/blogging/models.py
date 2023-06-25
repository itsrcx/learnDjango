from django.db import models

from django.contrib.auth.models import User

# form rendering different
status = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=status,default = 0)

    class Meta:
        ordering = ['-created_on'] # - is the sign of descending

    def __str__(self):
        return self.title
    