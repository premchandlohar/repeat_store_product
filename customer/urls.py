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
    path('login/', views.login),
    path('change_user_password/', views.change_user_password),
    path('forgot_user_password/', views.forgot_user_password),
    path('send_email/', views.send_email),
    path('send_mass_email/', views.send_mass_email),
    path('get_all_permissions_names/', views.get_all_permissions_names),
    path('assign_selected_permission_to_user/', views.assign_selected_permission_to_user),
    path('assign_all_permissions_to_users/', views.assign_all_permissions_to_users),
    path('remove_permissions_to_users/', views.remove_permissions_to_users),


    # path('accounts/login/', auth_views.LoginView.as_view()),

]
