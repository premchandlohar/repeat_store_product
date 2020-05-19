from django.urls import path
from customer import views
# from django.contrib.auth import views as auth_views


urlpatterns = [   
    path('create_user/', views.create_user),
    path('update_user/', views.update_user),
    path('get_user/', views.get_user),
    path('get_all_user/', views.get_all_user),
    path('delete_user/', views.delete_user),
    path('create_address/', views.create_address),
    path('update_address/', views.update_address),
    path('get_address/', views.get_address),
    path('get_all_address/', views.get_all_address),
    path('delete_address/', views.delete_address),
    path('get_addresses_by_user_id/', views.get_addresses_by_user_id),
    path('user_login/', views.user_login),
    path('change_user_password/', views.change_user_password),
    path('forget_user_password/', views.forget_user_password),
    path('login/', views.login),


    # path('accounts/login/', auth_views.LoginView.as_view()),

]
