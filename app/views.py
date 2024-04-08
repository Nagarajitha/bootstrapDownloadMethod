from django.shortcuts import render

# Create your views here.
def alerts(request):
    return render(request,'alerts.html')

def badge(request):
    return render(request,'badge.html')

def breadcrumb(request):
    return render(request,'breadcrumb.html')

def button(request):
    return render(request, 'button.html')

def buttongroup(request):
    return render(request,'buttongroup.html')

def cards(request):
    return render(request,'cards.html')

def carousel(request):
    return render(request, 'carousel.html')

def collapse(request):
    return render(request,'collapse.html')
def dropdowns(request):
    return render(request,'dropdowns.html')

def forms(request):
    return render(request,'forms.html')
