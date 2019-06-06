from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('gettypes/', views.gettypes, name='types'),
    path('getresource/', views.getresource, name='products'),
    path('resourcedetails/<int:id>', views.resourcedetails, name='resourcedetails'),
    path('newProduct/', views.newProduct, name='newproduct'),
]