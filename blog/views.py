from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.urls import reverse
from django.contrib import messages
from .models import Post
import logging
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm 
from .forms import ContactForm,CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
# posts = [
#         {"id":1,"title":"post1","content":"content for post1"},
#         {"id":2,"title":"post2","content":"content for post2"},
#         {"id":3,"title":"post3","content":"content for post3"},
#         {"id":4,"title":"post4","content":"content for post4"},
#     ]

def index(request):
    blog_title = "Jero's Blog"
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts,5)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)

    return render(request,'blog/index.html',{"blog_title":blog_title,"posts":page_obj})

def detail(request,slug):
    #under is static
    # post = next((item for item in posts if item['id']== int(post_id)),None)
    try:
       post = Post.objects.get(slug = slug)
       related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)
    
    except Post.DoesNotExist:
        raise Http404("Post Not Found")
    
    return render(request,'blog/detail.html',{"post":post,"related_posts":related_posts}) 

def old_url(request):
    return redirect(reverse("blog:nameofnew_url"))

def new_url(request):
    return HttpResponse("In new url")

def contact_view(request):
    if request.method == "POST":
       form = ContactForm(request.POST)
       name = request.POST.get('name')
       email = request.POST.get('email')
       message = request.POST.get('message')
       logger = logging.getLogger("TESTING")
       if form.is_valid():
           success_message = "Your mail has been received successfully"
           return render(request,'blog/contact.html',{'form':form,'success_message':success_message})
       else:
           logger.debug("Post invalid")
           return render(request,'blog/contact.html',{'form':form,'name':name,'email':email,'message':message})
    return render(request,'blog/contact.html')


def about_us(request):
    return render(request,'blog/about_us.html')


def register(request):
    if request.method=="POST":
        name = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1==password2:
           user = User.objects.create_user(username=name,email=email,password=password1)
           user.is_staff = True
           user.is_superuser =True
           user.save()
           return redirect(reverse("blog:login"))
        else:
           messages.warning(request,'password mismatching')
           return redirect(reverse("blog:register"))
    else:    
       form = CreateUserForm()
       return render(request,'blog/register.html',{'form':form})
    
@login_required
def profile(request):
    return render(request,'blog/profile.html')
    

