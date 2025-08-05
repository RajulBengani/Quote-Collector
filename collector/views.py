from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddForm
from .models import Quote
from django.db.models import Q
    
# Create your views here.
def index(request):
    query=request.GET.get('q')
    if query:
        quotes=Quote.objects.filter(
            Q(quote__icontains=query)| Q(author__icontains=query)
        )
    else:
        quotes = Quote.objects.all().order_by('-id')
    return render(request, 'collector/index.html',{
        "quotes": quotes,
        "query": query
    })

def add(request):
    if request.method=="POST":
        form=AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=AddForm()
    return render(request, 'collector/add.html',{
        "form":form
    })

def update(request,id):
    if request.method=="POST":
        form=AddForm(request.POST, instance=get_object_or_404(Quote, id=id))
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        return render(request, 'collector/update.html',{
            "form":AddForm(instance=get_object_or_404(Quote, id=id)),
            "quote":get_object_or_404(Quote, id=id)

    })
    
def delete(request, id):
    quote = get_object_or_404(Quote, id=id)
    if request.method == "POST":
        quote.delete()
        return redirect('index')
    else:
        return redirect('delete', id=id)  
    

    
         
        
    