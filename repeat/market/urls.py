from django.urls import path
from market import views
from django.contrib.auth import views as auth_views


urlpatterns = [
     path('create_store/', views.create_store),
     path('update_store/', views.update_store),
     path('get_store/', views.get_store),
     path('delete_store/', views.delete_store),
     path('get_all_store/', views.get_all_store),
     path('create_category/', views.create_category),
     path('update_category/', views.update_category),
     path('delete_category/', views.delete_category),
     path('get_category/', views.get_category),
     path('get_all_category/', views.get_all_category),
     path('create_subcategory/', views.create_subcategory),
     path('update_subcategory/', views.update_subcategory),
     path('delete_subcategory/', views.delete_subcategory),
     path('get_subcategory/', views.get_subcategory),
     path('get_all_subcategory/', views.get_all_subcategory),
     path('create_product/', views.create_product),
     path('update_product/', views.update_product),
     path('get_product/', views.get_product),
     path('get_all_product/', views.get_all_product),
     path('delete_product/', views.delete_product),
     path('add_followership/', views.add_followership),
     path('update_followership/', views.update_followership),
     path('get_followers_by_store/', views.get_followers_by_store),
     path('get_stores_by_follower/', views.get_stores_by_follower),
     path('remove_follower_by_some_reason/', views.remove_follower_by_some_reason),
     path('get_all_followerships/', views.get_all_followerships),
    
]