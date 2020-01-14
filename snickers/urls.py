from django.urls import path
from .views import HomePageView, AboutPageView

#wants a string for a path
#1st param - blank mean root of the site
#2nd param - view, make sure to import path
#3rd param - optional, best practices to have it with no conflicting names
urlpatterns = [
    #use .as_view() will return a function itself. Higher order function; for classes
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]