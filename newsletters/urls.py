from django.urls import path
from .views import newsletter_unsubscribe
from .views import HomeView
app_name ='newsletters'
urlpatterns =[
    path('',HomeView.as_view(), name='home'),
    path('unsubscribe/',newsletter_unsubscribe, name='unsubscribe'),
]