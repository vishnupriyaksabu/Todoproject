
from django.urls import path
from . import views

urlpatterns = [
   
      path('', views.add,name='add'),
      # path('details/', views.details,name='details'),
      path('delete/<int:task_id>/', views.delete,name='delete'),
      path('update/<int:task_id>/', views.update,name='update'),
      path('cbvhome/', views.Todoclassviewlist.as_view(),name='cbvhome'),
      path('cbvdetail/<int:pk>/', views.Todoclassviewdetail.as_view(),name='cbvdetail'),
      path('cbvupdate/<int:pk>/', views.Todoclassviewupdate.as_view(),name='cbvupdate'),
      path('cbvdelete/<int:pk>/', views.Todoclassviewdelete.as_view(),name='cbvdelete'),
]