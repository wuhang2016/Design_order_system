from __future__ import unicode_literals

from django.contrib import admin

# Seller/admin.py:
from Seller.models import Orders,Seller
 



# app01/admin.py:
class OrdersAdmin(admin.ModelAdmin):
    # 指定后台网页要显示的字段
    list_display = ["id", 
                    'orders_username',
                    'orders_address' ,
                    'orders_phone', 
                    'orders_email',
                    'orders_content', 
                    'orders_time', 
                    'orders_designer_bool',
                    'orders_designer_name', 
                    'orders_agreement', 
                    'orders_test_time',
                    'orders_scheme',
                    'orders_prices', 
                    'orders_finish_bool',
                    'orders_seller',
                   ]
 
 
class SellerAdmin(admin.ModelAdmin):
    # 指定后台网页要显示的字段
    list_display = ["id", "username","phone","email"]

# 注册Model类
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Seller, SellerAdmin)






# Register your models here.
