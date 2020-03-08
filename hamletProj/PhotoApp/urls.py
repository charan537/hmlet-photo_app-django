from django.urls import path
from PhotoApp import views
from django.conf.urls import url
from django.urls import re_path

urlpatterns = [    
    path('photo/myDrafts/', views.PhotoMyDraftsView.as_view(), name='photo_mydrafts'),
    path('photo/myPhotos/', views.PhotoMyListView.as_view(), name='photo_mylist'),
    path('photo/create/', views.PhotoCreate.as_view(), name='photo_create'),
    path('photo/<int:pk>/update/', views.PhotoUpdate.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', views.PhotoDelete.as_view(), name='photo_delete'),
    url(r'photo/search/$', views.FilteredPhotoListView.as_view(), name='photo_search'),
    re_path(r'^$', views.index, name='index')
]
