import re

def valid_string(string):return(True if type(string)!=str or string=='' or string==None else False) 

def valid_float(float_data):return( True if not isinstance(float_data,float) or (float_data=='') or (float_data==None) else False )

def valid_integer(integer):return (True if (type(integer) != int) or (integer ==None) or (integer=='')  else False )      
    
def valid_pincode(integer):return( True if (type(integer) != int) or len(str(integer)) !=6 or (integer==None) else False )

def valid_email(email):
   return(True if email==None or not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
   , email) or email=='' else False)

def valid_image (image): return (True if not (str(image).endswith(('.jpeg','.jpg','.png','.webp')))else False)

def valid_mobile_number(mobile_no):return(True if type(mobile_no)!=str or mobile_no=='' or mobile_no==None or len(mobile_no)!=10 else False)

def valid_ifsc_code(ifsc_code):return(True if type(ifsc_code)!=str or ifsc_code=='' or ifsc_code==None or len(ifsc_code)!=11 else False)
