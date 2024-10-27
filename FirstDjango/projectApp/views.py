from django.shortcuts import render

def Fetch_Django(request):
    return render(request, 'projectApp/index_all.html')

# Create your views here.
