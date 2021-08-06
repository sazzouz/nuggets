from .views import Home, search
from django.urls import path, include

urlpatterns = [
    path('', Home.as_view(), kwargs={'sample': 'sample value'}, name='home'),
    path('search/', search, name='search')
]
