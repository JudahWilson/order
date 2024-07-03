from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'header': 'Epic Tasks', 'version': '1.0.0'}
    return render(request, 'index.html', context)
    ###################
    # OR 
    ###################
    return HttpResponse("Hello World!")
