# from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
from django.db import transaction
from validator import *
from django.core.mail import send_mail,BadHeaderError
from repeat.settings import EMAIL_HOST_USER
from customer.models import Userprofile
# Create your views here.

def create_store(request):
    try:
        user_mails = []
        params = request.POST

        store_name = params.get('store_name')
        store_address = params.get('store_address')
        store_location = params.get('store_location')
        store_latitude = float(params.get('store_latitude'))
        store_longitude = float(params.get('store_longitude'))
        store_city = params.get('store_city')
        store_state = params.get('store_state')
        store_image = request.FILES.get('store_image')
        sub = 'New store open'
        body = 'in the'+' '+store_name+' '+'some offers are available.'

        qs = Userprofile.objects.all()
        for user in qs:
            user_mails.append(user.email)

        if valid_string(store_name): return JsonResponse({'validation':'enter valid store_name,must be string'})
        elif valid_string(store_address): return JsonResponse({'validation':'enter valid store_address,must be string'})
        elif valid_string(store_location): return JsonResponse({'validation':'enter valid store_location,must be string'})
        elif valid_float(store_latitude): return JsonResponse({'validation':'enter valid store_latitude,must float'})
        elif valid_float(store_longitude): return JsonResponse({'validation':'enter valid store_longitude,must be float'})
        elif valid_string(store_city): return JsonResponse({'validation':'enter valid store_city,must be string'})
        elif valid_string(store_state): return JsonResponse({'validation':'enter valid store_state,must string'})
        elif valid_string(store_state): return JsonResponse({'validation':'enter valid store_state,must string'})
        elif valid_image(store_image): return JsonResponse({'validation':'select valid image file,must be a valid format'})
        elif valid_string(sub):return JsonResponse({'validation':'enter valid sub,must be a string'})   
        elif valid_string(body):return JsonResponse({'validation':'enter valid body,must be a string'})   
        # elif valid_email(user_mail):return JsonResponse({'validation':'enter valid email,must be a string'})

        with transaction.atomic():           
            create_store_obj = Store.objects.create(
                store_name = store_name,
                store_address = store_address,
                store_location = store_location,
                store_latitude = store_latitude,
                store_longitude = store_longitude,
                store_city = store_city,
                store_state = store_state,
                store_image = store_image
            )

            if sub and body and user_mails:
                try:
                    send_mail(sub,body,EMAIL_HOST_USER,user_mails,fail_silently=False)

                except BadHeaderError:
                    return JsonResponse({'response':'invalid header found'})

                return JsonResponse({'validation':'success','msg':
                    'successfully send mail to user for our store info','status':True})
                
            else:return JsonResponse({'validation':'invalid credential','status':False})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def update_store(request):
    try:
        params = request.POST

        store_id = params.get('store_id')
        store_name = params.get('store_name')
        store_address = params.get('store_address')
        store_location = params.get('store_location')
        store_latitude = float(params.get('store_latitude'))
        store_longitude = float(params.get('store_longitude'))
        store_city = params.get('store_city')
        store_state = params.get('store_state')
        store_image = request.FILES.get('store_image')

        if valid_string(store_name): return JsonResponse({'validation':'enter valid store_name,must be string'})
        elif valid_string(store_address): return JsonResponse({'validation':'enter valid store_address,must be string'})
        elif valid_string(store_location): return JsonResponse({'validation':'enter valid store_location,must be string'})
        elif valid_float(store_latitude): return JsonResponse({'validation':'enter valid store_latitude,must float'})
        elif valid_float(store_longitude): return JsonResponse({'validation':'enter valid store_longitude,must be float'})
        elif valid_string(store_city): return JsonResponse({'validation':'enter valid store_city,must be string'})
        elif valid_string(store_state): return JsonResponse({'validation':'enter valid store_state,must string'})
        elif valid_string(store_state): return JsonResponse({'validation':'enter valid store_state,must string'})
        elif valid_image(store_image): return JsonResponse({'validation':'select valid image file,must be a valid format'})

        with transaction.atomic():
            store_obj = Store.objects.get(id = store_id)
            # print(store_obj)
            store_obj.store_name = store_name
            store_obj.store_address = store_address
            store_obj.store_location = store_location
            store_obj.store_latitude = store_latitude
            # print(store_latitude)
            store_obj.store_longitude = store_longitude
            store_obj.store_city = store_city
            store_obj.store_state = store_state
            store_obj.store_image = store_image
            store_obj.save()

            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def get_store(request):
    try:
        params = json.loads(request.body)
        response =[]

        store_id = params.get('store_id')
        if valid_integer(store_id): return JsonResponse({'validation':'enter valid store_id,must be int'})

        store_obj = Store.objects.get(id=store_id)
        response.append({
            'store_id' :store_obj.id,
            'store_name' :store_obj.store_name,
            'store_address' :store_obj.store_address,
            'store_location' :store_obj.store_location,
            'store_latitude' :store_obj.store_latitude,
            'store_longitude' :store_obj.store_longitude,
            'store_city' :store_obj.store_city,
            'store_state' :store_obj.store_state,
            'store_image' :str(store_obj.store_image),
            'created_on' :store_obj.created_on
        })

        return JsonResponse({'validation':'success','responsse':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def get_all_store(request):
    try:
        response = []

        qs = Store.objects.all()
        for store in qs:
            response.append({
                'store_id' :store.id,
                'store_name' :store.store_name,
                'store_address' :store.store_address,
                'store_location' :store.store_location,
                'store_latitude' :store.store_latitude,
                'store_longitude' :store.store_longitude,
                'store_city' :store.store_city,
                'store_state' :store.store_state,
                'store_image' :str(store.store_image),
                'created_on' :store.created_on
            })

        return JsonResponse({'validation':'success','responsse':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def delete_store(request):
    try:
        params = json.loads(request.body)

        store_id = params.get('store_id')
        if valid_integer(store_id): return JsonResponse({'validation':'enter valid store_id,must be int'})
        store_obj = Store.objects.get(id=store_id).delete()
       
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?
    
def create_category(request):
    try:
        params = request.POST

        store_id = int(params.get('store_id'))
        category_name = params.get('category_name')
        category_image = request.FILES.get('category_image')

        if valid_integer(store_id): return JsonResponse({'validation':'enter valid store_id,must be int'})
        elif valid_string(category_name): return JsonResponse({'validation':'enter valid category_name,must string'})
        elif valid_image(category_image): return JsonResponse({'validation':'select valid image file,must be a valid format'})

        with transaction.atomic():
            store_obj = Store.objects.get(id = store_id)
            create_category_obj = Category.objects.create(
                store = store_obj,
                category_name = category_name,
                category_image = category_image,
            )

            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?
    
def update_category(request):
    try:
        params = request.POST

        category_id = int(params.get('category_id'))
        category_name = params.get('category_name')
        category_image = request.FILES.get('category_image')

        if valid_integer(category_id): return JsonResponse({'validation':'enter valid category_id,must be int'})
        elif valid_string(category_name): return JsonResponse({'validation':'enter valid category_name,must string'})
        elif valid_image(category_image): return JsonResponse({'validation':'select valid image file,must be a valid format'})
       
        with transaction.atomic():
            caregory_obj = Category.objects.get(id = category_id)
            caregory_obj.category_name = category_name
            caregory_obj.category_image = category_image
            caregory_obj.save()

            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def get_category(request):
    try:
        params = json.loads(request.body)
        response = []

        category_id = params.get('category_id')
        if valid_integer(category_id): return JsonResponse({'validation':'enter valid category_id,must be int'})

        category_obj = Category.objects.get(id = category_id)
        response.append({
            'store_id':category_obj.store.id,
            'category_id':category_obj.id,
            'category_name':category_obj.category_name,
            'store_name':category_obj.store.store_name,
            'category_image':str(category_obj.category_image),
            'created_on':category_obj.created_on
        })

        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def get_all_category(request):
    try:
        response = []

        qs = Category.objects.all()
        for category in qs:
            response.append({
                'category_id':category.id,
                'category_name':category.category_name,
                'created_on':category.created_on
            })

        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def delete_category(request):
    try:
        params = json.loads(request.body)

        category_id = params.get('category_id')
        if valid_integer(category_id): return JsonResponse({'validation':'enter valid category_id,must be int'})
        category_obj = Category.objects.get(id = category_id).delete()

        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def create_subcategory(request):
    try:
        params = request.POST

        store_id = int(params.get('store_id'))
        category_id = int(params.get('category_id'))
        subcategory_name = params.get('subcategory_name')
        subcategory_image = request.FILES.get('subcategory_image')
        created_on = params.get('created_on')

        if valid_integer(store_id): return JsonResponse({'validation':'enter valid storid,must be int'})
        elif valid_integer(category_id): return JsonResponse({'validation':'enter valid category_id,must be int'})
        elif valid_string(subcategory_name): return JsonResponse({'validation':'enter valid subcategory_name,must string'})
        elif valid_image(subcategory_image): return JsonResponse({'validation':'select valid image file,must be a valid format'})
       
        with transaction.atomic():
            store_obj = Store.objects.get(id = store_id)
            category_obj = Category.objects.get(id = category_id)
            create_subcategory_obj = Subcategory.objects.create(
                store = store_obj,
                category = category_obj,
                subcategory_name = subcategory_name,
                subcategory_image = subcategory_image
            )

            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def update_subcategory(request):
    try:
        params = request.POST

        subcategory_id = int(params.get('subcategory_id'))
        subcategory_name = params.get('subcategory_name')
        subcategory_image = request.FILES.get('subcategory_image')

        if valid_integer(subcategory_id): return JsonResponse({'validation':'enter valid subcategory_id,must be int'})
        elif valid_string(subcategory_name): return JsonResponse({'validation':'enter valid subcategory_name,must string'})
        elif valid_image(subcategory_image): return JsonResponse({'validation':'select valid image file,must be a valid format'})
       
        with transaction.atomic():
            subcategory_obj = Subcategory.objects.get(id = subcategory_id)
            subcategory_obj.subcategory_name = subcategory_name
            subcategory_obj.subcategory_image = subcategory_image
            subcategory_obj.save()

            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def get_subcategory(request):
    try:
        params = json.loads(request.body)
        response = []

        subcategory_id = params.get('subcategory_id')  
        if valid_integer(subcategory_id): return JsonResponse({'validation':'enter valid subcategory_id,must be int'})

        subcategory_obj = Subcategory.objects.get(id=subcategory_id)
        response.append({
            'subcategory_id':subcategory_obj.id,
            'category_id':subcategory_obj.category.id,
            'store_id':subcategory_obj.store.id,
            'subcategory_name':subcategory_obj.subcategory_name,
            'category_name':subcategory_obj.category.category_name,
            'store_name':subcategory_obj.store.store_name,
            'subcategory_image':str(subcategory_obj.subcategory_image),
            'created_on':subcategory_obj.created_on
        })

        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_all_subcategory(request):
    try:
        response =[]

        qs = Subcategory.objects.all()
        for subcategory in qs:
            response.append({
                'subcategory_id':subcategory.id,
                'subcategory_name':subcategory.subcategory_name,
                'created_on':subcategory.created_on
            })

        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def delete_subcategory(request):
    try:
        params = json.loads(request.body)

        subcategory_id = params.get('subcategory_id')  
        if valid_integer(subcategory_id): return JsonResponse({'validation':'enter valid subcategory_id,must be int'})
        subcategory_obj = Subcategory.objects.get(id=subcategory_id).delete()
       
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def create_product(request):
    try:
        params = request.POST   

        store_id = int(params.get('store_id'))
        subcategory_id = int(params.get('subcategory_id'))
        product_name = params.get('product_name')
        product_quantity = int(params.get('product_quantity'))
        product_price = float(params.get('product_price'))
        product_discount_price = float(params.get('product_discount_price'))
        product_description = params.get('product_description')
        product_image = request.FILES.get('product_image')

        if valid_integer(store_id): return JsonResponse({'validation':'enter valid store_id,must be int'})
        elif valid_integer(subcategory_id): return JsonResponse({'validation':'enter valid subcategory_id,must be int'})
        elif valid_string(product_name): return JsonResponse({'validation':'enter valid product_name,must string'})
        elif valid_integer(product_quantity): return JsonResponse({'validation':'enter valid product_quantity,must be int'})
        elif valid_float(product_price): return JsonResponse({'validation':'enter valid product_price,must be float'})
        elif valid_float(product_discount_price): return JsonResponse({'validation':'enter valid product_discount_price,must be float'})
        elif valid_string(product_description): return JsonResponse({'validation':'enter valid product_description,must string'})
        elif valid_image(product_image): return JsonResponse({'validation':'select valid image file,must be a valid format'})

        with transaction.atomic():
            store_obj = Store.objects.get(id=store_id)
            subcategory_obj = Subcategory.objects.get(id=subcategory_id)
            create_product_obj = Product.objects.create(
                store = store_obj,
                subcategory = subcategory_obj,
                product_name = product_name,
                product_quantity =product_quantity,
                product_price = product_price,
                product_discount_price = product_discount_price,
                product_description = product_description,
                product_image = product_image
            )

            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def update_product(request):
    try:
        params = request.POST

        product_id = int(params.get('product_id'))
        # subcategory_id = int(params.get('subcategory_id'))
        product_name = params.get('product_name')
        product_quantity = int(params.get('product_quantity'))
        product_price = float(params.get('product_price'))
        product_discount_price = float(params.get('product_discount_price'))
        product_description = params.get('product_description')
        product_image = request.FILES.get('product_image')

        if valid_integer(product_id): return JsonResponse({'validation':'enter valid product_id,must be int'})
        # elif valid_integer(subcategory_id): return JsonResponse({'validation':'enter valid subcategory_id,must be int'})
        elif valid_string(product_name): return JsonResponse({'validation':'enter valid product_name,must string'})
        elif valid_integer(product_quantity): return JsonResponse({'validation':'enter valid product_quantity,must be int'})
        elif valid_float(product_price): return JsonResponse({'validation':'enter valid product_price,must be float'})
        elif valid_float(product_discount_price): return JsonResponse({'validation':'enter valid product_discount_price,must be float'})
        elif valid_string(product_description): return JsonResponse({'validation':'enter valid product_description,must string'})
        elif valid_image(product_image): return JsonResponse({'validation':'select valid image file,must be a valid format'})

        with transaction.atomic():
            product_obj = Product.objects.get(id=product_id)
            product_obj.product_name = product_name
            product_obj.product_quantity =product_quantity
            product_obj.product_price = product_price
            product_obj.product_discount_price = product_discount_price
            product_obj.product_description = product_description
            product_obj.product_image = product_image
            product_obj.save()

            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_product(request):
    try:
        params = json.loads(request.body)
        response = []

        product_id = params.get('product_id')
        if valid_integer(product_id): return JsonResponse({'validation':'enter valid product_id,must be int'})

        product_obj = Product.objects.get(id=product_id)
        response.append({
            'store_id':product_obj.store.id,
            'subcategory_id':product_obj.subcategory.id,
            'product_id':product_obj.id,
            'product_name':product_obj.product_name,
            'subcategory_name':product_obj.subcategory.subcategory_name,
            'store_name':product_obj.store.store_name,
            'created_on':product_obj.created_on
        })

        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_all_product(request):
    try:
        response = []

        qs = Product.objects.all()
        for products in qs:
            response.append({
                'product_id':products.id,
                'product_name':products.product_name,
                'created_on':products.created_on
            })

        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def delete_product(request):
    try:
        params = json.loads(request.body)

        product_id = params.get('product_id')
        if valid_integer(product_id): return JsonResponse({'validation':'enter valid product_id,must be int'})
        product_obj = Product.objects.get(id = product_id).delete()

        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def add_followership(request):
    try:
        params = json.loads(request.body)

        user_id = params.get('user_id')
        store_id = params.get('store_id')

        if valid_integer(user_id):return JsonResponse({'validation':'enter valid user_id,must be a integer'})  
        elif valid_integer(store_id):return JsonResponse({'validation':'enter valid store_id,must be a integer'})  

        with transaction.atomic():
            user_obj = Userprofile.objects.get(id = user_id)
            store_obj = Store.objects.get(id = store_id)

            create_followership_obj = Followership.objects.create(
                store = store_obj,
                user = user_obj
            )

            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def update_followership(request):
    try:
        params = json.loads(request.body)
        
        followership_id = params.get('followership_id')
        store_id = params.get('store_id')
        user_id = params.get('user_id')
        if valid_integer(followership_id):return JsonResponse({'validation':'enter valid followership_id,must be a integer'})  
        elif valid_integer(store_id):return JsonResponse({'validation':'enter valid store_id,must be a integer'})  
        elif valid_integer(user_id):return JsonResponse({'validation':'enter valid user_id,must be a integer'})  

        with transaction.atomic():
            user_obj = Userprofile.objects.get(id = user_id)
            store_obj = Store.objects.get(id = store_id)

            followership_obj = Followership.objects.get(id = followership_id)
            followership_obj.store = store_obj
            followership_obj.user = user_obj
            followership_obj.save()

            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_followers_by_store(request):
    try:
        response = []
        params = json.loads(request.body)

        store_id = params.get('store_id')
        if valid_integer(store_id):return JsonResponse({'validation':'enter valid store_id,must be a integer'})  
        store_obj = Store.objects.get(id = store_id)

        qs = store_obj.follower.all()
        for users in qs:
            response.append({"store_name":store_obj.store_name,
                'user_id':users.user.id,
                'first_name':users.user.first_name
            })

        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_stores_by_follower(request):
    try:
        response = []
        params = json.loads(request.body)

        user_id = params.get('user_id')
        if valid_integer(user_id):return JsonResponse({'validation':'enter valid user_id,must be a integer'})  

        user_obj =Userprofile.objects.get(id = user_id)
        qs = user_obj.following.all()
        for store in qs:
            response.append({
                'store_id':store.store.id,
                'store_name':store.store.store_name
            })

        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def remove_follower_by_some_reason(request):
    try:
        params = json.loads(request.body)
        
        followership_id = params.get('followership_id')
        reason = params.get('reason')

        if valid_integer(followership_id):return JsonResponse({'validation':'enter valid followership_id,must be a integer'})  
        elif valid_integer(reason):return JsonResponse({'validation':'enter valid reason,must be a integer'})  

        follower_obj = Followership.objects.get(id = followership_id)
        follower_obj.user = None
        follower_obj.reason = reason
        follower_obj.save()

        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_all_followerships(request):
    try:
        response = []

        qs = Followership.objects.all()
        for followers in qs:
            response.append(followers.getjson())

        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def send_mail_to_all_followers_for_specific_store(request):
    try:
        params = json.loads(request.body)  

        store_id = params.get('store_id')
        followers_data = []
        recipient = []

        if valid_integer(store_id): return JsonResponse({'validation':'enter valid store_id,must be int'})                  
        with transaction.atomic():          
            store_obj = Store.objects.get(id=store_id)
            product_obj = store_obj.products.get(id = 2)
            followers_qs = store_obj.follower.all()
            user_qs = Userprofile.objects.all()

            for obj in followers_qs:
                followers_data.append(user_qs.get(first_name = (obj.user.first_name)))

            for obj in followers_data:
                recipient.append(obj.email)
                
        subject = 'Latest Trending Product with discount available,in our Store'
        details_of_product = {"Product_Name" : product_obj.product_name, 
            "Product_Price" : product_obj.product_price,"product_discount_price":product_obj.product_discount_price }

        send_mail(subject,str(details_of_product),EMAIL_HOST_USER,recipient,fail_silently=False)

        return JsonResponse({'validation':'successfully send mail to followers of (store_obj.store_name)','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# try:
#         subject = 'Latest Trending Product in our Store'
#         details_dict = {"Product Name" : data["product_name"], "Product Price" : data["product_price"], 
#         "Product Discount Price" : data["product_discount_price"], 
#         "Product Description" : data["product_description"]}
#         recipient = []
#         follow_data = []
#         followers, status, message = get_follower_by_stores_function(data)
#         all_user = UserProfile.objects.all()
#         for obj in followers:
#             follow_data.append(all_user.get(id = obj["id"]))
#         for obj in follow_data:
#             recipient.append(obj.email)
#         send_mail(subject, str(details_dict), EMAIL_HOST_USER, recipient, fail_silently= False)
#         return True, "Email send successfully"
#     except Exception as e:
#         return False, str(e)