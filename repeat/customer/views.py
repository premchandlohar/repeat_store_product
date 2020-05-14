from django.http import JsonResponse
import json
from .models import Userprofile,Address
from django.contrib.auth import get_user_model
from django.db import transaction
from validator import *
from django.contrib.auth import authenticate, login
# Create your views here.
from django.contrib.auth.decorators import login_required


# Create your views here.
def createuser(request):
    params = json.loads(request.body)

    username = params.get('username')
    password = params.get('password')
    firstname = params.get('firstname')
    lastname = params.get('lastname')
    age = params.get('age')
    mobilenumber = params.get('mobilenumber')
    email = params.get('email')

    try:
        if validstring(username):return JsonResponse({'validation':'enter valid username ,must be a string'})   
        elif validstring(password):return JsonResponse({'validation':'enter valid password,must be a string'})  
        elif validstring(firstname):return JsonResponse({'validation':'enter valid first_name,must be a string'})   
        elif validstring(lastname):return JsonResponse({'validation':'enter valid last_name,must be a string'})    
        elif validinteger(age):return JsonResponse({'validation':'enter valid age,must be a integer'})
        elif validmobilenumber(mobilenumber):return JsonResponse({'validation':'enter valid mobilenumber ,must be a string and 10 digit'})   
        elif validemail(email):return JsonResponse({'validation':'enter valid email,must be a string'})   
        
        with transaction.atomic():
            userobj =get_user_model().objects.create(
                username = username
            )
            userobj.set_password(password)
            userobj.save()

            userprofileobj = Userprofile.objects.create(
                user = userobj,
                firstname = firstname,
                lastname = lastname,
                age = age,
                mobilenumber = mobilenumber,
                email = email
            )
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def updateuser(request):
    params = json.loads(request.body)

    userid = params.get('userid')
    username = params.get('username')
    password = params.get('password')
    firstname = params.get('firstname')
    lastname = params.get('lastname')
    age = params.get('age')
    mobilenumber = params.get('mobilenumber')
    print(mobilenumber)
    email = params.get('email')

    try:
        if validstring(username):return JsonResponse({'validation':'enter valid username ,must be a string'})   
        elif validstring(password):return JsonResponse({'validation':'enter valid password,must be a string'})  
        elif validstring(firstname):return JsonResponse({'validation':'enter valid first_name,must be a string'})   
        elif validstring(lastname):return JsonResponse({'validation':'enter valid last_name,must be a string'})    
        elif validinteger(age):return JsonResponse({'validation':'enter valid age,must be a integer'}) 
        elif validmobilenumber(mobilenumber):return JsonResponse({'validation':'enter valid mobilenumber ,must be a string and 10 digit'})   
        elif validemail(email):return JsonResponse({'validation':'enter valid email,must be a string'})
        with transaction.atomic():
            obj = Userprofile.objects.get(id = userid)
            obj.user.username = username
            obj.user.password = password
            obj.firstname = firstname
            obj.lastname = lastname
            obj.age = age
            obj.mobilenumber = mobilenumber
            obj.email = email
            obj.save()
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def getuser(request):
    params = json.loads(request.body)
    resposne = []

    userid = params.get('userid')

    try:
        if validinteger(userid):return JsonResponse({'validation':'enter valid userid,must be a integer'})
        
        obj = Userprofile.objects.get(id = userid)
        resposne.append({
            'userid':obj.id,
            'usernsme':obj.user.username,
            'firstname':obj.firstname,
            'lastname':obj.lastname,
            'age':obj.age,
            'mobilenumber':obj.mobilenumber,
            "email":obj.email,
            'createdon':obj.createdon
        })
        return JsonResponse({'validation':'success','resposne':resposne,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def getalluser(request):
    resposne = []

    try:
        
        obj = Userprofile.objects.all()
        for users in obj:
            resposne.append({
                'userid':users.id,
                'usernsme':users.user.username,
                'firstname':users.firstname,
                'lastname':users.lastname,
                'mobilenumber':obj.mobilenumber,
                "email":users.email,
            })
        return JsonResponse({'validation':'success','resposne':resposne,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def deleteuser(request):
    params = json.loads(request.body)
    resposne = []

    userid = params.get('userid')

    try:
        if validinteger(userid):return JsonResponse({'validation':'enter valid userid,must be a integer'})
        
        obj = Userprofile.objects.get(id = userid).delete()
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def createaddress(request):
    params = json.loads(request.body)

    userid = params.get('userid') 
    buildingname = params.get('buildingname')
    streetname = params.get('streetname')
    locality = params.get('locality')
    city = params.get('city')
    district = params.get('district')   
    state = params.get('state')
    pincode = params.get('pincode')

    try:
        if validinteger(userid):return JsonResponse({'validation':'enter valid userid,must be a integer'})  
        elif validstring(buildingname):return JsonResponse({'validation':'enter valid buildingname,must be a string'})    
        elif validstring(streetname):return JsonResponse({'validation':'enter valid streetname,must be a string'})    
        elif validstring(locality):return JsonResponse({'validation':'enter valid locality,must be a string'})    
        elif validstring(city):return JsonResponse({'validation':'enter valid city,must be a string'})    
        elif validstring(district):return JsonResponse({'validation':'enter valid district,must be a string'})    
        elif validstring(state):return JsonResponse({'validation':'enter valid state,must be a string'})    
        elif validpincode(pincode):return JsonResponse({'validation':'enter valid pincode,must be a integer and only 6 digit required'})    
     
        with transaction.atomic():
            userobj = Userprofile.objects.get(id = userid)
            createaddressobj = Address.objects.create(
                userprofile = userobj,
                buildingname = buildingname,
                streetname = streetname,
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

def updateaddress(request):
    params = json.loads(request.body)

    addressid = params.get('addressid')
    buildingname = params.get('buildingname')
    streetname = params.get('streetname')
    locality = params.get('locality')
    city = params.get('city')
    district = params.get('district')
    state = params.get('state')
    pincode = params.get('pincode')

    try:
        if validinteger(addressid):return JsonResponse({'validation':'enter valid addressid,must be a integer'})  
        elif validstring(buildingname):return JsonResponse({'validation':'enter valid buildingname,must be a string'})    
        elif validstring(streetname):return JsonResponse({'validation':'enter valid streetname,must be a string'})    
        elif validstring(locality):return JsonResponse({'validation':'enter valid locality,must be a string'})    
        elif validstring(city):return JsonResponse({'validation':'enter valid city,must be a string'})    
        elif validstring(district):return JsonResponse({'validation':'enter valid district,must be a string'})    
        elif validstring(state):return JsonResponse({'validation':'enter valid state,must be a string'})    
        elif validpincode(pincode):return JsonResponse({'validation':'enter valid pincode,must be a integer and only 6 digit required'})    
     
        with transaction.atomic():
            obj = Address.objects.get(id = addressid)
            obj.buildingname = buildingname
            obj.streetname = streetname
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

def getaddress(request):
    params = json.loads(request.body)
    response =[]

    addressid = params.get('addressid')

    try:
        if validinteger(addressid):return JsonResponse({'validation':'enter valid addressid,must be a integer'})  

        obj = Address.objects.get(id = addressid)
        response.append({
            'addressid':obj.id,
            'buildingname':obj.buildingname,
            'streetname':obj.streetname,
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

def getalladdress(request):
    response =[]

    try:  
        obj = Address.objects.all()
        for address in obj:
            response.append({
                'addressid':address.id,
                'userid':address.userprofile.id,
                'buildingname':address.buildingname,
                'streetname':address.streetname,
                'locality':address.locality,
                'city':address.city,
                'district':address.district,
            })
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def deleteaddress(request):
    params = json.loads(request.body)

    addressid = params.get('addressid')

    try:
        if validinteger(addressid):return JsonResponse({'validation':'enter valid addressid,must be a integer'})  

        obj = Address.objects.get(id = addressid).delete()
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def getaddressesbyuserid(request):
    params = json.loads(request.body)
    response = []

    userid = params.get('userid')

    try:
        if validinteger(userid):return JsonResponse({'validation':'enter valid userid,must be a integer'})  

        userobj = Userprofile.objects.get(id=userid)
        for address in userobj.addresses.all():
            response.append({
                'userid':address.userprofile.id,
                'username':address.userprofile.user.username,
                'addressid':address.id,
                'buildingname':address.buildingname,
                'streetname':address.streetname,
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
def userlogin(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        if validstring(username):return JsonResponse({'validation':'enter valid username ,must be a string'})   
        elif validstring(password):return JsonResponse({'validation':'enter valid password,must be a string'})  
        
        with transaction.atomic():
                
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
                return JsonResponse({'validation':'success','status':True})
            else:
                return JsonResponse({'validation':str(e),'status':False})

    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def changeuserpassword(request):
    params = request.POST

    username = params.get('username') 
    oldpassword = params.get('oldpassword')
    newpassword = params.get('newpassword')
    confirmnewpassword = params.get('confirmnewpassword')

    try:
        if validstring(username):return JsonResponse({'validation':'enter valid username ,must be a string'})   
        elif validstring(oldpassword):return JsonResponse({'validation':'enter valid oldpassword,must be a string'})  
        elif validstring(newpassword):return JsonResponse({'validation':'enter valid newpassword,must be a string'})  
        elif validstring(confirmnewpassword):return JsonResponse({'validation':'enter valid confirmnewpassword,must be a string'})  
        
        with transaction.atomic():
            user =  get_user_model().objects.filter(username = username).exists()
            if not user:
                return JsonResponse({'response':'not a user','status':user})

            user =  get_user_model().objects.get(username = username)
            check_password = user.check_password(oldpassword) 

            if not check_password:
                return JsonResponse({'response':'wrong password','status':check_password})
            if not (newpassword == confirmnewpassword):
                return JsonResponse({'response':('missmatch password',newpassword,confirmnewpassword),'status':False})

            user.set_password(newpassword)
            user.save()
            return JsonResponse({'response':'successfuly change password','status':True})

    except Exception as e:
            return JsonResponse({'response':str(e),'status':False})
            #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def forgetuserpassword(request):
    params = request.POST

    username = params.get('username') 
    mobilenumber = params.get('mobilenumber')
    newpassword = params.get('newpassword')
    confirmnewpassword = params.get('confirmnewpassword')
    otp = int(params.get('otp'))
    number = 123456

    try:
        if validstring(username):return JsonResponse({'validation':'enter valid username ,must be a string'})        
        elif validmobilenumber(mobilenumber):return JsonResponse({'validation':'enter valid mobilenumber ,must be a string and 10 digit'})    
        elif validstring(newpassword):return JsonResponse({'validation':'enter valid newpassword,must be a string'})  
        elif validstring(confirmnewpassword):return JsonResponse({'validation':'enter valid confirmnewpassword,must be a string'})  
        elif validinteger(otp):return JsonResponse({'validation':'enter valid otp,must be a integer'})  
        
        with transaction.atomic():
                
            user = get_user_model().objects.filter(username = username).exists()
            if not user:
                return JsonResponse({'response':'not a user','status':user})
            user = get_user_model().objects.get(username = username)

            if user:
                userobj = Userprofile.objects.get(mobilenumber = mobilenumber)
                mobileobj = userobj.mobilenumber
                
                if mobileobj != mobilenumber:
                    return JsonResponse({'response':'incorrect mobile number','status':False})

                if otp != number:
                    return JsonResponse({'response':'incorrect otp','status':False})

                if newpassword != confirmnewpassword:
                    return JsonResponse({'response':('missmatch password',newpassword,confirmnewpassword),'status':False})
                
                user.set_password(confirmnewpassword)
                user.save()
                return JsonResponse({'response':'successfuly change password','status':True})

    except Exception as e:
        return JsonResponse({'response':str(e),'status':False})
            #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

       



