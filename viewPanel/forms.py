from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.db import transaction
from userPanel.models import User
from viewPanel.models import Customer


class customerForm(UserCreationForm):
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
        user.is_user = True
        user.is_staff = False
        user.save()
        ctr = Customer.objects.create(user=user)
        ctr.user_phone = self.cleaned_data.get('user_phone')
        ctr.user_location = self.cleaned_data.get('user_location')
        ctr.save()
        return ctr


