from django.urls import path
from.import views
urlpatterns=[
    path('',views.homemenu,name='myhome'),
    
    path('login/',views.registermenu,name='myregister'),
    path('contact/',views.contactmenu,name='mycontact'),
    path('login1/',views.login1menu,name='mylogin1'),
    path('logout/',views.logoutmenu,name='logoutURL'),
    
]
