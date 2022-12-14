from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        'var1' : 'its my dynamic var value' 
    }
    return render(request, 'index.html', context)