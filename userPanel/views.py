import datetime
import os

from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import PasswordChangeView
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from userPanel.decorator import unauthenticated_user
from userPanel.forms import adminForm, creatorForm, sliderForm, foundForm, featurForm, tipsForm, subjectsForm, \
    communityForm, guidelineForm, blogsForm, contactForm, editCreatorForm
from userPanel.models import slider, found, feature, tips, subjects, community, guideline, blogs, contact, Creator, \
    Admin, all_feature
from userPanel.setup import file_save, handle_JPEG_image_file, handle_JPG_image_file, handle_VIDEO_file, extention, \
    parmanent_file
from django.contrib import messages
from django.contrib.auth.models import auth
from userPanel.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from userPanel.forms import adminForm, creatorForm, sliderForm, foundForm, featurForm, tipsForm, subjectsForm, \
    communityForm, guidelineForm, blogsForm, contactForm, editCreatorForm
from userPanel.models import *
from userPanel.setup import file_save, handle_JPEG_image_file, handle_JPG_image_file, handle_VIDEO_file,extention
from django.contrib import messages, auth
from django.contrib.auth.models import auth
from userPanel.models import User
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import CreateView

# Create your views here.


fs = FileSystemStorage()

class Creator_SignUp(CreateView):
    model = User
    form_class = creatorForm
    template_name = 'html/set_page/creator_signup.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'ctr'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        if form.is_valid():
            user = form.save()
            login(self.request,user)
            return redirect("login")
        else:
            messages.error(self.request,"Form is not valid")

'''
def Creator_SignUp(request):
    if request.method == 'POST':
        info = creatorForm(request.POST)
        if info.is_valid():
            get_email = request.POST['email']
            if User.objects.filter(email=get_email).exists():
                messages.error(request,"Email already exists")
                return redirect("singup")
            else:
                info.save()
                info.is_creator = True
                info.is_staff = True
                info.save()
                ctr = Creator.objects.create(user=info)
                ctr.user_phone = request.cleaned_data.get('user_phone')
                ctr.user_location = request.cleaned_data.get('user_location')
                ctr.save()
                messages.success(request,"Create new account successfully")
    form = creatorForm()
    return render(request,'html/set_page/creator_signup.html',{"form":form})
'''


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_creator:
            auth.login(request, user)
            return redirect("dashboard")
        else:
            auth.logout(request)
            return redirect('creator_login')
    else:
        return render(request, 'html/set_page/login.html')
def LogOut(request):
    auth.logout(request)
    return redirect('creator_login')


def Permission(request):
    if request.user.is_creator is True:
        auth.login(request, request.user)
    else:
        auth.logout(request)
        return redirect("/creator_login/")

class MyPasswordChangeView(PasswordChangeView):
    template_name = 'html/set_page/creator_pass_change.html'
    success_url = reverse_lazy('creator_profile_set')

@login_required(login_url='creator_login')
def Creator_Profile_show(request):
    user_details = User.objects.get(username = request.user.username)
    creatpr_details = Creator.objects.get(user_id = request.user.id)
    context = {
        'user' : user_details,
        'creatpr' : creatpr_details,
    }
    return render(request, 'html/set_page/profile.html',context)
