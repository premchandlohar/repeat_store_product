from django.http import JsonResponse
import json
from .models import Userprofile,Address
from django.contrib.auth import get_user_model
from django.db import transaction
from validator import *
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.
from django.contrib.auth.decorators import login_required
import jwt
from datetime import timedelta,datetime 
from django.core.mail import send_mail,BadHeaderError,send_mass_mail,EmailMessage
# from repeat import settings
from django.conf import settings
from repeat.settings import EMAIL_HOST_USER




# Create your views here.
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
                username = username
            )
            user_obj.set_password(password)
            user_obj.save()

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
    print(mobile_number)
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
            obj = Userprofile.objects.get(id = user_id)
            obj.user.username = username
            obj.user.password = password
            obj.first_name = first_name
            obj.last_name = last_name
            obj.age = age
            obj.mobile_number = mobile_number
            obj.email = email
            obj.save()
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
        
        obj = Userprofile.objects.get(id = user_id)
        resposne.append({
            'user_id':obj.id,
            'usernsme':obj.user.username,
            'first_name':obj.first_name,
            'last_name':obj.last_name,
            'age':obj.age,
            'mobile_number':obj.mobile_number,
            "email":obj.email,
            'created_on':obj.created_on
        })
        return JsonResponse({'validation':'success','resposne':resposne,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_all_user(request):
    resposne = []

    try:      
        obj = Userprofile.objects.all()
        for users in obj:
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
        
        obj = Userprofile.objects.get(id = user_id).delete()
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
            obj = Address.objects.get(id = address_id)
            obj.building_name = building_name
            obj.street_name = street_name
            obj.locality = locality
            obj.city = city
            obj.district = district
            obj.state = state
            obj.pincode = pincode
            obj.save()
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

        obj = Address.objects.get(id = address_id)
        response.append({
            'address_id':obj.id,
            'building_name':obj.building_name,
            'street_name':obj.street_name,
            'locality':obj.locality,
            'city':obj.city,
            'district':obj.district,
            'state':obj.state,
            'pincode':obj.pincode
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
        obj = Address.objects.all()
        for address in obj:
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

        obj = Address.objects.get(id = address_id).delete()
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

# @login_required(login_url='/accounts/login/')
def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        if valid_string(username):return JsonResponse({'validation':'enter valid username ,must be a string'})   
        elif valid_string(password):return JsonResponse({'validation':'enter valid password,must be a string'})         
                
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            
            payload = {'user_id':2,'exp':datetime.utcnow() + timedelta(seconds = 864000)}   
            # print(payload)

            # payload = {}    
            # payload["user_id"] = 2
            # payload["exp"] = datetime.utcnow() + timedelta(seconds = 864000)      
            token = jwt.encode(payload, "SECRET_KEY",algorithm='HS256').decode("utf-8")
            return JsonResponse({'validation':'success','status':True,'token': token})
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

def login(request):
    m = get_user_model().objects.get(username=request.POST['username'])
    if m.password == request.POST['password']:
        request.session['user_id'] = m.id
        return JsonResponse({'response':'You\'re logged in.'})
    else:
        return JsonResponse({'response':"Your username and password didn't match."})
    #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def send_email(request):#in this multiple receiver and single sender whose send same msg(only one) for all receiver
    params = json.loads(request.body)
    sub = params.get('sub')
    body = params.get('body')
    # sender = params.get('sender')
    receiver1 = params.get('receiver1')
    receiver2 = params.get('receiver2')

    # if valid_email(sender):return JsonResponse({'validation':'enter valid email,must be a string'})   
    if valid_string(sub):return JsonResponse({'validation':'enter valid sub,must be a string'})   
    elif valid_string(body):return JsonResponse({'validation':'enter valid body,must be a string'})   
    elif valid_email(receiver1):return JsonResponse({'validation':'enter valid email,must be a string'})   
    elif valid_email(receiver2):return JsonResponse({'validation':'enter valid email,must be a string'})   

    receiver = [receiver1,receiver2]
    if sub and body and receiver:
        try:
            send_mail(sub,body,EMAIL_HOST_USER,receiver,fail_silently=False)
            # print(obj)
            # if (obj==1):
            #     return JsonResponse({'response':'successfully send email','status':True})

        except BadHeaderError:
            return JsonResponse({'response':'invalid header found'})
        return JsonResponse({'response':'successfully send email','status':True})
    else:
        return JsonResponse({'response':'make sure all fields are entered and valid'})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#in this multiple receiver and multiple sender whose send differnt differnt msg for differnt receiver(one for other one for anothr) 
def send_mass_email(request):
    params = json.loads(request.body)
    sub1 = params.get('sub1')
    body1 = params.get('body1')
    sub2 = params.get('sub2')
    body2 = params.get('body2')
    # sender = params.get('sender')
    receiver1 = params.get('receiver1')
    receiver2 = params.get('receiver2')
    print(sub1,body1)

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

        # Not all features of the EmailMessage class are available through the send_mail() and related wrapper functions.
        # If you wish to use advanced features, such as BCC’ed recipients, file attachments, or multi-part email, you’ll need to create EmailMessage instances directly.
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
                headers={'Message-ID': 'foo'},cc=[cc_receiver],reply_to=[bcc_receiver])
            fd = open('manage.py', 'r')
            mail_obj.attach('manage.py', fd.read(), 'text/plain')
            mail_obj.send()
        except BadHeaderError:
                return JsonResponse({'response':'invalid header found'})
        return JsonResponse({'response':'successfully send email with attachment','status':True})
    else:
        return JsonResponse({'response':'make sure all fields are entered and valid'})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




