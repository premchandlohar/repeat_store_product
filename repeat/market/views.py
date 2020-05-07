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
            createobj = Store.objects.create(
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