from django import forms
from django.contrib import messages
from django.contrib.auth import models
from django.core.exceptions import ValidationError
from django.db import transaction
from userPanel.models import User,Creator,Admin,slider,found,feature,tips,subjects,community,guideline,blogs,comments,reply,contact,signup
from django.contrib.auth.forms import UserCreationForm

class creatorForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_phone = forms.CharField(required=True)
    user_location = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        if User.objects.filter(email=user.email).exists():
            raise ValidationError("Email exists")
        user.user_location = self.cleaned_data.get('user_location')
        user.user_phone = self.cleaned_data.get('user_phone')
        user.is_creator = True
        user.is_staff = True
        user.save()
        ctr = Creator.objects.create(user=user)
        ctr.user_phone = self.cleaned_data.get('user_phone')
        ctr.user_location = self.cleaned_data.get('user_location')
        ctr.save()
        return ctr
class editCreatorForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    location = forms.CharField(required=True)
    profile = forms.ImageField(required=True)

class adminForm(UserCreationForm):
    user_phone = forms.CharField(required=True)
    user_location = forms.CharField(required=True)
    email = forms.EmailField(max_length=100)
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def save(self,request):
        try:
            user = super().save(commit=False)
            user.is_admin =True
            user.is_staff = True
            user.email = self.cleaned_data.get('email')
            user.user_phone = self.cleaned_data.get('user_phone')
            user.user_location = self.cleaned_data.get('user_location')
            user.save()
            admin = Admin.objects.create(user=user)
            admin.user_phone = self.cleaned_data.get('user_phone')
            admin.user_location = self.cleaned_data.get('user_location')
            admin.save()
            return admin
        except:
            messages.error(request,"Email is not valid")

class sliderForm(forms.ModelForm):
    class Meta:
        model = slider
        fields = ['sl_title','sl_pragraph','sl_image']
        labels = {'sl_title': 'Slider Title','sl_pragraph': 'Slider Pragraph','sl_image': 'Slider Image',}

class foundForm(forms.ModelForm):
    class Meta:
        model = found
        fields = ['fnd_title','fnd_pragraph','fnd_image']
        labels = {'fnd_title':'Title','fnd_pragraph':'Pragraph','fnd_image':'Image',}

class featurForm(forms.ModelForm):
    class Meta:
        model = feature
        fields = ['feat_title','subject','feat_duration','feat_fee','feat_pragraph','feat_image','feat_cover']
        labels = {'feat_title':'Feature Title','feat_pragraph':'Feature Pragraph','feat_image':'Course File','feat_duration':"Duration",'feat_fee':"Price",'feat_cover':'Cover Image'}

class tipsForm(forms.ModelForm):
    class Meta:
        model =  tips
        fields = ['tps_title', 'tps_pragraph', 'tps_line','tps_file']
        labels = {'tps_title': 'Tips Title', 'tps_pragraph': 'Tips Pragraph', 'tps_line': 'Tips Line','tps_file':'Tips Image' }

class subjectsForm(forms.ModelForm):
    class Meta:
        model = subjects
        fields = ['sub_name','sub_fee','sub_duration','sub_details','sub_image']
        labels = {'sub_name':'Subject Name','sub_fee':'Subject Fee','sub_duration':'Subject Duration','sub_details':'Subject Details','sub_image':'Subject Image',}

class communityForm(forms.ModelForm):
    class Meta:
        model = community
        fields = ['com_name', 'com_pragraph', 'com_address','com_details','com_image']
        labels = {'com_name': 'Community Name', 'com_pragraph': 'Community Pragraph', 'com_address': 'Community Address','com_details': 'Community Details','com_image': 'Community Image'}

class guidelineForm(forms.ModelForm):
    class Meta:
        model =  guideline
        fields = ['guid_title', 'guid_pragraph','guid_file']
        labels = {'guid_title': 'Guideline Title', 'guid_pragraph': 'Guideline Pragraph','guid_file': 'Guideline File'}

class blogsForm(forms.ModelForm):
    class Meta:
        model =  blogs
        fields = ['blog_name','blog_title','blog_comment','blog_details','blog_image']
        labels = {'blog_name': 'Blog Name', 'blog_title': 'Blog Title', 'blog_comment': 'Blog Comment','blog_details': 'Blog Details','blog_image': 'Blog Image'}

class commentsForms(forms.ModelForm):
    class Meta:
        model =  comments
        fields = ['comm_person_name','comm_person_email','comm_person_website','comm_detils','comm_date','comm_time','comm_person_image','commnts_id']

class replyForm(forms.ModelForm):
    class Meta:
        model =  reply
        fields = ['rply_person_name','rply_details','rply_date','rply_time','rply_person_image','rply_id']

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['cont_person_name','cont_person_email', 'cont_person_subject','cont_person_message']
        labels = {'cont_person_name': 'Person Name', 'cont_person_email': 'Person Email', 'cont_person_subject': 'Person Subject','cont_person_message': 'Person Message'}
















