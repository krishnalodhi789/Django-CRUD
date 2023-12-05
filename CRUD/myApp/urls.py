from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('allRecords',views.allRecords, name='allRecords'),
    path('insertRecord',views.insertRecord, name='insertRecord'),
    path('deleteRecord/<int:id>',views.deleteRecord, name='deleteRecord'),
    path('editRecord/<int:id>',views.editRecord, name='editRecord'),

    path('uploadImage',views.uploadImage, name='uploadImage'),    
    path('gallary',views.gallary, name='gallary'),

    path('profileCreate',views.profileCreate, name='profileCreate'),
    path('profileCollection',views.profileCollection, name='profileCollection'),
    path('deleteProfile/<int:id>',views.deleteProfile, name='deleteProfile'),
    path('updateProfile/<int:id>',views.updateProfile, name='updateProfile'),
]