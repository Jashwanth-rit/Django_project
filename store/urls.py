

from django.urls import path
from . import views



urlpatterns = [
   path('',views.home,name='home'),
   path('login',views.login_user,name='login'),
    path('regist',views.regist_user,name='regist'),
    path('logout',views.logout_user,name='logout'),
     path('product/<int:id>',views.product_details,name='product'),
  
     
]
