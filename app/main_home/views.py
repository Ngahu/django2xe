from django.shortcuts import render

# Create your views here.



def home_view(request):
    template_name = 'home/index.html'
    context = {}
    return render(request,template_name,context)