from django.urls import path
from .import  views 
urlpatterns = [
    path('',views.home,name='home'),
    path('dcme', views.dcme,name= 'dcme'),
    path('deee', views.deee,name= 'deee'),
    path('dce', views.dce,name= 'dce'),
    path('dmec', views.dmec,name= 'dmec'),
    path('ccp', views.ccp,name= 'ccp'),
    # adiminstration
    path('ccp_fac', views.ccp_fac,name= 'ccp_fac'),
    path('dcme_fac', views.dcme_fac,name= 'dcme_fac'),
    path('dme_fac', views.dme_fac,name= 'dme_fac'),
    path('dce_fac', views.dce_fac,name= 'dce_fac'),
    path('deee_fac', views.deee_fac,name= 'deee_fac')
]