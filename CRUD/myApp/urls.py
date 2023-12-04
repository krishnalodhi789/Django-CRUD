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
]