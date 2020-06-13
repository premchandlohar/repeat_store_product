from django.http import JsonResponse
from .models import *
import json
from django.db import transaction
from validator import *
from django.core.mail import send_mail,BadHeaderError
from repeat.settings import EMAIL_HOST_USER
from customer.models import Userprofile

def create_store(request):
    params = request.POST

    try:
        store_name = params.get('store_name')
        store_address = params.get('store_address')
        store_location = params.get('store_location')
        store_latitude = float(params.get('store_latitude'))
        store_longitude = float(params.get('store_longitude'))
        store_city = params.get('store_city')
        store_state = params.get('store_state')
        store_image = request.FILES.get('store_image')
        sub = 'New store open'
        body = 'in the store_name some offers are available '
        user_id = int(params.get('user_id'))

        user_obj = Userprofile.objects.get(id = user_id)
        user_mail = user_obj.email

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
        elif valid_email(user_mail):return JsonResponse({'validation':'enter valid email,must be a string'})

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

            if sub and body and user_mail:
                try:
                    send_mail(sub,body,EMAIL_HOST_USER,[user_mail],fail_silently=False)

                except BadHeaderError:
                    return JsonResponse({'response':'invalid header found'})

                return JsonResponse({'validation':'success','msg':
                    'successfully send mail to user for our store info','status':True})
                
            else:
                return JsonResponse({'validation':'invalid credential','status':False})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def update_store(request):
    params = request.POST
    try:
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
            store_obj.store_name = store_name
            store_obj.store_address = store_address
            store_obj.store_location = store_location
            store_obj.store_latitude = store_latitude
            print(store_latitude)
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
    params = json.loads(request.body)
    response =[]

    try:
        store_id = params.get('store_id')
        if valid_integer(store_id): return JsonResponse({'validation':'enter valid store_id,must be int'})

        store_obj = Store.store_objects.get(id=store_id)

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
    response = []

    try:
        queryset = Store.objects.all()

        for store in queryset:
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
    params = json.loads(request.body)

    try:
        store_id = params.get('store_id')
        if valid_integer(store_id): return JsonResponse({'validation':'enter valid store_id,must be int'})
       
        store_obj = Store.objects.get(id=store_id).delete()
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?
    
