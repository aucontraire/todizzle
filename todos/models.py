from django.db import models
from django.utils import timezone
from django.template.defaultfilters import default


class Tag(models.Model):
    created = models.DateTimeField(default=timezone.now, blank=True)
    name = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name


class Item(models.Model):
    created = models.DateTimeField(default=timezone.now, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    text = models.TextField(default='')
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(blank=True, null=True)
    archived = models.BooleanField(default=False) 
    
    def __str__(self):
        return self.text

    def friendly_created_date(self):        
        created = self.created

        return created.strftime('%B %d, %Y, %I:%M %p')
    
    def friendly_due_date(self):
        due_date = timezone.localtime(self.due_date)
        
        return due_date.strftime('%B %d, %Y, %I:%M %p')

    def friendly_completed_date(self):
        completed_date = self.completed_date
        
        return completed_date.strftime('%B %d, %Y, %I:%M %p')   
    