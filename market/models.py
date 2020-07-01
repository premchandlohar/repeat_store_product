from django.db import models
from datetime import datetime
from customer.models import Userprofile
# from market.models import Userprofile



# Create your models here.
class Store(models.Model):
    store_name = models.CharField(max_length=30)
    store_location = models.CharField(max_length=30)
    store_address = models.CharField(max_length=50)
    store_latitude = models.DecimalField(max_digits=10,decimal_places=3)
    store_longitude = models.DecimalField(max_digits=10,decimal_places=3)
    store_city = models.CharField(max_length=25)
    store_state = models.CharField(max_length=25)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_on = models.DateTimeField(auto_now=True,null=True,blank=True)
    store_image = models.ImageField(upload_to ='uploads/%Y/%m/%d/',null = True,blank= True)
    # follower = models.ManyToManyField(Userprofile, through = 'Followership',related_name='followers')

    def __str__(self):
        return self.store_name

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
    category_name = models.CharField(max_length=30)
    category_image = models.ImageField(upload_to = 'uploads',null = True)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_on = models.DateTimeField(auto_now=True,null=True,blank=True)


    def __str__(self):
        return self.category_name

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
    subcategory_name  = models.CharField(max_length=30)
    subcategory_image  = models.ImageField(upload_to = 'uploads',null = True) 
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_on = models.DateTimeField(auto_now=True,null=True,blank=True)


    def __str__(self):
        return self.subcategory_name

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
    store   = models.ForeignKey(Store, on_delete=models.CASCADE,related_name='products')
    subcategory  = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    product_name  = models.CharField(max_length=30)
    product_quantity  = models.IntegerField()
    product_price  = models.FloatField()
    product_discount_price = models.FloatField()
    product_description  = models.TextField(max_length=801)
    product_image  = models.ImageField(upload_to = 'uploads',null = True,blank= True)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_on = models.DateTimeField(auto_now=True,null=True,blank=True)
  
    def __str__(self):
        return self.product_name
 
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
class Followership(models.Model):  
    REASONCHOICES = (
        (1,'not intrested'),
        (2,'high price'),
        (3,'not liked'),
        (4,'other')
    )
    store = models.ForeignKey(Store, on_delete=models.CASCADE,related_name='follower')
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE,null=True,blank=True,related_name='following')
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
            return self.store.store_name+': unfollow'
        else:
            return self.store.store_name + ': '  +self.user.first_name
                       
    def __str__(self):
        if self.user == None:
            return self.store.store_name+'- unfollow'
        else:
            return self.store.store_name+ ' ' 'followers'+'-'+self.user.first_name
            # return self.user.first_name + ' '+ self.store.store_name      
    # ***********************************************************************************************



    