from numpy import delete
from books import views



from. import views
from django.contrib.auth import views as auth_views
from django.conf import settings

from numpy import delete
from books import views
from django.urls import path


from django.contrib.auth import views as auth_views
from users.views import home
from numpy import delete
from books import views
from django.urls import path
from . import views

urlpatterns = [
    path('', home, name='users-home'),
    path('store/', views.store, name='users-store'),
    path('prod_detail/',views.viewbook, name='users-prod_detail'),
  
   
    
    
]