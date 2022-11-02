from userPanel import views
from django.urls import path


urlpatterns = [
    path('login/', views.Login , name="creator_login"),

    path('permission/', views.Permission , name="permission"),
    path('logout/', views.LogOut , name="logout"),
    path('signup/', views.Creator_SignUp.as_view() , name="signup"),
    path('changePass/', views.MyPasswordChangeView.as_view() , name="changePass"),

    path('logout/', views.LogOut , name="logout"),
    path('signup/', views.Creator_SignUp.as_view() , name="signup"),
    #path('signup/', views.Creator_SignUp , name="signup"),

    path('dashboard/', views.Dashboard,name="dashboard"),
    path('creator_profile_show/', views.Creator_Profile_show,name="creator_profile_show"),
    path('creator_profile_edit/', views.Creator_Profile_edit,name="creator_profile_edit"),
    path('creator_profile_set/', views.Creator_Profile_set,name="creator_profile_set"),

    path('set_slider/', views.setSlider,name="set_slider"),
    path('view_slider/', views.viewSlider,name="view_slider"),
    path('update_slider/<id>', views.updateSlider,name="update_slider"),
    path('del_slider/<id>', views.delSlider,name="del_slider"),

    path('set_found/', views.setFound,name="set_found"),
    path('view_found/', views.viewFound,name="view_found"),
    path('update_found/<id>', views.updateFound,name="update_found"),
    path('del_found/<id>', views.delFound,name="del_found"),

    path('set_feature/', views.setFeature,name="set_feature"),
    path('view_feature/', views.viewFeature,name="view_feature"),
    path('update_feature/<id>', views.updateFeature,name="update_feature"),

    #path('del_feature/<id>', views.delFeature,name="del_feature"),




    path('set_tips/', views.setTips,name="set_tips"),
    path('view_tips/', views.viewTips,name="view_tips"),
    path('update_tips/<id>', views.updateTips,name="update_tips"),
    path('del_tips/<id>', views.delTips,name="del_tips"),

    path('set_subject/', views.setSubject,name="set_subject"),
    path('view_subject/', views.viewSubject,name="view_subject"),
    path('update_subject/<id>', views.updateSubject,name="update_subject"),
    path('del_subject/<id>', views.delSubject,name="del_subject"),

    path('set_community/', views.setCommunity,name="set_community"),
    path('view_community/', views.viewCommunity,name="view_community"),
    path('update_community/<id>', views.updateCommunity,name="update_community"),
    path('del_community/<id>', views.delCommunity,name="del_community"),

    path('set_guideline/', views.setGuideline,name="set_guideline"),
    path('view_guideline/', views.viewGuideline,name="view_guideline"),
    path('update_guideline/<id>', views.updateGuideline,name="update_guideline"),
    path('del_guideline/<id>', views.delGuideline,name="del_guideline"),

    path('set_blog/', views.setBlog,name="set_blog"),
    path('view_blog/', views.viewBlog,name="view_blog"),
    path('update_blog/<id>', views.updateBlog,name="update_blog"),
    path('del_blog/<id>', views.delBlog,name="del_blog"),

    path('set_contact/', views.setContact,name="set_contact"),
    path('view_contact/', views.viewContact,name="view_contact"),
    path('update_contact/<id>', views.updateContact,name="update_contact"),
    path('del_contact/<id>', views.delContact,name="del_contact"),
    path('calender/', views.calender,name="calender"),
    path('chat/', views.chat,name="chat"),
    path('invoice/', views.invoice,name="invoice"),

]
