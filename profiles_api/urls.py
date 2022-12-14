from django.urls import path
from profiles_api import views

urlpatterns=[
    ## to convert class to view -- as_view
    path('hello-view/',views.HelloApiView.as_view()),
]