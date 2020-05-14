import re

def validstring(string):return(True if type(string)!=str or string=='' or string==None else False) 

def validfloat(float_data):return( True if not isinstance(float_data,float) or (float_data=='') or (float_data==None) else False )

def validinteger(integer):return (True if (type(integer) != int) or (integer ==None) or (integer=='')  else False )      
    
def validpincode(integer):return( True if (type(integer) != int) or len(str(integer)) !=6 or (integer==None) else False )

def validemail(email):
   return(True if email==None or not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
   , email) or email=='' else False)

def validimage (image): return (True if not (str(image).endswith(('.jpeg','.jpg','.png','.webp')))else False)

def validmobilenumber(mobileno):return(True if type(mobileno)!=str or mobileno=='' or mobileno==None or len(mobileno)!=10 else False)