@login_required(login_url='creator_login')
def Creator_Profile_edit(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['user_phone']
        location = request.POST['user_location']

        #path = file_save(request.FILES['user_image'], extention(request.FILES['user_image']))

        request.user.first_name = firstname
        request.user.last_name = lastname
        request.user.username = username
        request.user.email = email
        request.user.user_phone = phone
        request.user.user_location = location
        request.user.save()
        creator_data = Creator.objects.get(user_id=request.user.id)
        creator_data.user_phone = phone
        creator_data.user_location = location

        try:
            if request.FILES['user_image']:
                deltPath = "userPanel" + creator_data.user_image
                fs.delete(deltPath)
                path = file_save(request.FILES['user_image'], extention(request.FILES['user_image']))
                creator_data.user_image = path
                request.user.user_image = path
                request.user.save()
        except:
            pass
        #creator_data.user_image = path
        creator_data.save()
        return redirect("creator_profile_show")
    user_data = User.objects.get(id=request.user.id)
    creator_data = Creator.objects.get(user_id = request.user.id)
    context = {
        'user_data':user_data,
        'creator_data':creator_data,
    }
    return render(request, 'html/set_page/edit_profile.html',context)
@login_required(login_url='creator_login')
def Creator_Profile_set(request):
    return render(request, 'html/set_page/set_profile.html')

@login_required(login_url='creator_login')
def Dashboard(request):
    return render(request, 'html/set_page/index.html')

@login_required(login_url='creator_login')
def setSlider(request):

        if request.method == 'POST':
            data = sliderForm(request.POST, request.FILES)
            if data.is_valid():
                title = request.POST['sl_title']
                pragraph = request.POST['sl_pragraph']
                path = file_save(request.FILES['sl_image'], extention(request.FILES['sl_image']))
                if path != False:
                    catch = slider(sl_title=title,sl_pragraph=pragraph,sl_image=path)
                    catch.save()
                    messages.success(request,'Save Successfully')
                    return redirect("view_slider")

        form = sliderForm()
        return render(request, 'html/set_page/set_slider.html',{'form':form})
@login_required(login_url='creator_login')
def viewSlider(request):
    all = slider.objects.all()
    return render(request,'html/view_page/slider.html',{"record":all})
@login_required(login_url='creator_login')
def updateSlider(request,id):
    item = slider.objects.get(id=id)
    file = sliderForm(instance=item)
    if request.method == "POST":
        title = request.POST['sl_title']
        pragraph = request.POST['sl_pragraph']
        item.sl_title = title
        item.sl_pragraph = pragraph
        try:
            if request.FILES['sl_image']:
                deltPath = "userPanel" + item.sl_image.name
                fs.delete(deltPath)
                path = file_save(request.FILES['sl_image'], extention(request.FILES['sl_image']))
                item.sl_image = path
        except:
            pass
        item.save()
        messages.success(request, "Update Successfully")
        return redirect("view_slider")
    return render(request,'html/update_page/up_slider.html',{"form":file,"id":id})
@login_required(login_url='creator_login')
def delSlider(request,id):
    try:
        data = slider.objects.get(id=id)
        deltPath = "userPanel" + data.sl_image.name
        fs.delete(deltPath)
        data.delete()
        messages.success(request, "Delete Successfully")
        return redirect("/userPanel/view_slider/")
    except:
        try:
            data = slider.objects.get(id=id)
            data.delete()
            messages.success(request, "Only Text Delete")
            return redirect("/userPanel/view_slider/")
        except:
            return redirect("/userPanel/view_slider/")

@login_required(login_url='creator_login')
def setFound(request):

    if request.method == 'POST':
        data = foundForm(request.POST, request.FILES)
        if data.is_valid():
            title = request.POST['fnd_title']
            pragraph = request.POST['fnd_pragraph']
            path = file_save(request.FILES['fnd_image'], extention(request.FILES['fnd_image']))
            if path != False:
                catch = found(fnd_title=title,fnd_pragraph=pragraph,fnd_image=path,user=request.user.id)
                catch.save()
                messages.success(request,"Save Successfully")
                return redirect("view_found")

    form = foundForm()
    return render(request, 'html/set_page/set_found.html',{'form':form})
@login_required(login_url='creator_login')
def viewFound(request):
    all = found.objects.filter(user=request.user.id)
    return render(request,'html/view_page/found.html',{"record":all})
@login_required(login_url='creator_login')
def updateFound(request,id):
    item = found.objects.get(id=id)
    file = foundForm(instance=item)
    if request.method == "POST":
        title = request.POST['fnd_title']
        pragraph = request.POST['fnd_pragraph']
        item.fnd_title = title
        item.fnd_pragraph = pragraph
        try:
            if request.FILES['fnd_image']:
                deltPath = "userPanel" + item.fnd_image.name
                fs.delete(deltPath)
                path = file_save(request.FILES['fnd_image'], extention(request.FILES['fnd_image']))
                item.fnd_image = path
        except:
            pass
        item.save()
        messages.success(request, "Update Successfully")
        return redirect("view_found")
    return render(request,'html/update_page/up_found.html',{"form":file,"id":id})
@login_required(login_url='creator_login')
def delFound(request,id):
    try:
        data = found.objects.get(id=id)
        deltPath = "userPanel" + data.fnd_image.name
        fs.delete(deltPath)
        data.delete()
        messages.success(request, "Delete Successfully")
        return redirect("view_found")
    except:
        try:
            data = found.objects.get(id=id)
            data.delete()
            messages.success(request, "Only Text Delete")
            return redirect("view_found")
        except:
            return redirect("view_found")

@login_required(login_url='creator_login')
def setFeature(request):
    try:
        if request.method == 'POST':
            data = featurForm(request.POST, request.FILES)
            if data.is_valid():
                title = request.POST['feat_title']
                pragraph = request.POST['feat_pragraph']
                duration = request.POST['feat_duration']
                fee = request.POST['feat_fee']
                subject = int(request.POST.get('subject'))
                path = file_save(request.FILES['feat_image'], extention(request.FILES['feat_image']))
                path2 = file_save(request.FILES['feat_cover'], extention(request.FILES['feat_cover']))
                if path != False:
                    catch = feature(seller_name=request.user.username,subject_id=subject,feat_title=title,feat_duration=duration,feat_fee=fee,feat_pragraph=pragraph,feat_image=path,feat_cover=path2,user_id=request.user.id)
                    catch.save()
                    messages.success(request,"Save Successfully")
                    return redirect("view_feature")
    except:
        messages.error(request, "Invalid Input")
        return redirect("set_feature")
    form = featurForm()
    return render(request, 'html/set_page/set_feature.html',{'form':form})
@login_required(login_url='creator_login')
def viewFeature(request):
    all = feature.objects.filter(user_id=request.user.id)
    return render(request,'html/view_page/feature.html',{"record":all})
@login_required(login_url='creator_login')
def updateFeature(request,id):
    item = feature.objects.get(id=id)
    file = featurForm(instance=item)
    if request.method == "POST":
        title = request.POST['feat_title']
        duration = request.POST['feat_duration']
        fee = request.POST['feat_fee']
        pragraph = request.POST['feat_pragraph']
        subject = request.POST.get('subject')
        item.feat_title = title
        item.feat_duration = duration
        item.feat_fee = fee
        item.feat_pragraph = pragraph
        item.subject_id = subject
        item.date_time = datetime.datetime.now()
        try:
            if request.FILES['feat_image']:
                deltPath = "userPanel" + item.feat_image.name
                fs.delete(deltPath)
                path = file_save(request.FILES['feat_image'], extention(request.FILES['feat_image']))
                item.feat_image = path
        except:
            pass
        try:
            if request.FILES['feat_cover']:
                deltPath = "userPanel" + item.feat_image.name
                fs.delete(deltPath)
                path2 = file_save(request.FILES['feat_cover'], extention(request.FILES['feat_cover']))
                item.feat_cover = path2
        except:
            pass
        item.save()
        messages.success(request, "Update Successfully")
        return redirect("view_feature")
    return render(request,'html/update_page/up_feature.html',{"form":file,"id":id})

'''
@login_required(login_url='login')
def delFeature(request,id):
    try:
        data = feature.objects.get(id=id)
        deltPath = "userPanel" + data.feat_image.name
        fs.delete(deltPath)
        data.delete()
        messages.success(request, "Delete Successfully")
        return redirect("view_feature")
    except:
        try:
            data = feature.objects.get(id=id)
            data.delete()
            messages.success(request, "Only Text Delete")
            return redirect("view_feature")
        except:
            return redirect("view_feature")
'''

@login_required(login_url='creator_login')
def setTips(request):
    try:
        if request.method == 'POST':
            data = tipsForm(request.POST, request.FILES)
            if data.is_valid():
                title = request.POST['tps_title']
                pragraph = request.POST['tps_pragraph']
                line = request.POST['tps_line']
                path = file_save(request.FILES['tps_file'], extention(request.FILES['tps_file']))
                if path != False:
                    catch = tips(tps_title=title,tps_pragraph=pragraph,tps_line=line,tps_file=path,user_id=request.user.id)
                    catch.save()
                    messages.success(request,"Save Successfully")
                    return redirect("view_tips")
    except:
        messages.error(request, "Invalid Input Tips Form")
        return redirect("set_tips")
    form = tipsForm()
    return render(request, 'html/set_page/set_tips.html',{'form':form})
@login_required(login_url='creator_login')
def viewTips(request):
    all = tips.objects.filter(user_id=request.user.id)
    return render(request,'html/view_page/tips.html',{"record":all})
@login_required(login_url='creator_login')
def updateTips(request,id):
    item = tips.objects.get(id=id)
    file = tipsForm(instance=item)
    if request.method == "POST":
        title = request.POST['tps_title']
        pragraph = request.POST['tps_pragraph']
        line = request.POST['tps_line']
        item.tps_title = title
        item.tps_pragraph = pragraph
        item.tps_line = line
        try:
            if request.FILES['tps_file']:
                deltPath = "userPanel" + item.tps_file.name
                fs.delete(deltPath)
                path = file_save(request.FILES['tps_file'], extention(request.FILES['tps_file']))
                item.tps_file = path
        except:
            pass
        item.save()
        messages.success(request, "Update Successfully")
        return redirect("view_tips")
    return render(request,'html/update_page/up_tips.html',{"form":file,"id":id})
@login_required(login_url='creator_login')
def delTips(request,id):
    try:
        data = tips.objects.get(id=id)
        deltPath = "userPanel" + data.tps_file.name
        fs.delete(deltPath)
        data.delete()
        messages.success(request, "Delete Successfully")
        return redirect("view_tips")
    except:
        try:
            data = tips.objects.get(id=id)
            data.delete()
            messages.success(request, "Only Text Delete")
            return redirect("view_tips")
        except:
            return redirect("view_tips")

@login_required(login_url='creator_login')
def setSubject(request):
    try:
        if request.method == 'POST':
            data = subjectsForm(request.POST, request.FILES)
            if data.is_valid():
                name = request.POST['sub_name']
                fee = request.POST['sub_fee']
                duration = request.POST['sub_duration']
                details = request.POST['sub_details']
                path = file_save(request.FILES['sub_image'], extention(request.FILES['sub_image']))
                if path != False:
                    catch = subjects(sub_name=name,sub_fee=fee,sub_duration=duration,sub_details=details,sub_image=path,user_id=request.user.id)
                    catch.save()
                    messages.success(request,"Save Successfully")
                    return redirect("view_subject")
    except:
        messages.error(request, "Invalid Input")
        return redirect("set_subject")
    form = subjectsForm()
    return render(request, 'html/set_page/set_subject.html',{'form':form})
@login_required(login_url='creator_login')
def viewSubject(request):
    all = subjects.objects.filter(user_id=request.user.id)
    return render(request,'html/view_page/subject.html',{"record":all})
@login_required(login_url='creator_login')
def updateSubject(request,id):
    item = subjects.objects.get(id=id)
    file = subjectsForm(instance=item)
    if request.method == "POST":
        name = request.POST['sub_name']
        fee = request.POST['sub_fee']
        duration = request.POST['sub_duration']
        details = request.POST['sub_details']
        item.sub_name = name
        item.sub_fee = fee
        item.sub_duration = duration
        item.sub_details = details
        try:
            if request.FILES['sub_image']:
                deltPath = "userPanel" + item.sub_image.name
                fs.delete(deltPath)
                path = file_save(request.FILES['sub_image'], extention(request.FILES['sub_image']))
                item.sub_image = path
        except:
            pass
        item.save()
        messages.success(request, "Update Successfully")
        return redirect("view_subject")
    return render(request,'html/update_page/up_subject.html',{"form":file,"id":id})
@login_required(login_url='creator_login')
def delSubject(request,id):
    try:
        data = subjects.objects.get(id=id)
        deltPath = "userPanel" + data.sub_image.name
        fs.delete(deltPath)
        data.delete()
        messages.success(request, "Delete Successfully")
        return redirect("view_subject")
    except:
        try:
            data = subjects.objects.get(id=id)
            data.delete()
            messages.success(request, "Only Text Delete")
            return redirect("view_subject")
        except:
            return redirect("view_subject")

@login_required(login_url='creator_login')
def setCommunity(request):
    try:
        if request.method == 'POST':
            data = communityForm(request.POST, request.FILES)
            if data.is_valid():
                name = request.POST['com_name']
                pragraph = request.POST['com_pragraph']
                address = request.POST['com_address']
                details = request.POST['com_details']
                path = file_save(request.FILES['com_image'], extention(request.FILES['com_image']))
                if path != False:
                    catch = community(com_name=name,com_pragraph=pragraph,com_address=address,com_details=details,com_image=path,user_id=request.user.id)
                    catch.save()
                    messages.success(request,"Save Successfully")
                    return redirect("view_community")
    except:
        messages.error(request, "Invalid Input")
        return redirect("set_community")
    form = communityForm()
    return render(request, 'html/set_page/set_community.html',{'form':form})
@login_required(login_url='creator_login')
def viewCommunity(request):
    all = community.objects.filter(user_id=request.user.id)
    return render(request,'html/view_page/community.html',{"record":all})
@login_required(login_url='creator_login')
def updateCommunity(request,id):
    item = community.objects.get(id=id)
    file = communityForm(instance=item)
    if request.method == "POST":
        name = request.POST['com_name']
        pragraph = request.POST['com_pragraph']
        address = request.POST['com_address']
        details = request.POST['com_details']
        item.com_name = name
        item.com_pragraph = pragraph
        item.com_address = address
        item.com_details = details
        try:
            if request.FILES['com_image']:
                deltPath = "userPanel" + item.com_image.name
                fs.delete(deltPath)
                path = file_save(request.FILES['com_image'], extention(request.FILES['com_image']))
                item.com_image = path
        except:
            pass
        item.save()
        messages.success(request, "Update Successfully")
        return redirect("view_community")
    return render(request,'html/update_page/up_community.html',{"form":file,"id":id})
@login_required(login_url='creator_login')
def delCommunity(request,id):
    try:
        data = community.objects.get(id=id)
        deltPath = "userPanel" + data.com_image.name
        fs = FileSystemStorage()
        fs.delete(deltPath)
        data.delete()
        messages.success(request, "Delete Successfully")
        return redirect("view_community")
    except:
        try:
            data = community.objects.get(id=id)
            data.delete()
            messages.success(request, "Only Text Delete")
            return redirect("view_community")
        except:
            return redirect("view_community")

@login_required(login_url='creator_login')
def setGuideline(request):
    try:
        if request.method == 'POST':
            data = guidelineForm(request.POST, request.FILES)
            if data.is_valid():
                title = request.POST['guid_title']
                pragraph = request.POST['guid_pragraph']
                is_file = file_save(request.FILES['guid_file'], extention(request.FILES['guid_file']))
                if is_file != False:
                    catch = guideline(guid_title=title,guid_pragraph=pragraph,guid_file=is_file,user_id=request.user.id)
                    catch.save()
                    messages.success(request,"Save Successfully")
                    return redirect("view_guideline")
    except:
        messages.error(request, "Invalid Input")
        return redirect("set_guideline")
    form = guidelineForm()
    return render(request, 'html/set_page/set_guideline.html',{'form':form})
@login_required(login_url='creator_login')
def viewGuideline(request):
    all = guideline.objects.filter(user_id=request.user.id)
    return render(request,'html/view_page/guideline.html',{"record":all})
@login_required(login_url='creator_login')
def updateGuideline(request,id):
    item = guideline.objects.get(id=id)
    file = guidelineForm(instance=item)
    if request.method == "POST":
        title = request.POST['guid_title']
        pragraph = request.POST['guid_pragraph']
        item.guid_title = title
        item.guid_pragraph = pragraph
        try:
            if request.FILES['guid_file']:
                fs.delete("userPanel" + item.guid_file.name)
                item.guid_file = file_save(request.FILES['guid_file'], extention(request.FILES['guid_file']))
        except:
            pass
        item.save()
        messages.success(request, "Update Successfully")
        return redirect("view_guideline")
    return render(request,'html/update_page/up_guideline.html',{"form":file,"id":id})
@login_required(login_url='creator_login')
def delGuideline(request,id):
    try:
        data = guideline.objects.get(id=id)
        deltPath = "userPanel" + data.guid_file.name
        fs.delete(deltPath)
        data.delete()
        messages.success(request, "Delete Successfully")
        return redirect("view_guideline")
    except:
        try:
            data = guideline.objects.get(id=id)
            data.delete()
            messages.success(request, "Only Text Delete")
            return redirect("view_guideline")
        except:
            return redirect("view_guideline")

@login_required(login_url='creator_login')
def setBlog(request):
    try:
        if request.method == 'POST':
            data = blogsForm(request.POST, request.FILES)
            if data.is_valid():
                name = request.POST['blog_name']
                title = request.POST['blog_title']
                comment = request.POST['blog_comment']
                details = request.POST['blog_details']
                path = file_save(request.FILES['blog_image'], extention(request.FILES['blog_image']))
                if path != False:
                    catch = blogs(blog_name=name,blog_title=title,blog_comment=comment,blog_details=details,blog_image=path,user_id=request.user.id)
                    catch.save()
                    messages.success(request,"Save Successfully")
                    return redirect("view_blog")
    except:
        messages.error(request, "Invalid Input")
        return redirect("set_blog")
    form = blogsForm()
    return render(request, 'html/set_page/set_blog.html',{'form':form})
@login_required(login_url='creator_login')
def viewBlog(request):
    all = blogs.objects.filter(user_id=request.user.id)
    return render(request,'html/view_page/blog.html',{"record":all})
@login_required(login_url='creator_login')
def updateBlog(request,id):
    item = blogs.objects.get(id=id)
    file = blogsForm(instance=item)
    if request.method == "POST":
        name = request.POST['blog_name']
        title = request.POST['blog_title']
        comment = request.POST['blog_comment']
        details = request.POST['blog_details']
        item.blog_name = name
        item.blog_title = title
        item.blog_comment = comment
        item.blog_details = details
        try:
            if request.FILES['blog_image']:
                fs.delete("userPanel" + item.blog_image.name)
                item.blog_image = file_save(request.FILES['blog_image'], extention(request.FILES['blog_image']))
        except:
            pass
        item.save()
        messages.success(request, "Update Successfully")
        return redirect("view_blog")
    return render(request,'html/update_page/up_blog.html',{"form":file,"id":id})
@login_required(login_url='creator_login')
def delBlog(request,id):
    try:
        data = blogs.objects.get(id=id)
        deltPath = "userPanel" + data.blog_image.name
        fs.delete(deltPath)
        data.delete()
        messages.success(request, "Delete Successfully")
        return redirect("view_blog")
    except:
        try:
            data = blogs.objects.get(id=id)
            data.delete()
            messages.success(request, "Only Text Delete")
            return redirect("view_blog")
        except:
            return redirect("view_blog")

@login_required(login_url='creator_login')
def setContact(request):
    try:
        if request.method == 'POST':
            data = contactForm(request.POST)
            if data.is_valid():
                name = request.POST['cont_person_name']
                email = request.POST['cont_person_email']
                subject = request.POST['cont_person_subject']
                message = request.POST['cont_person_message']
                catch = contact(cont_person_name=name,cont_person_email=email,cont_person_subject=subject,cont_person_message=message,user_id=request.user.id)
                catch.save()
                messages.success(request,"Save Successfully")
                return redirect("view_contact")
    except:
        messages.error(request, "Invalid Input")
        return redirect("set_contact")
    form = contactForm()
    return render(request, 'html/set_page/set_contact.html',{'form':form})
@login_required(login_url='creator_login')
def viewContact(request):
    all = contact.objects.filter(user_id=request.user.id)
    return render(request,'html/view_page/contact.html',{"record":all})
@login_required(login_url='creator_login')
def updateContact(request,id):
    item = contact.objects.get(id=id)
    file = contactForm(instance=item)
    if request.method == "POST":
        name = request.POST['cont_person_name']
        email = request.POST['cont_person_email']
        subject = request.POST['cont_person_subject']
        message = request.POST['cont_person_message']
        item.cont_person_name = name
        item.cont_person_email = email
        item.cont_person_subject = subject
        item.cont_person_message = message
        item.save()
        messages.success(request, "Update Successfully")
        return redirect("view_contact")
    return render(request,'html/update_page/up_contact.html',{"form":file,"id":id})
@login_required(login_url='creator_login')
def delContact(request,id):
        data = contact.objects.get(id=id)
        data.delete()
        messages.success(request, "Delete Successfully")
        return redirect("view_blog")


@login_required(login_url='creator_login')
def calender(request):
    return render(request,'html/view_page/calender.html')

@login_required(login_url='creator_login')
def chat(request):
    return render(request, 'html/view_page/chat.html')

@login_required(login_url='creator_login')
def invoice(request):
    return render(request,'html/view_page/invoice.html')

