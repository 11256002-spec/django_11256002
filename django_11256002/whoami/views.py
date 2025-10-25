from django.shortcuts import render
from whoami.views import whoami_view

def whoami_view(request):
    return render(request, 'whoami.html')
