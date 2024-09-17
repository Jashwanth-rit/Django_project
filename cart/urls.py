

from django.urls import path
from . import views



urlpatterns = [
  
     path('',views.cart_get,name='cart_get'),
      path('add/',views.cart_add,name='cart_add'),
       path('update/',views.cart_update,name='cart_update'),
        path('delete/',views.cart_delete,name='cart_delete'),
     
]
