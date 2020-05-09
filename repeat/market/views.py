# from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
from django.db import transaction
from validator import *

# Create your views here.
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
