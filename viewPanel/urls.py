from viewPanel import views
from django.urls import path

urlpatterns = [
    path('', views.homePage),
    path('home/', views.homePage,name="home"),
    path('about/', views.aboutPage,name="about"),
    path('blog/', views.blogPage,name="blog"),
    path('profile/', views.profilePage,name="profile"),
    path('file_download/<int:id>', views.File_download,name="file_download"),
    path('blog_details/<int:id>', views.blogDetailsPage,name="blog_details"),
    path('contact/', views.contactPage,name="contact"),
    path('course/', views.coursePage,name="course"),
    path('details_course/<int:id>', views.course_detailsPage,name="details_course"),
    path('checkout/<int:id>', views.checkoutPage,name="checkout"),
    path('view_login/', views.loginPage,name="view_login"),
    path('view_logout/', views.LogOut,name="view_logout"),
    path('chat/<int:id>', views.Chat,name="chat"),
    path('register/', views.Customer_SignUp.as_view()),
 ]




