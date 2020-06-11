# # activate_this = 'C:/Users/myuser/Envs/my_application/Scripts/activate_this.py'
# activate_this = 'C:/Users/PRENCHAND/secondrepoofdjango/repeat_store_product/Scripts/activate_this.py'
# # execfile(activate_this, dict(__file__=activate_this))
# exec(open(activate_this).read(),dict(__file__=activate_this))

# import os
# import sys
# import site

# # Add the site-packages of the chosen virtualenv to work with
# # site.addsitedir('C:/Users/myuser/Envs/my_application/Lib/site-packages')
# site.addsitedir('C:/Users/PRENCHAND/secondrepoofdjango/repeat_store_product/Lib/site-packages')




# # Add the app's directory to the PYTHONPATH
# sys.path.append('C:/Users/PRENCHAND/secondrepoofdjango/repeat_store_product')
# sys.path.append('C:/Users/PRENCHAND/secondrepoofdjango/repeat_store_product/repeat')

# os.environ['DJANGO_SETTINGS_MODULE'] = 'repeat.settings'
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "repeat.settings")

# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()


# def users_not_login_past_three_months(request):#stockants code
#     response = []
#     data = []
#     counts = 0

#     try:
#         today_date = date.today()
#         last_date = today_date - timedelta(days=90)
#         not_login_users = User.objects.filter(last_login__range=(last_date, today_date))

#         for obj in not_login_users:
#             counts+=1
#             data.append({'username':obj.username})

#         return JsonResponse({'validation':'success','resposne':data,"not login past 3 months users":counts,'status':True})
#     except Exception as e:
#         return JsonResponse({'validation':str(e),'status':False})
        # -------------------------------------------------------------------------------------------------

