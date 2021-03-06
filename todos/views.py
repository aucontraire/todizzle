from django.shortcuts import redirect, render
from django.views import generic
from django.utils import timezone

from todos.models import Item, Tag
from todos.forms import TagForm

import datetime


class HomeView(generic.View):
    def get(self, request):
        items = Item.objects.all().filter(archived=False).order_by('-created')
        
        return render(request, 'home.html', { 'items': items })
    
    def post(self, request, *args, **kwargs):
        Item.objects.create(text=request.POST['item_text'])
        
        return redirect('/')


def item_page(request, item_pk):
    item = Item.objects.get(pk=item_pk)
    
    if item.tags:
        tags = []
        for tag in item.tags.all():
            tags.append(tag.name)
        
        tags = ','.join(tags)
    else:
        tags = ''
        
    if request.method == 'POST':
        due_date = request.POST['due_date']
        if due_date != '':
            item.due_date = datetime.datetime.strptime(due_date, '%m/%d/%Y %I:%M %p') # (10/29/2015 12:00 AM) 
        
        raw_tags = "".join(request.POST['tags'].lower().split())
        if len(raw_tags) > 0:
            tags_list = []
            for raw_tag in raw_tags.split(","):
                tag, created = Tag.objects.get_or_create(name=raw_tag)
                tags_list.append(tag)
            item.tags.add(*tags_list) 
        
        item.save()
        
        return redirect('/')
    
    return render(request, 'item.html', { 'item': item, 'tags': tags })
    
def item_complete(request, item_pk): 
    item = Item.objects.get(pk=item_pk)
    timezone.activate("America/Los_Angeles")
    item.completed_date = timezone.now()
    item.completed = True
    item.save()
    
    return render(request, 'home.html')
    
def item_archive(request, item_pk):
    item = Item.objects.get(pk=item_pk)
    item.archived = True
    item.save()
    
def item_delete(request, item_pk):
    item = Item.objects.get(pk=item_pk)
    item.delete()


class TagsView(generic.ListView):
    template_name = 'tags.html'
    context_object_name = 'tags'
    
    def get_queryset(self):
        return Tag.objects.all().order_by('name')
    
   
def tag_view(request, tag_pk):
    tag = Tag.objects.get(pk=tag_pk)
    items = Item.objects.filter(tags=tag).filter(archived=False).order_by('-created')
    
    if request.method == 'POST':
        item = Item.objects.create(text=request.POST['item_text'])
        item.tags.add(tag)
        
        return redirect('tag_view', tag.pk)
    
    return render(request, 'tag.html', { 'tag': tag, 'items': items })


