
from django.shortcuts import render, reverse
from django.shortcuts import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from blo.models import Categery, Blog, Author
from django.contrib.auth.models import User


@login_required(login_url='/login')
def index(request):
    categerys = Categery.objects.all()
    blogs = Blog.objects.all()
    
    context={
       "title":"Blog",
       "categerys": categerys,
       "blogs" : blogs
    }

    return render(request, "index.html", context=context)

@login_required(login_url='/login')
def category(request,id):
    category = Categery.objects.get(id=id)
    categerys = Categery.objects.all()
    blogs = Blog.objects.filter(categery = category)
    
    context={
       "title":"Blog",
       "categerys": categerys,
       "blogs" : blogs
    }

    return render(request, "index.html", context=context)


@login_required(login_url='/login')
def account(request):
    user = request.user
    author = Author.objects.get(user=user)

    blogs = Blog.objects.filter(author = author)

    context={
       "title":"Blog",
       "blogs":blogs
    }


    return render(request, "account.html",context=context)


@login_required(login_url='/login')
def blog(request,id):
    blog = Blog.objects.get(id=id)
    blogs = Blog.objects.all()[:4]
    
    context={
       "title":"Blog",
       "blog" : blog,
       "blogs":blogs,
    }

    return render(request, "blog.html", context=context)

@login_required(login_url='/login')
def create(request):
    user = request.user
    author = Author.objects.get(user=user)
    if request.method =='POST':
       title = request.POST.get('title')
       image = request.FILES.get('image')
       short_description = request.POST.get('short_description')
       categery = request.POST.get('categery')
       description = request.POST.get('description')

       categery = Categery.objects.get(id=categery)

       blog = Blog.objects.create(
           title = title,
           image = image,
           short_description = short_description,
           description = description,
           author = author,
           categery=categery

       )

       blog.save()

       return HttpResponseRedirect(reverse('blo:account'))
    
    else :
       categories = Categery.objects.all()
       context = {
           "title":"Create Blog",
           "categories": categories
       }

       return render(request, "create.html",context=context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")


        if username and password:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    auth_login(request, user)

                    return HttpResponseRedirect(reverse("blo:index"))
                
                else:
                    context ={
                        "title":"Login",
                        "error":True,
                        "message":"invalid credentials"
                    }

                return render(request, "login.html", context=context)
    
    else:
        context ={
            "title":"Login",
        }
        return render(request, "login.html", context=context)
    

def logout(request):
  
    auth_logout(request)

    return HttpResponseRedirect(reverse("blo:login"))




def register(request):
    if request.method == 'POST':
       username = request.POST.get("username")
       first_name = request.POST.get("first_name")
       last_name = request.POST.get("last_name")
       password = request.POST.get("password")

       user = User.objects.create_user(
           username = username,
           first_name = first_name,
           last_name = last_name,
           password = password

       )

       user.save()

       author = Author.objects.create(
           user=user
       )

       author.save()

       return HttpResponseRedirect(reverse("blo:login"))
    
    else:
       context={
           "title":"Create account",
       }
    
       return render(request, "register.html", context=context)


@login_required(login_url='/login')
def blog_del(request, id):
  
    blog = Blog.objects.get(id=id)
    blog.delete()

    return HttpResponseRedirect(reverse("blo:account"))




@login_required(login_url='/login')
def blog_edit(request, id):
  
    blog = Blog.objects.get(id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        short_description =request.POST.get('short_description')
        categery = request.POST.get('categery')
        description = request.POST.get('description')

        categery= Categery.objects.get(id=categery)

        blog.title = title
        blog.image = image

        blog.save()

        return HttpResponseRedirect(reverse("blo:account"))

    else :
       categories = Categery.objects.all()
       context = {
           "title":"Create Blog",
           "categories": categories
       }

       return render(request, "create.html",context=context)



    


