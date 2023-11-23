from django.shortcuts import render

# Create your views here.
def dummy2(request):
    return render(request, 'dummy_app2.html')