from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
 path("", views.index, name="index" ),
 path("post/<str:slug>", views.detail, name="detail"),
 path("newnew_url", views.new_url, name="nameofnew_url"),
 path("old_url", views.old_url, name="old_url" ),
 path("contact", views.contact_view, name="contact" ),
 path("profile", views.profile, name="profile" ),
 path("about", views.about_us, name="about" ),
#  path("login",views.login,name="login"),
 path("login",auth_views.LoginView.as_view(template_name='blog/login.html'),name="login"),
 path("logout",auth_views.LogoutView.as_view(template_name='blog/logout.html'),name="logout"),
 path("register",views.register,name="register"),

]