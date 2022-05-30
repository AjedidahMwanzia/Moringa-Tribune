
from django.urls import re_path as url
from . import views
# from django.conf.urls import url,include

urlpatterns = [
  url(r'^login_user/',views.login_user,name = 'login'),
  
   
]