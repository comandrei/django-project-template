from django.shortcuts import render
# Create your views here.

def hello(request):
    context = {
        'ana': 'are mere'
    }
    return render(request, "hello.html", context)
