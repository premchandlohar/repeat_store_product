from django.urls import path
from bank import views
# from django.contrib.auth import views as auth_views


urlpatterns = [   
    path('establish_new_bank/', views.establish_new_bank),
    path('update_bank_details/', views.update_bank_details),
    path('get_bank_details_by_ifsc_code/', views.get_bank_details_by_ifsc_code),
    path('get_all_bank_details/', views.get_all_bank_details),
    path('terminate_bank/', views.terminate_bank),

]