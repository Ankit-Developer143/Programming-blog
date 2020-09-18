from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Contact,Post

from django.contrib import messages

# Create your views here.

def index(request):
   db = {"data":Post.objects.all(),
        "java":Post.objects.all().filter(title = "Java"),
        "python":Post.objects.all().filter(title = "Python")
        
        }
   
    
    
   return render(request,'blog/index.html',db)


def about(request):
    return render(request,'blog/about.html')

def contact(request):
    if request.method =="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        # print(desc,name,phone)
        
        #Fetch The Data from admin Page
        contact = Contact(name = name,email = email, phone = phone, desc =desc)
        contact.save()
        messages.add_message(request,messages.WARNING,"Succefull")
        
        
    return render(request, "blog/contact.html")

def Myblog(request):
    
   posts = Post.objects.all()
   db = {"data":Post.objects.all(),
        "java":Post.objects.all().filter(title = Java),
        "python":Post.objects.all().filter(title = Python)
        
        }
   print(java)
   return render(request,'blog/blog.html',db)
    
        
    
def java(request):
    db = {"data":Post.objects.all(),
        "java":Post.objects.all().filter(language = "Java")}
    return render(request,'blog/java.html',db)


def python(request):
    db1 = {"data":Post.objects.all(),
        "python":Post.objects.all().filter(language = "Python")}
    return render(request,'blog/python.html',db1)