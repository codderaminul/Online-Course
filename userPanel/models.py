from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin,AbstractBaseUser

# Create your models here.

from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_superuser(self,username,email,password,**other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_admin', False)
        other_fields.setdefault('is_user', False)
        other_fields.setdefault('is_visitor', False)
        other_fields.setdefault('is_creator', False)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Supperuser must be assign is_staff = True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assign is_superuser = True')
        return self.create_user(username,email,password,**other_fields)

    def create_user(self, username, email, password, **other_fields):
        if not username:
            raise ValueError("User must be an user name")
        if not email:
            raise ValueError("User must be an email address")
        user = self.model(username=username, email=self.normalize_email(email), **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100,default=None,unique=True)
    email = models.CharField(max_length=100, unique=True)
    user_phone = models.CharField(max_length=20,default=None,null=True,blank=True)
    user_location = models.CharField(max_length=100,default=None,null=True,blank=True)
    user_image = models.CharField(max_length=200, default="static/userPanel/files/PNG/login_image.png", null=True,blank=True)
    password = models.CharField(max_length=100)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_creator = models.BooleanField(default=False)
    is_visitor = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = CustomUserManager()
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    def __str__(self):
        return self.username

class Creator(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_phone = models.CharField(max_length=15,default=None,null=True, blank=True)
    user_location = models.CharField(max_length=100)
    user_image = models.CharField(max_length=200,default="/static/userPanel/files/PNG/login_image.png",null=True,blank=True)
    last_login = models.DateTimeField(default=None, null=True, blank=True)
    def __str__(self):
        return self.user.username

class Admin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    user_phone = models.CharField(max_length=15)
    user_location = models.CharField(max_length=100)
    last_login = models.DateTimeField(default=None,null=True,blank=True)
    def __str__(self):
        return self.user.username






class slider(models.Model):
    sl_title = models.CharField(max_length=200)
    sl_pragraph = models.TextField(max_length=500)
    sl_image = models.FileField()

class found(models.Model):
    fnd_title = models.CharField(max_length=200)
    fnd_pragraph = models.CharField(max_length=200)
    fnd_image = models.ImageField()
    user = models.CharField(max_length=50,default=None)


class all_feature(models.Model):
    feat_title = models.CharField(max_length=200)
    feat_duration = models.CharField(max_length=50, default="", null=True, blank=True)
    feat_fee = models.CharField(max_length=50, default="", null=True, blank=True)
    feat_image = models.ImageField()
    date_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    feature_id = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class tips(models.Model):
    tps_title = models.CharField(max_length=200)
    tps_pragraph = models.TextField(max_length=500)
    tps_line = models.CharField(max_length=200)
    tps_file = models.FileField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class subjects(models.Model):
    sub_name = models.CharField(max_length=50)
    sub_fee = models.CharField(max_length=50)
    sub_duration = models.CharField(max_length=50)
    sub_details = models.TextField(max_length=500)
    sub_image = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.sub_name

class feature(models.Model):
    seller_name = models.CharField(max_length=50)
    feat_title = models.CharField(max_length=200)
    subject = models.ForeignKey(subjects, on_delete=models.CASCADE,default=1, blank=True, null=True)
    feat_pragraph = models.TextField(max_length=500)
    feat_duration = models.CharField(max_length=50,default="",null=True,blank=True)
    feat_fee = models.CharField(max_length=50,default="",null=True,blank=True)
    feat_image = models.FileField(max_length=250,default=None)
    feat_cover = models.ImageField(max_length=250,default=None)
    date_time = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class community(models.Model):
    com_name = models.CharField(max_length=50)
    com_pragraph = models.TextField(max_length=500)
    com_address = models.CharField(max_length=150)
    com_details = models.TextField(max_length=500)
    com_image = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class guideline(models.Model):
    guid_title = models.CharField(max_length=200)
    guid_pragraph = models.TextField(max_length=500)
    guid_file = models.FileField()
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class blogs(models.Model):
    blog_name =  models.CharField(max_length=50)
    blog_title =  models.CharField(max_length=200)
    blog_details =  models.TextField(max_length=1500)
    blog_comment = models.CharField(max_length=500)
    blog_image = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class comments(models.Model):
    comm_person_name =  models.CharField(max_length=50)
    comm_person_email =  models.EmailField(max_length=150)
    comm_person_website =  models.URLField()
    comm_detils =  models.TextField(max_length=500)
    comm_date =  models.DateField()
    comm_time =  models.TimeField()
    comm_person_image = models.ImageField()
    commnts_id = models.ForeignKey(blogs,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class reply(models.Model):
    rply_person_name = models.CharField(max_length=50)
    rply_details = models.TextField(max_length=500)
    rply_date = models.DateField()
    rply_time = models.TimeField()
    rply_person_image = models.ImageField()
    rply_id = models.ForeignKey(comments, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class contact(models.Model):
    cont_person_name = models.CharField(max_length=50)
    cont_person_email = models.EmailField(max_length=150)
    cont_person_subject = models.CharField(max_length=50)
    cont_person_message = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class signup(models.Model):
    fst_name = models.CharField(max_length=50)
    lst_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    usr_email = models.CharField(max_length=50)
    usr_pass = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=None)
    is_active = models.BooleanField(default=None)

'''
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
'''

'''
class CustomUserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not username:
            raise ValueError("User must be an user name")
        if not email:
            raise ValueError("User must be an email address")
        user = self.model(
            username = username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,username,email,password=None):
        user = self.create_user(
            username=username,
            email = email,
            password=password,
        )
        user.is_staff = True
        user.is_actve = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100,default=None,unique=True)
    email = models.CharField(max_length=100, unique=True)
    user_phone = models.CharField(max_length=20,default=None,null=True,blank=True)
    user_location = models.CharField(max_length=100,default=None,null=True,blank=True)
    password = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    is_creator = models.BooleanField(default=False)
    is_visitor = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    user_image = models.ImageField(max_length=100, default=None, null=True, blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = CustomUserManager()
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    def __str__(self):
        return self.username



class MyCreator(models.Model):
    user = models.OneToOneField(MyUser,on_delete=models.CASCADE)
    user_phone = models.CharField(max_length=15,default=None,null=True, blank=True)
    user_location = models.CharField(max_length=100)
    user_image = models.CharField(max_length=200,default="static/userPanel/files/PNG/login_image.png",null=True,blank=True)
    last_login = models.DateTimeField(default=None, null=True, blank=True)
    def __str__(self):
        return self.user.username
'''
'''
class MyAdmin(models.Model):
    user = models.OneToOneField(MyUser,on_delete=models.CASCADE,primary_key=True)
    user_phone = models.CharField(max_length=15)
    user_location = models.CharField(max_length=100)
    last_login = models.DateTimeField(default=None,null=True,blank=True)
    def __str__(self):
        return self.user.username
'''