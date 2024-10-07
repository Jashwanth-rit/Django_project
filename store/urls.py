from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # The home view that handles search
    path('login', views.login_user, name='login'),
    path('regist', views.regist_user, name='regist'),
    path('logout', views.logout_user, name='logout'),
    path('product/<int:id>', views.product_details, name='product'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('user_info', views.user_info, name='user_info'),
    path('password/', views.update_password, name='update_password'),
]
