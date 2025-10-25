from django.shortcuts import render

def whoami_view(request):
    return render(request, 'whoami.html')