def create_category(request):
    params = request.POST

    try:
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
    params = request.POST

    category_id = int(params.get('category_id'))
    category_name = params.get('category_name')
    category_image = request.FILES.get('category_image')

    try:
        if valid_integer(category_id): return JsonResponse({'validation':'enter valid category_id,must be int'})
        elif valid_string(category_name): return JsonResponse({'validation':'enter valid category_name,must string'})
        elif valid_image(category_image): return JsonResponse({'validation':'select valid image file,must be a valid format'})
       
        with transaction.atomic():
            category_obj = Category.objects.get(id = category_id)

            category_obj.category_name = category_name
            category_obj.category_image = category_image
            category_obj.save()
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def get_category(request):
    params = json.loads(request.body)
    response = []

    category_id = params.get('category_id')
    if valid_integer(category_id): return JsonResponse({'validation':'enter valid category_id,must be int'})

    try:
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
    response = []

    try:
        queryset = Category.objects.all()

        for categories in queryset:
            response.append({
                'category_id':categories.id,
                'category_name':categories.category_name,
                'created_on':categories.created_on
            })
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def delete_category(request):
    params = json.loads(request.body)

    category_id = params.get('category_id')

    try:
        if valid_integer(category_id): return JsonResponse({'validation':'enter valid category_id,must be int'})
       
        category_obj = Category.objects.get(id = category_id).delete()
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def create_subcategory(request):
    params = request.POST

    store_id = int(params.get('store_id'))
    category_id = int(params.get('category_id'))
    subcategory_name = params.get('subcategory_name')
    subcategory_image = request.FILES.get('subcategory_image')
    created_on = params.get('created_on')

    try:
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
    params = request.POST

    subcategory_id = int(params.get('subcategory_id'))
    subcategory_name = params.get('subcategory_name')
    subcategory_image = request.FILES.get('subcategory_image')

    try:
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
    params = json.loads(request.body)
    response = []

    subcategory_id = params.get('subcategory_id')
    
    try:
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
    response =[]

    try:
        queryset = Subcategory.objects.all()

        for subcategories in queryset:
            response.append({
                'subcategory_id':subcategories.id,
                'subcategory_name':subcategories.subcategory_name,
                'created_on':subcategories.created_on
            })
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def delete_subcategory(request):
    params = json.loads(request.body)

    subcategory_id = params.get('subcategory_id')
    
    try:
        if valid_integer(subcategory_id): return JsonResponse({'validation':'enter valid subcategory_id,must be int'})
       
        subcategory_obj = Subcategory.objects.get(id=subcategory_id).delete()
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def create_product(request):
    params = request.POST   

    store_id = int(params.get('store_id'))
    subcategory_id = int(params.get('subcategory_id'))
    product_name = params.get('product_name')
    product_quantity = int(params.get('product_quantity'))
    product_price = float(params.get('product_price'))
    product_discount_price = float(params.get('product_discount_price'))
    product_description = params.get('product_description')
    product_image = request.FILES.get('product_image')

    try:
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
    params = request.POST

    product_id = int(params.get('product_id'))
    product_name = params.get('product_name')
    product_quantity = int(params.get('product_quantity'))
    product_price = float(params.get('product_price'))
    product_discount_price = float(params.get('product_discount_price'))
    product_description = params.get('product_description')
    product_image = request.FILES.get('product_image')

    try:
        if valid_integer(product_id): return JsonResponse({'validation':'enter valid product_id,must be int'})
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
    params = json.loads(request.body)
    response = []

    product_id = params.get('product_id')

    try:
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
    response = []

    try:
        queryset = Product.objects.all()
        for products in queryset:
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
    params = json.loads(request.body)

    product_id = params.get('product_id')

    try:
        if valid_integer(product_id): return JsonResponse({'validation':'enter valid product_id,must be int'})

        product_obj = Product.objects.get(id = product_id).delete()

        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def add_followership(request):
    params = json.loads(request.body)

    user_id = params.get('user_id')
    store_id = params.get('store_id')

    try:
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
    params = json.loads(request.body)
    
    followership_id = params.get('followership_id')
    store_id = params.get('store_id')
    user_id = params.get('user_id')

    try:
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
    params = json.loads(request.body)
    response = []

    store_id = params.get('store_id')

    try:
        if valid_integer(store_id):return JsonResponse({'validation':'enter valid store_id,must be a integer'})  

        store_obj = Store.objects.get(id = store_id)
        
        follower_qs = store_obj.follower.all()
        for user in follower_qs:
            response.append({"store_name":store_obj.store_name,
                'user_id':user.user.id,
                'first_name':user.user.first_name
            })
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_stores_by_follower(request):
    params = json.loads(request.body)
    response = []

    user_id = params.get('user_id')

    try:
        if valid_integer(user_id):return JsonResponse({'validation':'enter valid user_id,must be a integer'})  

        user_obj =Userprofile.objects.get(id = user_id)

        following_qs = user_obj.following.all()
        for store in following_qs:
            response.append({
                'store_id':store.store.id,
                'store_name':store.store.store_name
            })
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def remove_follower_by_some_reason(request):
    params = json.loads(request.body)
     
    followership_id = params.get('followership_id')
    reason = params.get('reason')

    try:
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
    response = []

    try:
        follower_qs = Followership.objects.all()

        for followers in follower_qs:
            response.append(followers.getjson())

        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def send_mail_to_all_followers_for_specific_store(request):
    params = json.loads(request.body)  

    store_id = params.get('store_id')
    followers_data = []
    recipient = []

    try:
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


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

