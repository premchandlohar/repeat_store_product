from django.urls import path
from market import views

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
     path('createuser/', views.createuser),
     path('updateuser/', views.updateuser),
     path('getuser/', views.getuser),
     path('getalluser/', views.getalluser),
     path('deleteuser/', views.deleteuser),


]