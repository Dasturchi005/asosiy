from django.urls import path
from .views import home ,about
urlpatterns=[
    path('about/', about.as_view(), name='about'),
    path('',home.as_view(),name='home'),
]