from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name = 'Home'),
    path('about/',views.about,name = 'About'),
    path('contact/',views.contact,name = 'contact'),
    path('Myblog/',views.Myblog,name = 'blog'),
    path('java/',views.java,name = 'java'),
    path('python/',views.python,name = 'python')
    
]