from django.http import JsonResponse
import json
from .models import Bankprofile
from validator import *
from django.db import transaction


# Create your views here.
def establish_new_bank(request):
    params = json.loads(request.body)

    #get input from params
    state = params.get('state')
    bank_name = params.get('bank_name')
    ifsc_code = params.get('ifsc_code')
    branch = params.get('branch')
    address = params.get('address')
    contact = params.get('contact')
    city = params.get('city')
    district = params.get('district')

    #valided there fields
    try:
        if valid_string(state):return JsonResponse({'validation':'enter valid state ,must be a string'})   
        elif valid_string(bank_name):return JsonResponse({'validation':'enter valid bank_name,must be a string'})  
        elif valid_ifsc_code(ifsc_code):return JsonResponse({'validation':'enter valid ifsc_code,must be a string & digit must be 11'})   
        elif valid_string(branch):return JsonResponse({'validation':'enter valid branch,must be a string'})    
        elif valid_string(address):return JsonResponse({'validation':'enter valid address,must be a string'})
        elif valid_mobile_number(contact):return JsonResponse({'validation':'enter valid contact ,must be a string and 10 digit'})   
        elif valid_string(city):return JsonResponse({'validation':'enter valid city ,must be a string'})   
        elif valid_string(district):return JsonResponse({'validation':'enter valid district,must be a string'})   
        
        with transaction.atomic():#used for all field is valid then and only then create obj
            bank_obj = Bankprofile.objects.create(#create the details
                state = state,
                bank_name = bank_name,
                ifsc_code = ifsc_code,
                branch = branch,
                address = address,
                contact = contact,
                city = city,
                district = district
            )
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def update_bank_details(request):
    params = json.loads(request.body)

    bank_id = params.get('bank_id')
    state = params.get('state')
    bank_name = params.get('bank_name')
    ifsc_code = params.get('ifsc_code')
    branch = params.get('branch')
    address = params.get('address')
    contact = params.get('contact')
    city = params.get('city')
    district = params.get('district')

    try:
        if valid_integer(bank_id):return JsonResponse({'validation':'enter valid bank_id ,must be a integer'})   
        elif valid_string(state):return JsonResponse({'validation':'enter valid state ,must be a string'})   
        elif valid_string(bank_name):return JsonResponse({'validation':'enter valid bank_name,must be a string'})  
        elif valid_ifsc_code(ifsc_code):return JsonResponse({'validation':'enter valid ifsc_code,must be a string & digit must be 11'})   
        elif valid_string(branch):return JsonResponse({'validation':'enter valid branch,must be a string'})    
        elif valid_string(address):return JsonResponse({'validation':'enter valid address,must be a string'})
        elif valid_mobile_number(contact):return JsonResponse({'validation':'enter valid contact ,must be a string and 10 digit'})   
        elif valid_string(city):return JsonResponse({'validation':'enter valid city ,must be a string'})   
        elif valid_string(district):return JsonResponse({'validation':'enter valid district,must be a string'})   
        
        with transaction.atomic():
            bank_obj = Bankprofile.objects.create(
                state = state,
                bank_name = bank_name,
                ifsc_code = ifsc_code,
                branch = branch,
                address = address,
                contact = contact,
                city = city,
                district = district
            )
            return JsonResponse({'validation':'success','status':True})
    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_bank_details_by_ifsc_code(request):
    params = json.loads(request.body)
    response = []

    ifsc_code = params.get('ifsc_code')

    #valided the ifsc code
    if valid_ifsc_code(ifsc_code):return JsonResponse({'validation':'enter valid ifsc_code,must be a string & digit must be 11'})   
    try:
        bank_obj = Bankprofile.objects.get(ifsc_code=ifsc_code)#create object of specific bank
        # print(bank_obj)
        if bank_obj:#if object is true then append a there field into response list
            response.append({
                "state":bank_obj.state,
                "bank_name":bank_obj.bank_name,
                "ifsc_code":bank_obj.ifsc_code,
                "branch":bank_obj.branch,
                "address":bank_obj.address,
                "contact":bank_obj.contact,
                "city":bank_obj.city,
                "district":bank_obj.district
            })
            return JsonResponse({'validation':'success','response':response,'status':True})

        else:
            return JsonResponse({'validation':'please enter a valid ifsc_code','status':False})

    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_all_bank_details(request):
    response = []

    try:
        bank_obj = Bankprofile.objects.all()
        for bank in bank_obj:
            response.append({ 
                "bank_id":bank.id,
                "state":bank.state,
                "bank_name":bank.bank_name,
                "ifsc_code":bank.ifsc_code,
                "branch":bank.branch,
                "address":bank.address,
                "contact":bank.contact,
                "city":bank.city,
                "district":bank.district
            })
        return JsonResponse({'validation':'success','response':response,'status':True})

    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def terminate_bank(request):
    params = json.loads(request.body)

    bank_id = params.get('bank_id')

    if valid_integer(bank_id):return JsonResponse({'validation':'enter valid bank_id,must be integer'})   

    try:
        obj = Bankprofile.objects.get(id=bank_id).delete()
        return JsonResponse({'validation':'success','response':'terminate this branch','status':True})

    except Exception as e:
        return JsonResponse({'validation':str(e),'status':False})
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



