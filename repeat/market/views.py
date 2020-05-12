# from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
from django.db import transaction
from validator import *
from django.contrib.auth import authenticate, login
# Create your views here.
from django.contrib.auth.decorators import login_required

def createstore(request):
    params = request.POST
    try:
        storename = params.get('storename')
        storeaddress = params.get('storeaddress')
        storelocation = params.get('storelocation')
        storelatitude = float(params.get('storelatitude'))
        storelongitude = float(params.get('storelongitude'))
        storecity = params.get('storecity')
        storestate = params.get('storestate')
        storeimage = request.FILES.get('storeimage')

        if validstring(storename): return JsonResponse({'validation':'enter valid storename,must be string'})
        elif validstring(storeaddress): return JsonResponse({'validation':'enter valid storeaddress,must be string'})
        elif validstring(storelocation): return JsonResponse({'validation':'enter valid storelocation,must be string'})
        elif validfloat(storelatitude): return JsonResponse({'validation':'enter valid storelatitude,must float'})
        elif validfloat(storelongitude): return JsonResponse({'validation':'enter valid storelongitude,must be float'})
        elif validstring(storecity): return JsonResponse({'validation':'enter valid storecity,must be string'})
        elif validstring(storestate): return JsonResponse({'validation':'enter valid storestate,must string'})
        elif validstring(storestate): return JsonResponse({'validation':'enter valid storestate,must string'})
        elif validimage(storeimage): return JsonResponse({'validation':'select valid image file,must be a valid format'})

        with transaction.atomic():
            createstoreobj = Store.objects.create(
                storename = storename,
                storeaddress = storeaddress,
                storelocation = storelocation,
                storelatitude = storelatitude,
                storelongitude = storelongitude,
                storecity = storecity,
                storestate = storestate,
                storeimage = storeimage
            )
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def updatestore(request):
    params = request.POST
    try:
        storeid = params.get('storeid')
        storename = params.get('storename')
        storeaddress = params.get('storeaddress')
        storelocation = params.get('storelocation')
        storelatitude = float(params.get('storelatitude'))
        storelongitude = float(params.get('storelongitude'))
        storecity = params.get('storecity')
        storestate = params.get('storestate')
        storeimage = request.FILES.get('storeimage')

        if validstring(storename): return JsonResponse({'validation':'enter valid storename,must be string'})
        elif validstring(storeaddress): return JsonResponse({'validation':'enter valid storeaddress,must be string'})
        elif validstring(storelocation): return JsonResponse({'validation':'enter valid storelocation,must be string'})
        elif validfloat(storelatitude): return JsonResponse({'validation':'enter valid storelatitude,must float'})
        elif validfloat(storelongitude): return JsonResponse({'validation':'enter valid storelongitude,must be float'})
        elif validstring(storecity): return JsonResponse({'validation':'enter valid storecity,must be string'})
        elif validstring(storestate): return JsonResponse({'validation':'enter valid storestate,must string'})
        elif validstring(storestate): return JsonResponse({'validation':'enter valid storestate,must string'})
        elif validimage(storeimage): return JsonResponse({'validation':'select valid image file,must be a valid format'})

        with transaction.atomic():
            storeobj = Store.objects.get(id = storeid)
            print(storeobj)
            storeobj.storename = storename
            storeobj.storeaddress = storeaddress
            storeobj.storelocation = storelocation
            storeobj.storelatitude = storelatitude
            print(storelatitude)
            storeobj.storelongitude = storelongitude
            storeobj.storecity = storecity
            storeobj.storestate = storestate
            storeobj.storeimage = storeimage
            storeobj.save()

            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def getstore(request):
    params = json.loads(request.body)
    response =[]
    try:
        storeid = params.get('storeid')
        if validinteger(storeid): return JsonResponse({'validation':'enter valid storeid,must be int'})

        obj = Store.objects.get(id=storeid)

        response.append({
            'storeid' :obj.id,
            'storename' :obj.storename,
            'storeaddress' :obj.storeaddress,
            'storelocation' :obj.storelocation,
            'storelatitude' :obj.storelatitude,
            'storelongitude' :obj.storelongitude,
            'storecity' :obj.storecity,
            'storestate' :obj.storestate,
            'storeimage' :str(obj.storeimage),
            'createdon' :obj.createdon
        })
        return JsonResponse({'validation':'success','responsse':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def getallstore(request):
    response = []
    try:
        obj = Store.objects.all()

        for store in obj:
            response.append({
                'storeid' :store.id,
                'storename' :store.storename,
                'storeaddress' :store.storeaddress,
                'storelocation' :store.storelocation,
                'storelatitude' :store.storelatitude,
                'storelongitude' :store.storelongitude,
                'storecity' :store.storecity,
                'storestate' :store.storestate,
                'storeimage' :str(store.storeimage),
                'createdon' :store.createdon
            })
        return JsonResponse({'validation':'success','responsse':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def deletestore(request):
    params = json.loads(request.body)
    try:
        storeid = params.get('storeid')
        if validinteger(storeid): return JsonResponse({'validation':'enter valid storeid,must be int'})
       
        obj = Store.objects.get(id=storeid).delete()
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?
    
def createcategory(request):
    params = request.POST
    try:
        storeid = int(params.get('storeid'))
        categoryname = params.get('categoryname')
        productimage = request.FILES.get('categoryimage')

        if validinteger(storeid): return JsonResponse({'validation':'enter valid storeid,must be int'})
        elif validstring(categoryname): return JsonResponse({'validation':'enter valid categoryname,must string'})
        elif validimage(categoryimage): return JsonResponse({'validation':'select valid image file,must be a valid format'})

        with transaction.atomic():
            storeobj = Store.objects.get(id = storeid)
            createcategoryobj = Category.objects.create(
                store = storeobj,
                categoryname = categoryname,
                categoryimage = categoryimage,
            )
            print(categoryobj)
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?
    
def updatecategory(request):
    params = request.POST

    categoryid = int(params.get('categoryid'))
    categoryname = params.get('categoryname')
    categoryimage = request.FILES.get('categoryimage')

    try:
        if validinteger(categoryid): return JsonResponse({'validation':'enter valid categoryid,must be int'})
        elif validstring(categoryname): return JsonResponse({'validation':'enter valid categoryname,must string'})
        elif validimage(categoryimage): return JsonResponse({'validation':'select valid image file,must be a valid format'})
       
        with transaction.atomic():
            obj = Category.objects.get(id = categoryid)
            obj.categoryname = categoryname
            obj.categoryimage = categoryimage
            obj.save()
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def getcategory(request):
    params = json.loads(request.body)
    response = []

    categoryid = params.get('categoryid')
    if validinteger(categoryid): return JsonResponse({'validation':'enter valid categoryid,must be int'})

    try:
        obj = Category.objects.get(id = categoryid)
        response.append({
            'storeid':obj.store.id,
            'categoryid':obj.id,
            'categoryname':obj.categoryname,
            'storename':obj.store.storename,
            'categoryimage':str(obj.categoryimage),
            'createdon':obj.createdon
        })
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def getallcategory(request):
    response = []

    try:
        obj = Category.objects.all()

        for categories in obj:
            response.append({
                'categoryid':categories.id,
                'categoryname':categories.categoryname,
                'createdon':categories.createdon
            })
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def deletecategory(request):
    params = json.loads(request.body)

    categoryid = params.get('categoryid')

    try:
        if validinteger(categoryid): return JsonResponse({'validation':'enter valid categoryid,must be int'})
        obj = Category.objects.get(id = categoryid).delete()
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def createsubcategory(request):
    params = request.POST

    storeid = int(params.get('storeid'))
    categoryid = int(params.get('categoryid'))
    subcategoryname = params.get('subcategoryname')
    subcategoryimage = request.FILES.get('subcategoryimage')
    createdon = params.get('createdon')

    try:
        if validinteger(storeid): return JsonResponse({'validation':'enter valid storid,must be int'})
        elif validinteger(categoryid): return JsonResponse({'validation':'enter valid categoryid,must be int'})
        elif validstring(subcategoryname): return JsonResponse({'validation':'enter valid subcategoryname,must string'})
        elif validimage(subcategoryimage): return JsonResponse({'validation':'select valid image file,must be a valid format'})
       
        with transaction.atomic():
            storeobj = Store.objects.get(id = storeid)
            categoryobj = Category.objects.get(id = categoryid)
            createsubcategoryobj = Subcategory.objects.create(
                store = storeobj,
                category = categoryobj,
                subcategoryname = subcategoryname,
                subcategoryimage = subcategoryimage
            )
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def updatesubcategory(request):
    params = request.POST

    subcategoryid = int(params.get('subcategoryid'))
    subcategoryname = params.get('subcategoryname')
    subcategoryimage = request.FILES.get('subcategoryimage')

    try:
        if validinteger(subcategoryid): return JsonResponse({'validation':'enter valid subcategoryid,must be int'})
        elif validstring(subcategoryname): return JsonResponse({'validation':'enter valid subcategoryname,must string'})
        elif validimage(subcategoryimage): return JsonResponse({'validation':'select valid image file,must be a valid format'})
       
        with transaction.atomic():
            obj = Subcategory.objects.get(id = subcategoryid)
            obj.subcategoryname = subcategoryname
            obj.subcategoryimage = subcategoryimage
            obj.save()
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++?

def getsubcategory(request):
    params = json.loads(request.body)
    response = []

    subcategoryid = params.get('subcategoryid')
    
    try:
        if validinteger(subcategoryid): return JsonResponse({'validation':'enter valid subcategoryid,must be int'})

        obj = Subcategory.objects.get(id=subcategoryid)
        response.append({
            'subcategoryid':obj.id,
            'categoryid':obj.category.id,
            'storeid':obj.store.id,
            'subcategoryname':obj.subcategoryname,
            'categoryname':obj.category.categoryname,
            'storename':obj.store.storename,
            'subcategoryimage':str(obj.subcategoryimage),
            'createdon':obj.createdon
        })
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def getallsubcategory(request):
    response =[]

    try:
        obj = Subcategory.objects.all()

        for subcategories in obj:
            response.append({
                'subcategoryid':subcategories.id,
                'subcategoryname':subcategories.subcategoryname,
                'createdon':subcategories.createdon
            })
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def deletesubcategory(request):
    params = json.loads(request.body)

    subcategoryid = params.get('subcategoryid')
    
    try:
        if validinteger(subcategoryid): return JsonResponse({'validation':'enter valid subcategoryid,must be int'})
       
        obj = Subcategory.objects.get(id=subcategoryid).delete()
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def createproduct(request):
    params = request.POST   

    storeid = int(params.get('storeid'))
    subcategoryid = int(params.get('subcategoryid'))
    productname = params.get('productname')
    productquantity = int(params.get('productquantity'))
    productprice = float(params.get('productprice'))
    productdiscountprice = float(params.get('productdiscountprice'))
    productdescription = params.get('productdescription')
    productimage = request.FILES.get('productimage')

    try:
        if validinteger(storeid): return JsonResponse({'validation':'enter valid storeid,must be int'})
        elif validinteger(subcategoryid): return JsonResponse({'validation':'enter valid subcategoryid,must be int'})
        elif validstring(productname): return JsonResponse({'validation':'enter valid productname,must string'})
        elif validinteger(productquantity): return JsonResponse({'validation':'enter valid productquantity,must be int'})
        elif validfloat(productprice): return JsonResponse({'validation':'enter valid productprice,must be float'})
        elif validfloat(productdiscountprice): return JsonResponse({'validation':'enter valid productdiscountprice,must be float'})
        elif validstring(productdescription): return JsonResponse({'validation':'enter valid productdescription,must string'})
        elif validimage(productimage): return JsonResponse({'validation':'select valid image file,must be a valid format'})

        with transaction.atomic():
            storeobj = Store.objects.get(id=storeid)
            subcategoryobj = Subcategory.objects.get(id=subcategoryid)
            createproductobj = Product.objects.create(
                store = storeobj,
                subcategory = subcategoryobj,
                productname = productname,
                productquantity =productquantity,
                productprice = productprice,
                productdiscountprice = productdiscountprice,
                productdescription = productdescription,
                productimage = productimage
            )
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def updateproduct(request):
    params = request.POST

    productid = int(params.get('productid'))
    # subcategoryid = int(params.get('subcategoryid'))
    productname = params.get('productname')
    productquantity = int(params.get('productquantity'))
    productprice = float(params.get('productprice'))
    productdiscountprice = float(params.get('productdiscountprice'))
    productdescription = params.get('productdescription')
    productimage = request.FILES.get('productimage')

    try:
        if validinteger(productid): return JsonResponse({'validation':'enter valid productid,must be int'})
        # elif validinteger(subcategoryid): return JsonResponse({'validation':'enter valid subcategoryid,must be int'})
        elif validstring(productname): return JsonResponse({'validation':'enter valid productname,must string'})
        elif validinteger(productquantity): return JsonResponse({'validation':'enter valid productquantity,must be int'})
        elif validfloat(productprice): return JsonResponse({'validation':'enter valid productprice,must be float'})
        elif validfloat(productdiscountprice): return JsonResponse({'validation':'enter valid productdiscountprice,must be float'})
        elif validstring(productdescription): return JsonResponse({'validation':'enter valid productdescription,must string'})
        elif validimage(productimage): return JsonResponse({'validation':'select valid image file,must be a valid format'})

        with transaction.atomic():

            obj = Product.objects.get(id=productid)
            obj.productname = productname
            obj.productquantity =productquantity
            obj.productprice = productprice
            obj.productdiscountprice = productdiscountprice
            obj.productdescription = productdescription
            obj.productimage = productimage
            obj.save()
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def getproduct(request):
    params = json.loads(request.body)
    response = []

    productid = params.get('productid')

    try:
        if validinteger(productid): return JsonResponse({'validation':'enter valid productid,must be int'})

        obj = Product.objects.get(id=productid)
        response.append({
            'storeid':obj.store.id,
            'subcategoryid':obj.subcategory.id,
            'productid':obj.id,
            'productname':obj.productname,
            'subcategoryname':obj.subcategory.subcategoryname,
            'storename':obj.store.storename,
            'createdon':obj.createdon
        })
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def getallproduct(request):
    response = []

    try:
        obj = Product.objects.all()
        for products in obj:
            response.append({
                'productid':products.id,
                'productname':products.productname,
                'createdon':products.createdon
            })
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def deleteproduct(request):
    params = json.loads(request.body)

    productid = params.get('productid')

    try:
        if validinteger(productid): return JsonResponse({'validation':'enter valid productid,must be int'})

        obj = Product.objects.get(id = productid).delete()
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def createuser(request):
    params = json.loads(request.body)

    username = params.get('username')
    password = params.get('password')
    firstname = params.get('firstname')
    lastname = params.get('lastname')
    age = params.get('age')
    email = params.get('email')

    try:
        if validstring(username):return JsonResponse({'validation':'enter valid username ,must be a string'})   
        elif validstring(password):return JsonResponse({'validation':'enter valid password,must be a string'})  
        elif validstring(firstname):return JsonResponse({'validation':'enter valid first_name,must be a string'})   
        elif validstring(lastname):return JsonResponse({'validation':'enter valid last_name,must be a string'})    
        elif validinteger(age):return JsonResponse({'validation':'enter valid age,must be a integer'})
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
    email = params.get('email')

    try:
        if validstring(username):return JsonResponse({'validation':'enter valid username ,must be a string'})   
        elif validstring(password):return JsonResponse({'validation':'enter valid password,must be a string'})  
        elif validstring(firstname):return JsonResponse({'validation':'enter valid first_name,must be a string'})   
        elif validstring(lastname):return JsonResponse({'validation':'enter valid last_name,must be a string'})    
        elif validinteger(age):return JsonResponse({'validation':'enter valid age,must be a integer'})
        elif validemail(email):return JsonResponse({'validation':'enter valid email,must be a string'})   
        
        with transaction.atomic():
            obj = Userprofile.objects.get(id = userid)
            obj.user.username = username
            obj.user.password = password
            obj.firstname = firstname
            obj.lastname = lastname
            obj.age = age
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

def addfollowership(request):
    params = json.loads(request.body)

    userid = params.get('userid')
    storeid = params.get('storeid')

    try:
        if validinteger(userid):return JsonResponse({'validation':'enter valid userid,must be a integer'})  
        elif validinteger(storeid):return JsonResponse({'validation':'enter valid storeid,must be a integer'})  

        with transaction.atomic():
            userobj = Userprofile.objects.get(id = userid)
            storeobj = Store.objects.get(id = storeid)

            createfollowershipobj = Followership.objects.create(
                store = storeobj,
                user = userobj
            )
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def updatefollowership(request):
    params = json.loads(request.body)
    
    followershipid = params.get('followershipid')
    storeid = params.get('storeid')
    userid = params.get('userid')
    try:
        if validinteger(followershipid):return JsonResponse({'validation':'enter valid followershipid,must be a integer'})  
        elif validinteger(storeid):return JsonResponse({'validation':'enter valid storeid,must be a integer'})  
        elif validinteger(userid):return JsonResponse({'validation':'enter valid userid,must be a integer'})  

        with transaction.atomic():
            userobj = Userprofile.objects.get(id = userid)
            storeobj = Store.objects.get(id = storeid)

            obj = Followership.objects.get(id = followershipid)
            obj.store = storeobj
            obj.user = userobj
            obj.save()
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def getfollowersbystore(request):
    params = json.loads(request.body)
    response = []

    storeid = params.get('storeid')

    try:
        if validinteger(storeid):return JsonResponse({'validation':'enter valid storeid,must be a integer'})  

        storeobj = Store.objects.get(id = storeid)
        followerobj = storeobj.follower.all()
        for users in followerobj:
            response.append({
                'userid':users.user.id,
                'firstname':users.user.firstname
            })
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def getstoresbyfollower(request):
    params = json.loads(request.body)
    response = []

    userid = params.get('userid')

    try:
        if validinteger(userid):return JsonResponse({'validation':'enter valid userid,must be a integer'})  

        userobj =Userprofile.objects.get(id = userid)
        followingobj = userobj.following.all()
        for stores in followingobj:
            response.append({
                'storeid':stores.store.id,
                'storename':stores.store.storename
            })
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def removeuserbysomereason(request):
    params = json.loads(request.body)
     
    followershipid = params.get('followershipid')
    reason = params.get('reason')

    try:
        if validinteger(followershipid):return JsonResponse({'validation':'enter valid followershipid,must be a integer'})  
        elif validinteger(reason):return JsonResponse({'validation':'enter valid reason,must be a integer'})  

        followerobj = Followership.objects.get(id = followershipid)
        followerobj.user = None
        followerobj.reason = reason
        followerobj.save()
        return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def getallfollowerships(request):
    response = []

    try:
        followerobj = Followership.objects.all()

        for followers in followerobj:
            response.append(followers.getjson())
        return JsonResponse({'validation':'success','response':response,'status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
@login_required(login_url='/accounts/login/')
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


