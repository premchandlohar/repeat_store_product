from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model



# Create your models here.
class Store(models.Model):
    storename = models.CharField(max_length=30)
    storelocation = models.CharField(max_length=30)
    storeaddress = models.CharField(max_length=50)
    storelatitude = models.DecimalField(max_digits=10,decimal_places=3)
    storelongitude = models.DecimalField(max_digits=10,decimal_places=3)
    storecity = models.CharField(max_length=25)
    storestate = models.CharField(max_length=25)
    createdon = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    storeimage = models.ImageField(upload_to ='uploads/%Y/%m/%d/',null = True,blank= True)

    def __str__(self):
        return self.storename

    # def get_json(self):
    #     return {
    #         'store_id':self.id,
    #         'store_name':self.store_name,
    #         'store_location':self.store_location,
    #         'store_address':self.store_address,
    #         'store_latitude':self.store_latitude,
    #         'store_longitude':self.store_longitude,
    #         'store_city':self.store_city,
    #         'store_state':self.store_state,
    #         'store_image':str(self.store_image),
    #         'created_on':str(self.created_on),
        
    # *******************************************************************************************

class Category(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    categoryname = models.CharField(max_length=30)
    categoryimage = models.ImageField(upload_to = 'uploads',null = True)
    createdon = models.DateTimeField(auto_now_add=True,null=True,blank=True)


    def __str__(self):
        return self.categoryname

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    # def get_json(self):
    #     return {
    #         'store_id':self.store.id,
    #         'store_name':self.store.store_name,
    #         'category_id':self.id,
    #         'category_name':self.category_name,
    #         'category_image':str(self.category_image),
    #         'created_on':str(self.created_on),
    #     }


    # def get_all_category(self):
    #     return {
    #         'store_name':self.store.store_name,
    #         'category_id':self.id,
    #         'category_name':self.category_name,
    #         'category_image':str(self.category_image),
    #         'created_on':str(self.created_on),
    #     }

    # def get_category(self):
    #     return {
    #             'store_id':self.store.id,
    #             'store_name':self.store.store_name,
    #             'category_id':self.id,
    #             'category_name':self.category_name,
    #             'created_on':str(self.created_on),
    #         }

    # *******************************************************************************************************
class Subcategory(models.Model):
    store  = models.ForeignKey(Store, on_delete=models.CASCADE)
    category  = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategoryname  = models.CharField(max_length=30)
    subcategoryimage  = models.ImageField(upload_to = 'uploads',null = True) 
    createdon = models.DateTimeField(auto_now_add=True,null=True,blank=True)


    def __str__(self):
        return self.subcategoryname

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"

    # def get_json(self):
    #     return {
    #         'store_id': self.store.id,
    #         'store_name': self.store.store_name,
    #         'category_id':self.category.id,
    #         'category_name': self.category.category_name,
    #         'subcategory_id': self.id,
    #         'subcategory_name': self.subcategory_name,
    #         'subcategory_image': str(self.subcategory_image),
    #         'created_on':str(self.created_on),
    #     }


    # def get_all_subcategory(self):
    #     return {
    #             'store_name':self.store.store_name,
    #             'category_name':self.category.category_name,
    #             'subcategory_id':self.id,
    #             'subcategory_name':self.subcategory_name,
    #             'subcategory_image': str(self.subcategory_image),
    #             'created_on':str(self.created_on),
    #         }

    
    # def get_subcategory(self):
    #     return {
    #             'category_id':self.category.id,
    #             'category_name':self.category.category_name,
    #             'subcategory_id':self.id,
    #             'subcategory_name':self.subcategory_name,
    #             'created_on':str(self.created_on),
    #         }

        # *********************************************************************************************
class Product(models.Model):
    store   = models.ForeignKey(Store, on_delete=models.CASCADE)
    subcategory  = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    productname  = models.CharField(max_length=30)
    productquantity  = models.IntegerField()
    productprice  = models.FloatField()
    productdiscountprice = models.FloatField()
    productdescription  = models.TextField(max_length=801)
    productimage  = models.ImageField(upload_to = 'uploads',null = True,blank= True)
    createdon = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    
    def __str__(self):
        return self.productname
 
    #    class instance method 

    # def get_json(self):
    #     return {
    #         'store_id': self.store.id,
    #         'store_name': self.store.store_name,                              
    #         'subcategory_id': self.subcategory.id,
    #         'subcategory_name':self.subcategory.subcategory_name,
    #         'product_id': self.id,
    #         'product_name' : self.product_name,     
    #         'product_quantity' : self.product_quantity,
    #         'product_price' : self.product_price,       
    #         'product_discount_price' : self.product_discount_price,
    #         'product_description' : self.product_description,
    #         'product_image':str(self.product_image),
    #         'created_on':str(self.created_on),
    #     }

    # def get_all_product(self):
    #     return {
    #         'store_name': self.store.store_name,
    #         'product_id': self.id,
    #         'product_name' : self.product_name,     
    #         'product_price' : self.product_price,
    #         'product_image' : str(self.product_image),
    #         'created_on':str(self.created_on),
    #     }
        # *****************************************************************************************


class Userprofile(models.Model):

    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(max_length=255,unique=False)
    createdon = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    # following= models.ManyToManyField(Store, through = 'Followership',related_name='following',
    # blank =True)

    def __str__(self):
        return self.firstname + " " + self.lastname

    # def get_json(self):
    #     return {
    #         "username": self.user.username,
    #         "first_name" : self.first_name,
    #         "last_name" : self.last_name,
    #         "age" : self.age,
    #         "email" : self.email,
    #         "created_on" :self.created_on
    #     }

    # def all_user(self):
    #     return {
    #         "user_id" : self.id,
    #         "username": self.user.username,
    #         "first_name" : self.first_name,
    #         "last_name" : self.last_name,
    #         "age" : self.age,
    #         "email" : self.email,
    #         "created_on" :self.created_on
    #     }

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Address(models.Model):
    userprofile = models.ForeignKey(Userprofile,on_delete=models.CASCADE,related_name='addresses')
    buildingname =  models.CharField(max_length=30)
    streetname =  models.CharField(max_length=30)
    locality =  models.CharField(max_length=30)
    city =  models.CharField(max_length=30)
    district =  models.CharField(max_length=30)
    state =  models.CharField(max_length=30)
    pincode =  models.DecimalField(max_digits = 10,decimal_places = 4)

    def __str__(self):
        return self.userprofile.firstname +" "+ self.userprofile.lastname

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    # def get_json(self):
    #     return {
    #         "user_id" : self.userprofile.id,
    #         "first_name" : self.userprofile.first_name,
    #         "last_name" : self.userprofile.last_name,
    #         "building_name" : self.building_name,
    #         "street_name" : self.street_name,
    #         "locality" : self.locality,
    #         "city" : self.city,
    #         "district" : self.district,
    #         "state" : self.state,
    #         "pincode" : self.pincode
    #     }

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Followership(models.Model):  
    REASONCHOICES = (
        (1,'not intrested'),
        (2,'high price'),
        (3,'not liked'),
        (4,'other')
    )
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE,null=True,blank=True)
    reason = models.IntegerField( choices=REASONCHOICES,null=True,blank=True)
    
     
    # def get_json(self):
    #     if self.user==None:
    #         return {
    #             "store_name" : self.store.store_name
    #             # 'first_name':self.user.first_name,
    #         }
    #     else:
    #         return {
    #             "follower" : self.user.first_name
    #         }
               
    def getjson(self):
        if self.user == None:
            return self.store.storename+': unfollow'
        else:
            return self.store.storename + ': '  +self.user.firstname
             
             
             
    def __str__(self):
        if self.user == None:
            return self.store.storename
        else:
            return self.user.firstname + ' ' + self.store.storename
        
    # ***********************************************************************************************



    