from django.shortcuts import redirect, render

from todos.models import Item, Tag

from django.utils import timezone
import datetime

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    
    items = Item.objects.all().filter(archived=False).order_by('-created')
    return render(request, 'home.html', { 'items': items })

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
        item.due_date = datetime.datetime.strptime(request.POST['due_date'], '%m/%d/%Y %I:%M %p') # (10/29/2015 12:00 AM) 
        
        raw_tags = request.POST['tags'].lower()
        raw_tags = raw_tags.split(",")
        tags_list = []
        for raw_tag in raw_tags:
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

