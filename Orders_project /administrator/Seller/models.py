from django.db import models



# 分类表
'''
class Types(models.Model):
    label = models.CharField(max_length=32)  # 分类名称 例如 水果类，水产类
    parent_id = models.IntegerField()  # 父id
    description = models.TextField()  # 分类描述，对类型的一个描述。
'''

# 用户
class Seller(models.Model):
    username = models.CharField(max_length=32)  # 用户名
    password = models.CharField(max_length=32)  # 密码
    nickname = models.CharField(max_length=32)  # 昵称
    #photo = models.ImageField(upload_to='image')  # 卖家图片
    phone = models.CharField(max_length=32)  # 电话
    #address = models.CharField(max_length=32)  # 地址
    email = models.EmailField()  # 邮箱
    #id_number = models.CharField(max_length=32)  # 身份证


from ckeditor_uploader.fields import RichTextUploadingField


# 订单类
class Orders(models.Model):
    #goods_id = models.CharField(max_length=32)  
    orders_username = models.CharField(max_length=32) #下单用户名
    orders_address = models.CharField(max_length=32) # 设计订单地址
    #goods_price = models.FloatField()  # 原价
    #goods_now_price = models.FloatField()  # 现价
    orders_phone = models.CharField(max_length=32)  # 用户手机号码
    orders_email = models.EmailField() #用户邮箱
    orders_content = models.TextField()  # 简单描述
    #orders_content = RichTextUploadingField()   使用富文本字段
    orders_time = models.DateTimeField()  # 下单时间
    orders_designer_bool = models.IntegerField() #设计师是否接单
    orders_designer_name = models.CharField(max_length=32) #设计师名字
    orders_agreement = models.FileField(upload_to='agreement') #合作协议
    orders_test_time = models.CharField(max_length=108) #用户预约测量时间
    orders_scheme = models.FileField(upload_to='scheme') #设计方案
    orders_prices = models.FloatField() #报价
    orders_finish_bool = models.IntegerField() #订单是否完成
    orders_seller = models.ForeignKey(Seller, on_delete=True)  # 一个用户对应多个订单
    #orders_seller_id = models.IntegerField() #下单用户的id

# Create your models here.
