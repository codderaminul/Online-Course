from django.contrib import admin
from userPanel.models import feature,blogs,comments,community,contact,signup,slider,tips,subjects,Creator,Admin,User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class UserAdminConfig(UserAdmin):
    ordering = ('username',)
    list_filter = ('username','first_name','is_active','is_staff')
    search_fields = ('email','username','first_name','is_active','is_staff')
    list_display = ('username','email','first_name','last_name','is_active','is_staff')

#admin.site.register(User,UserAdmin)

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

admin.site.register(User)
admin.site.register(Creator)
admin.site.register(Admin)
admin.site.register(feature)
admin.site.register(blogs)
admin.site.register(comments)
admin.site.register(community)
admin.site.register(contact)
admin.site.register(signup)
admin.site.register(slider)
admin.site.register(tips)
admin.site.register(subjects)


