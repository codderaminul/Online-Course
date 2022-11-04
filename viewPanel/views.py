import mimetypes
import os
import uuid
from wsgiref.util import FileWrapper
from django.contrib import auth, messages
from django.contrib.auth.models import auth
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import StreamingHttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from userPanel.models import guideline, feature, subjects, community, found, blogs, User
from viewPanel.forms import customerForm
# Create your views here.
from viewPanel.models import ByCourse


class Customer_SignUp(CreateView):
    model = User
    form_class = customerForm
    template_name = 'view_file/register.html'
    '''
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'ctr'
        return super().get_context_data(**kwargs)
    '''
    def form_valid(self, form):
        if form.is_valid():
            user = form.save()
            messages.success(self.request,"Create Account Successfully")
            return redirect("view_login")
        else:
            messages.error(self.request, "Form is not valid")

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_user:
            auth.login(request, user)
            return redirect("home")
        else:

            messages.error(request, "Username or Password not match")
            return render(request, 'view_file/login.html')
    else:
        return render(request, 'view_file/login.html')

def LogOut(request):
    auth.logout(request)
    return redirect('home')


def homePage(request):
    guide = guideline.objects.all()[:3]
    featr = feature.objects.all()
    subject = subjects.objects.all()
    commu = community.objects.all()
    fnd = found.objects.all()[:1]


    context = {
        'guidelines':guide,
        'features':featr,
        'subjects':subject,
        'community':commu,
        'found':fnd,
    }
    return render(request,'view_file/index.html',context)


def aboutPage(request):
    guide = guideline.objects.all()[:3]
    featr = feature.objects.all()
    subject = subjects.objects.all()
    commu = community.objects.all()
    fnd = found.objects.all()
    context = {
        'guidelines': guide,
        'features': featr,
        'subjects': subject,
        'community': commu,
        'found': fnd,
    }
    return render(request,'view_file/about.html',context)


def blogPage(request):
    all_blog = blogs.objects.all()
    course = feature.objects.all()
    blog = blogs.objects.all()[:9]
    context = {

        'recent_course': course,
        'recent_blog': blog,
        'blogs': all_blog
    }

    return render(request,'view_file/blog.html',context)


def blogDetailsPage(request,id):
    blog = blogs.objects.get(id=id)
    course = feature.objects.all()
    blog = blogs.objects.all()[:9]
    context = {
        'blog': blog,
        'recent_course': course,
        'recent_blog': blog,
    }
    return render(request,'view_file/blog_details.html',context)


def contactPage(request):
    return render(request,'view_file/contact.html')

def coursePage(request):
    guide = guideline.objects.all()[:3]
    featr = feature.objects.all()
    subject = subjects.objects.all()

    context = {
        'guidelines': guide,
        'features': featr,
        'subjects': subject,
    }
    return render(request,'view_file/course.html',context)

def course_detailsPage(request,id):
    featr = feature.objects.get(id=id)
    course = feature.objects.all()
    blog = blogs.objects.all()
    context={
        'feature' : featr,
        'recent_course':course,
        'recent_blog':blog,
    }
    return render(request, 'view_file/course_details.html',context)

def checkoutPage(request,id):
    if request.method == 'POST':
       check = ByCourse.objects.filter(course_id=id)
       if not check:
           saveCourse =  ByCourse(customer_id=request.user.id,course_id=id)
           saveCourse.save()
           messages.success(request,"Add Successfully")
           return redirect('profile')
       messages.success(request,"Course Already Added")

    featr = feature.objects.get(id=id)
    context = {
        "delivary":featr,
    }
    return render(request, 'view_file/checkout.html',context)

def profilePage(request):
    my_course = ByCourse.objects.filter(customer_id = request.user.id)
    course_list = []
    for course in my_course:
        course_list.append(int(course.course_id))
    all_course = feature.objects.filter(id__in = course_list)
    return render(request,'view_file/profile.html',{"my_course":all_course})

def Chat(request,id):
    return render(request,'view_file/chat.html')
