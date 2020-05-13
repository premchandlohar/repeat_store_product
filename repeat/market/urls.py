from django.urls import path
from market import views
from django.contrib.auth import views as auth_views


urlpatterns = [
     path('createstore/', views.createstore),
     path('updatestore/', views.updatestore),
     path('getstore/', views.getstore),
     path('deletestore/', views.deletestore),
     path('getallstore/', views.getallstore),
     path('createcategory/', views.createcategory),
     path('updatecategory/', views.updatecategory),
     path('deletecategory/', views.deletecategory),
     path('getcategory/', views.getcategory),
     path('getallcategory/', views.getallcategory),
     path('createsubcategory/', views.createsubcategory),
     path('updatesubcategory/', views.updatesubcategory),
     path('deletesubcategory/', views.deletesubcategory),
     path('getsubcategory/', views.getsubcategory),
     path('getallsubcategory/', views.getallsubcategory),
     path('createproduct/', views.createproduct),
     path('updateproduct/', views.updateproduct),
     path('getproduct/', views.getproduct),
     path('getallproduct/', views.getallproduct),
     path('deleteproduct/', views.deleteproduct),
     path('addfollowership/', views.addfollowership),
     path('updatefollowership/', views.updatefollowership),
     path('getfollowersbystore/', views.getfollowersbystore),
     path('getstoresbyfollower/', views.getstoresbyfollower),
     path('removeuserbysomereason/', views.removeuserbysomereason),
     path('getallfollowerships/', views.getallfollowerships),
    
]