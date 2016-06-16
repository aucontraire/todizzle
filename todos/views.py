from django.shortcuts import redirect, render

from todos.models import Item

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    
    items = Item.objects.all().order_by('-created')
    return render(request, 'home.html', { 'items': items })

def item_page(request, item_pk):
    
    item = Item.objects.get(pk=item_pk)
    
    return render(request, 'item.html', { 'item': item })
    