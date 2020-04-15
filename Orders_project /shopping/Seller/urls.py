app_name= 'Seller'
from django.urls import path
from Seller import views
from django.conf.urls import *
from django.views.decorators.csrf import csrf_exempt



urlpatterns=[
    path('index/',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('sign-up/', csrf_exempt(views.sign_up), name="sign-up"),
    #path('sign-up/',views.sign_up,name="sign-up"),
    path('register/',views.register,name="register"),
    path('single/',views.single,name="single"),
    path('logout/',views.logout,name="logout"),
    path('orders_add/',views.orders_add,name="orders_add"),
    #path('goods_list/',views.goods_list,name="goods_list"),
    #path('goods_change/',views.goods_change,name="goods_change"),
    #path('goods_delete/',views.goods_delete,name="goods_delete"),
    path('about/',views.about,name="about"),
    path('services/',views.services,name="services"),
    path('mail/',views.mail,name="mail"),
    path('single_order_get/',views.single_order_get,name="single_order_get"),
    path('single_order_manage/',views.single_order_manage,name="single_order_manage"),
    path('orders_add/',views.orders_add,name="orders_add"),
    path('orders_list/',views.orders_list,name="orders_list"),
    path(r'orders_change/<pk>',views.orders_change,name='orders_change' ),
    path(r'orders_delete/<pk>',views.orders_delete,name='orders_delete' ),
    path(r'orders_test_time/<pk>',views.orders_test_time,name='views.orders_test_time' ),
]