from django.http import JsonResponse
import json
from .models import Userprofile,Address
from django.contrib.auth import get_user_model
from django.db import transaction
from validator import *
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
import jwt
from datetime import timedelta,datetime 
from django.core.mail import send_mail,BadHeaderError,send_mass_mail,EmailMessage
from django.conf import settings
from repeat.settings import EMAIL_HOST_USER
from django.contrib.auth.models import Permission
from django.db.models import Avg,Max,Q,Count,Sum,Min,FloatField
from django.db.models.functions import Lower,Upper


# # Create your views here.
def verify_token(request):
    token = request.headers['token']
    if not token: 
        return False       
    try:         
        data = jwt.decode(token, "SECRET_KEY", algorithm='HS256')
        return True
    except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:        
        return False
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   
def create_user(request):
    params = json.loads(request.body)

    username = params.get('username')
    password = params.get('password')
    first_name = params.get('first_name')
    last_name = params.get('last_name')
    age = params.get('age')
    mobile_number = params.get('mobile_number')
    email = params.get('email')

    try:
        if valid_string(username):return JsonResponse({'validation':'enter valid username ,must be a string'})   
        elif valid_string(password):return JsonResponse({'validation':'enter valid password,must be a string'})  
        elif valid_string(first_name):return JsonResponse({'validation':'enter valid first_name,must be a string'})   
        elif valid_string(last_name):return JsonResponse({'validation':'enter valid last_name,must be a string'})    
        elif valid_integer(age):return JsonResponse({'validation':'enter valid age,must be a integer'})
        elif valid_mobile_number(mobile_number):return JsonResponse({'validation':'enter valid mobile_number ,must be a string and 10 digit'})   
        elif valid_email(email):return JsonResponse({'validation':'enter valid email,must be a string'})   
        
        with transaction.atomic():
            user_obj =get_user_model().objects.create(
                username = username,
                # is_staff = True
            )
            user_obj.set_password(password)
            user_obj.save()

            # permission = Permission.objects.get(name='Can view poll')
            # user_obj.user_permissions.add(permission)

            user_profile_obj = Userprofile.objects.create(
                user = user_obj,
                first_name = first_name,
                last_name = last_name,
                age = age,
                mobile_number = mobile_number,
                email = email
            )
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def update_user(request):
    params = json.loads(request.body)

    user_id = params.get('user_id')
    username = params.get('username')
    password = params.get('password')
    first_name = params.get('first_name')
    last_name = params.get('last_name')
    age = params.get('age')
    mobile_number = params.get('mobile_number')
    email = params.get('email')

    try:
        if valid_string(username):return JsonResponse({'validation':'enter valid username ,must be a string'})   
        elif valid_string(password):return JsonResponse({'validation':'enter valid password,must be a string'})  
        elif valid_string(first_name):return JsonResponse({'validation':'enter valid first_name,must be a string'})   
        elif valid_string(last_name):return JsonResponse({'validation':'enter valid last_name,must be a string'})    
        elif valid_integer(age):return JsonResponse({'validation':'enter valid age,must be a integer'}) 
        elif valid_mobile_number(mobile_number):return JsonResponse({'validation':'enter valid mobile_number ,must be a string and 10 digit'})   
        elif valid_email(email):return JsonResponse({'validation':'enter valid email,must be a string'})

        with transaction.atomic():
            user_obj = Userprofile.objects.get(id = user_id)
            user_obj.user.username = username
            user_obj.user.password = password
            user_obj.first_name = first_name
            user_obj.last_name = last_name
            user_obj.age = age
            user_obj.mobile_number = mobile_number
            user_obj.email = email
            user_obj.save()

            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_user(request):
    params = json.loads(request.body)
    resposne = []

    user_id = params.get('user_id')

    try:
        if valid_integer(user_id):return JsonResponse({'validation':'enter valid user_id,must be a integer'})
        
        user_obj = Userprofile.objects.get(id = user_id)
        resposne.append({
            'user_id':user_obj.id,
            'usernsme':user_obj.user.username,
            'first_name':user_obj.first_name,
            'last_name':user_obj.last_name,
            'age':user_obj.age,
            'mobile_number':user_obj.mobile_number,
            "email":user_obj.email,
            'created_on':user_obj.created_on
        })
        return JsonResponse({'validation':'success','resposne':resposne,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_all_user(request):
    resposne = []

    try:      
        queryset = Userprofile.objects.all()
        for users in queryset:
            resposne.append({
                'user_id':users.id,
                'usernsme':users.user.username,
                'first_name':users.first_name,
                'last_name':users.last_name,
                'mobile_number':users.mobile_number,
                "email":users.email,
            })
        return JsonResponse({'validation':'success','resposne':resposne,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def delete_user(request):
    params = json.loads(request.body)
    resposne = []

    user_id = params.get('user_id')

    try:
        if valid_integer(user_id):return JsonResponse({'validation':'enter valid user_id,must be a integer'})
        
        user_obj = Userprofile.objects.get(id = user_id).delete()
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def create_address(request):
    params = json.loads(request.body)

    user_id = params.get('user_id') 
    building_name = params.get('building_name')
    street_name = params.get('street_name')
    locality = params.get('locality')
    city = params.get('city')
    district = params.get('district')   
    state = params.get('state')
    pincode = params.get('pincode')

    try:
        if valid_integer(user_id):return JsonResponse({'validation':'enter valid user_id,must be a integer'})  
        elif valid_string(building_name):return JsonResponse({'validation':'enter valid building_name,must be a string'})    
        elif valid_string(street_name):return JsonResponse({'validation':'enter valid street_name,must be a string'})    
        elif valid_string(locality):return JsonResponse({'validation':'enter valid locality,must be a string'})    
        elif valid_string(city):return JsonResponse({'validation':'enter valid city,must be a string'})    
        elif valid_string(district):return JsonResponse({'validation':'enter valid district,must be a string'})    
        elif valid_string(state):return JsonResponse({'validation':'enter valid state,must be a string'})    
        elif valid_pincode(pincode):return JsonResponse({'validation':'enter valid pincode,must be a integer and only 6 digit required'})    
     
        with transaction.atomic():
            user_obj = Userprofile.objects.get(id = user_id)
            create_address_obj = Address.objects.create(
                user_profile = user_obj,
                building_name = building_name,
                street_name = street_name,
                locality = locality,
                city = city,
                district = district,
                state = state,
                pincode = pincode
            )
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def update_address(request):
    params = json.loads(request.body)

    address_id = params.get('address_id')
    building_name = params.get('building_name')
    street_name = params.get('street_name')
    locality = params.get('locality')
    city = params.get('city')
    district = params.get('district')
    state = params.get('state')
    pincode = params.get('pincode')

    try:
        if valid_integer(address_id):return JsonResponse({'validation':'enter valid address_id,must be a integer'})  
        elif valid_string(building_name):return JsonResponse({'validation':'enter valid building_name,must be a string'})    
        elif valid_string(street_name):return JsonResponse({'validation':'enter valid street_name,must be a string'})    
        elif valid_string(locality):return JsonResponse({'validation':'enter valid locality,must be a string'})    
        elif valid_string(city):return JsonResponse({'validation':'enter valid city,must be a string'})    
        elif valid_string(district):return JsonResponse({'validation':'enter valid district,must be a string'})    
        elif valid_string(state):return JsonResponse({'validation':'enter valid state,must be a string'})    
        elif valid_pincode(pincode):return JsonResponse({'validation':'enter valid pincode,must be a integer and only 6 digit required'})    
     
        with transaction.atomic():
            add_obj = Address.objects.get(id = address_id)
            add_obj.building_name = building_name
            add_obj.street_name = street_name
            add_obj.locality = locality
            add_obj.city = city
            add_obj.district = district
            add_obj.state = state
            add_obj.pincode = pincode
            add_obj.save()

            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_address(request):
    params = json.loads(request.body)
    response =[]

    address_id = params.get('address_id')

    try:
        if valid_integer(address_id):return JsonResponse({'validation':'enter valid address_id,must be a integer'})  

        add_obj = Address.objects.get(id = address_id)
        response.append({
            'address_id':add_obj.id,
            'building_name':add_obj.building_name,
            'street_name':add_obj.street_name,
            'locality':add_obj.locality,
            'city':add_obj.city,
            'district':add_obj.district,
            'state':add_obj.state,
            'pincode':add_obj.pincode
        })
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_all_address(request):

    status = verify_token(request)
    if not status:
        return JsonResponse({'validation':'invalid token'})

    response =[]

    try:  
        queryset = Address.objects.all()
        for address in queryset:
            response.append({
                'address_id':address.id,
                'user_id':address.user_profile.id,
                'building_name':address.building_name,
                'street_name':address.street_name,
                'locality':address.locality,
                'city':address.city,
                'district':address.district,
            })
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def delete_address(request):
    params = json.loads(request.body)

    address_id = params.get('address_id')

    try:
        if valid_integer(address_id):return JsonResponse({'validation':'enter valid address_id,must be a integer'})  

        add_obj = Address.objects.get(id = address_id).delete()
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_addresses_by_user_id(request):
    params = json.loads(request.body)
    response = []

    user_id = params.get('user_id')

    try:
        if valid_integer(user_id):return JsonResponse({'validation':'enter valid user_id,must be a integer'})  

        user_obj = Userprofile.objects.get(id=user_id)

        for address in user_obj.addresses.all():
            response.append({
                'user_id':address.user_profile.id,
                'username':address.user_profile.user.username,
                'address_id':address.id,
                'building_name':address.building_name,
                'street_name':address.street_name,
                'locality':address.locality,
                'city':address.city,
                'district':address.district,
                'state':address.state,
                'pincode':address.pincode
            })
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        if valid_string(username):return JsonResponse({'validation':'enter valid username ,must be a string'})   
        elif valid_string(password):return JsonResponse({'validation':'enter valid password,must be a string'})         
                
        user = authenticate(request, username=username, password=password)#authenticate by username & password
        if user is not None:
            auth_login(request, user)
            
            payload = {'user_id':2,'exp':datetime.utcnow() + timedelta(seconds = 864000)}   
            token = jwt.encode(payload, "SECRET_KEY",algorithm='HS256').decode("utf-8")#generate token
            return JsonResponse({'validation':'success','status':True,'token': token})#send response
        else:
            return JsonResponse({'validation':str(e),'status':False})

    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def change_user_password(request):
    params = request.POST

    username = params.get('username') 
    old_password = params.get('old_password')
    new_password = params.get('new_password')
    confirm_new_password = params.get('confirm_new_password')

    try:
        if valid_string(username):return JsonResponse({'validation':'enter valid username ,must be a string'})   
        elif valid_string(old_password):return JsonResponse({'validation':'enter valid old_password,must be a string'})  
        elif valid_string(new_password):return JsonResponse({'validation':'enter valid new_password,must be a string'})  
        elif valid_string(confirm_new_password):return JsonResponse({'validation':'enter valid confirm_new_password,must be a string'})  
        
        with transaction.atomic():
            user =  get_user_model().objects.filter(username = username).exists()
            if not user:
                return JsonResponse({'response':'not a user','status':user})

            user =  get_user_model().objects.get(username = username)
            check_password = user.check_password(old_password) 

            if not check_password:
                return JsonResponse({'response':'wrong password','status':check_password})
            if not (new_password == confirm_new_password):
                return JsonResponse({'response':('missmatch password',new_password,confirm_new_password),'status':False})

            user.set_password(new_password)
            user.save()
            return JsonResponse({'response':'successfully change password','status':True})

    except Exception as e:
            return JsonResponse({'response':str(e),'status':False})
            #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def forgot_user_password(request):
    params = request.POST

    username = params.get('username') 
    mobile_number = params.get('mobile_number')
    new_password = params.get('new_password')
    confirm_new_password = params.get('confirm_new_password')
    otp = int(params.get('otp'))
    number = 123456

    try:
        if valid_string(username):return JsonResponse({'validation':'enter valid username ,must be a string'})        
        elif valid_mobile_number(mobile_number):return JsonResponse({'validation':'enter valid mobile_number ,must be a string and 10 digit'})    
        elif valid_string(new_password):return JsonResponse({'validation':'enter valid new_password,must be a string'})  
        elif valid_string(confirm_new_password):return JsonResponse({'validation':'enter valid confirm_new_password,must be a string'})  
        elif valid_integer(otp):return JsonResponse({'validation':'enter valid otp,must be a integer'})  
        
        with transaction.atomic():
                
            user = get_user_model().objects.filter(username = username).exists()
            if not user:
                return JsonResponse({'response':'not a user','status':user})
            user = get_user_model().objects.get(username = username)

            if user:
                user_obj = Userprofile.objects.get(mobile_number = mobile_number)
                mobile_obj = user_obj.mobile_number
                
                if mobile_obj != mobile_number:
                    return JsonResponse({'response':'incorrect mobile number','status':False})

                if otp != number:
                    return JsonResponse({'response':'incorrect otp','status':False})

                if new_password != confirm_new_password:
                    return JsonResponse({'response':('missmatch password',new_password,confirm_new_password),'status':False})
                
                user.set_password(confirm_new_password)
                user.save()
                return JsonResponse({'response':'successfully change password','status':True})

    except Exception as e:
        return JsonResponse({'response':str(e),'status':False})
            #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def send_email(request):
    params = json.loads(request.body)
    sub = params.get('sub')
    body = params.get('body')
    receiver1 = params.get('receiver1')
    receiver2 = params.get('receiver2')
  
    if valid_string(sub):return JsonResponse({'validation':'enter valid sub,must be a string'})   
    elif valid_string(body):return JsonResponse({'validation':'enter valid body,must be a string'})   
    elif valid_email(receiver1):return JsonResponse({'validation':'enter valid email,must be a string'})   
    elif valid_email(receiver2):return JsonResponse({'validation':'enter valid email,must be a string'})   

    receiver = [receiver1,receiver2]
    if sub and body and receiver:
        try:
            send_mail(sub,body,EMAIL_HOST_USER,receiver,fail_silently=False)

        except BadHeaderError:
            return JsonResponse({'response':'invalid header found'})
        return JsonResponse({'response':'successfully send email','status':True})
    else:
        return JsonResponse({'response':'make sure all fields are entered and valid'})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def send_mass_email(request):
    params = json.loads(request.body)
    sub1 = params.get('sub1')
    body1 = params.get('body1')
    sub2 = params.get('sub2')
    body2 = params.get('body2')
    receiver1 = params.get('receiver1')
    receiver2 = params.get('receiver2')

    msg1 = (sub1,body1,EMAIL_HOST_USER,[receiver1])
    msg2 = (sub2,body2,EMAIL_HOST_USER,[receiver2])
   
    if valid_string(sub1):return JsonResponse({'validation':'enter valid sub1,must be a string'})   
    elif valid_string(body1):return JsonResponse({'validation':'enter valid body1,must be a string'})  
    elif valid_string(sub2):return JsonResponse({'validation':'enter valid sub2,must be a string'})   
    elif valid_string(body2):return JsonResponse({'validation':'enter valid body2,must be a string'})   
    elif valid_email(receiver1):return JsonResponse({'validation':'enter valid email,must be a string'})   
    elif valid_email(receiver2):return JsonResponse({'validation':'enter valid email,must be a string'})      

    if msg1 and msg2:
        try:
            send_mass_mail((msg1,msg2),fail_silently=False)
        except BadHeaderError:
                return JsonResponse({'response':'invalid header found'})
        return JsonResponse({'response':'successfully send email','status':True})
    else:
        return JsonResponse({'response':'make sure all fields are entered and valid'})
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def send_email_message(request):
    params = json.loads(request.body)
    sub = params.get('sub')
    body = params.get('body')
    receiver = params.get('receiver')
    bcc_receiver = params.get('bcc_receiver')
    cc_receiver = params.get('cc_receiver')

    if valid_string(sub):return JsonResponse({'validation':'enter valid sub,must be a string'})   
    elif valid_string(body):return JsonResponse({'validation':'enter valid body,must be a string'})   
    elif valid_email(receiver):return JsonResponse({'validation':'enter valid email,must be a string'})   
    elif valid_email(bcc_receiver):return JsonResponse({'validation':'enter valid email,must be a string'})   
    elif valid_email(cc_receiver):return JsonResponse({'validation':'enter valid email,must be a string'})   

    if sub and body and receiver:
        try:
            mail_obj = EmailMessage(sub,body,EMAIL_HOST_USER,[receiver],[bcc_receiver],
                headers={'Message-ID': 'abc'},cc=[cc_receiver],reply_to=[bcc_receiver])
            fd = open('manage.py', 'r')
            mail_obj.attach('manage.py', fd.read(), 'text/plain')
            mail_obj.send()
        except BadHeaderError:
                return JsonResponse({'response':'invalid header found'})
        return JsonResponse({'response':'successfully send email with attachment','status':True})
    else:
        return JsonResponse({'response':'make sure all fields are entered and valid'})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # def assign_permissions_to_users(request):
    #     # username = request.POST['username']
    #     # password = request.POST['password']
    #     user_id = request.POST['user_id']
        
    #     try:
    #         user=get_user_model().objects.get(id = 6)   

    #         return JsonResponse({'validation':'success','msg':'successfully assign permissions','status':True}) 
    #         # else:
    #         #     return JsonResponse({'validation':'unsuccess','msg':'user not exist','status':False}) 
    #     except Exception as e:
    #         return JsonResponse({'response':str(e),'status':False})
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_all_permissions_names(request):
    response=[]
    queryset=Permission.objects.all()
    for x in queryset:
        response.append(x.name)
    return JsonResponse({'status':response})
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def assign_selected_permission_to_user(request): 
    user_id = request.POST['user_id']  
    permission_id = request.POST['permission_id']

    try:
        user=get_user_model().objects.get(id = user_id)  

        if user is not None: 
            permissions = Permission.objects.get(id=permission_id)
            user.user_permissions.add(permissions)
            user.save()
            print(user.has_perm("Can view userprofile"))
            return JsonResponse({'validation':'success','msg':'successfully assign selected permissions to user','status':True}) 
        else:
            return JsonResponse({'validation':'unsuccess','msg':'user not exist','status':False}) 

    except Exception as e:
        return JsonResponse({'response':str(e),'status':False})
     # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def assign_all_permissions_to_users(request): 
    user_id = request.POST['user_id']   

    try:
        user=get_user_model().objects.get(id = user_id)  

        if user is not None: 
            queryset = Permission.objects.all()
            for permission in queryset:
                user.user_permissions.add(permission)
            user.save()
            print(user.has_perm("Can view userprofile"))
            return JsonResponse({'validation':'success','msg':'successfully assign all permissions to user','status':True}) 
        else:
            return JsonResponse({'validation':'unsuccess','msg':'user not exist','status':False}) 

    except Exception as e:
        return JsonResponse({'response':str(e),'status':False})
     # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def remove_permissions_to_users(request): 
    user_id = request.POST['user_id']   

    try:
        user=get_user_model().objects.get(id = user_id)  

        if user is not None: 
            queryset = Permission.objects.all()
            for permission in queryset:
                user.user_permissions.remove(permission)
            user.save()
            return JsonResponse({'validation':'success','msg':'successfully remove all permissions to user','status':True}) 
        else:
            return JsonResponse({'validation':'unsuccess','msg':'user not exist','status':False}) 

    except Exception as e:
        return JsonResponse({'response':str(e),'status':False})
     # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



