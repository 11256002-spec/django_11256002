from django.urls import path
from .views import whoami_view

urlpatterns = [
    path('whoamI', whoami_view),
]
