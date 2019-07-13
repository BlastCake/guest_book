from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Note(models.Model):
    user_name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=50, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    home_page = models.URLField(max_length=150, blank=True)
    text = models.TextField(max_length=350)
    tags = models.ManyToManyField('Tag', blank=True, related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('list_notes')

    def __str__(self):
        return '{} | {} | {}'.format(self.user_name, self.email, self.text)



class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.title