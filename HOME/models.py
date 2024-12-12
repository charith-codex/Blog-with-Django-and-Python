from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from = 'name', unique = True, null=True, default=None)

    def save (self, *args, **kwargs):
        if not self.slug:
           base_slug =   slugify(self.name)
           self.slug = f"{base_slug}"
        super().save(*args, **kwargs)
    def __str__(self) -> str:
        return self.name
    
class Blog(models.Model):
    STATUS = {
        ('0', 'DRAFT',)
        ('1', 'PUBLISH')
    }
    
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='/images')
    content = models.TextField()
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    blog_slug = AutoSlugField(populated_from= 'title', unique=True, null=True, default=None)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=1, default=0)