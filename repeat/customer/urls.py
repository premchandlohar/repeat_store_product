from django.urls import path
from customer import views
# from django.contrib.auth import views as auth_views


urlpatterns = [   
    path('createuser/', views.createuser),
    path('updateuser/', views.updateuser),
    path('getuser/', views.getuser),
    path('getalluser/', views.getalluser),
    path('deleteuser/', views.deleteuser),
    path('createaddress/', views.createaddress),
    path('updateaddress/', views.updateaddress),
    path('getaddress/', views.getaddress),
    path('getalladdress/', views.getalladdress),
    path('deleteaddress/', views.deleteaddress),
    path('getaddressesbyuserid/', views.getaddressesbyuserid),
    path('userlogin/', views.userlogin),
    path('changeuserpassword/', views.changeuserpassword),
    path('forgetuserpassword/', views.forgetuserpassword),
    path('login/', views.login),


    # path('accounts/login/', auth_views.LoginView.as_view()),

]
