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
    path('aggregate_function/', views.aggregate_function),
    path('annotate_function/', views.annotate_function),
    path('UserProfileListview/', views.UserProfileListview.as_view()),
    # path('username/', views.username),





    # path('accounts/login/', auth_views.LoginView.as_view()),

]

# class user_listview(ListView):
#     models = Userprofile

    # def get_queryset(self,request):
    #     qs = super().get_queryset() 
        # response = []
        # obj = Userprofile.objects.all()
        # for user in obj:
        #     response.append(user.first_name)
        # return JsonResponse({'status':qs})

    # def get_queryset(self):
    #     response = []
    #     qs = self.models.objects.filter(
    #         first_name=self.user.first_name)
    #     print(qs)
    #     # a= Userprofile.objects.get(id=qs)
    #     # for q in qs:
    #     #     response.append(qs.first_name)
    #     # qs = super(user_listview,self).get_queryset(self,pk=self.kwargs['1'])
    #     # if request.user.is_superuser:
    #     #     return qs
    #     # a=qs.filter(first_name=self.user)
    #     return JsonResponse(list(qs))

        
    # def get_queryset(self):
    #     response = []

#         # a=Userprofile.objects.filter(user=self.request.user)
#         # queryset = super(user_listview, self).get_queryset()
#         # queryset = queryset.filter(user=self.request.user)
#         # return JsonResponse({'status':a})
#         a=Userprofile.objects.order_by('id')
#         for obj in a:
#             response.append(obj.first_name)

#         return JsonResponse({'status':response})
# foo = Foo.objects.order_by('-id')
#         bar = foo.filter(Country=64)
#         return foo, bar
