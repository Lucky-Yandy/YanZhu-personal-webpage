

from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from django.contrib import auth

from .models import Blog, Project, AboutMe



class BlogForm(forms.ModelForm):
            class meta:
               model=Blog
               field=[ 'title','text','created',' image',]


class ProjectForm(forms.ModelForm):
            class meta:
               model=Project
               field=[ 'title','text','created',' image','field_name',]

class AboutMeForm(forms.ModelForm):
            class meta:
               model=AboutMe
               field=[ 'title','text',]


class NewUserForm(forms.Form):
           class meta:
               model=User
               field=[ 'username',' first_name','last_name','password','email ']
    
    
   





def about_me(request):
        
      sections=AboutMe.objects.all()
      # form = AboutMeForm(request.POST)
      context = {
            'sections': sections
           
        }
      return render(request,  'contact.html',  context)

  
def my_blog(request):

      sections=Blog.objects.all()
      context = {
           'sections': sections
        }
      return render(request, 'blog.html', context)
  
  
  
  
  
def my_project(request):
             
             
        sections=Project.objects.all()

        context = {
         'sections': sections
        }
        return render(request, 'project.html', context)
  
  
  
  
  
  
  

  
  
  
  
  
  
  
  
