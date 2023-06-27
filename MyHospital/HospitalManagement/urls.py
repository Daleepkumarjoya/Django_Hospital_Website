
from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage, name="Home Views"),
    path('servicePage/', views.servicePage, name="servicePage Views"),
    path('readMore/<slug>', views.readMore, name="readMore Views"),
    path('aboutPage/', views.aboutPage, name="aboutPage Views"),
    path('doctorPage/', views.doctorPage, name="doctorPage Views"),
    path('bookPage/', views.bookPage, name="bookPage Views"),
    path('postComment/', views.postComment, name="postComment Views"),
    path('Comment/', views.Comment, name="Comment Views"),
    path('contactus/', views.contactus, name="contactus Views"),
    path('signup/', views.signup, name="signup Views"),
    path('Login/', views.Login, name="Login Views"),
    path('LogOut/', views.LogOut, name="Logout Views"),
]
