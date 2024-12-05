from django.urls import path
from . import views
from .views import home,index,news,events,member_create,member_list,member_update,member_delete,gallery,upload_image,news_list,news_detail,upload_news,edit_news,delete_news,export_csv,export_excel,export_pdf
urlpatterns = [
    path('home',home,name='home'),
    path('',index,name='index'),
    path('news',news,name='news'),
    path('events',events,name='events'),
    path('member_create',member_create,name='member_create'),
    path('member_list',member_list,name='member_list'),
    path('member_update/<int:pk>',member_update,name='member_update'),
    path('member_delete/<int:pk>',member_delete,name='member_delete'),
    path('gallery',gallery,name='gallery'),
    path('upload',upload_image,name='upload'),
    path('news/', news_list, name='news'),
    path('news/<int:pk>/',news_detail, name='news_detail'),
    path('news/upload/',upload_news, name='upload_news'),
    path('news/edit/<int:pk>/', edit_news, name='edit_news'),
    path('news/delete/<int:pk>/', delete_news, name='delete_news'),
    path('sermons/', views.sermon_list, name='sermon_list'),
    path('sermons/add/', views.add_sermon, name='add_sermon'),
    path('sermons/<int:sermon_id>/edit/', views.edit_sermon, name='edit_sermon'),
    path('sermons/<int:sermon_id>/delete/', views.delete_sermon, name='delete_sermon'),
    path('export_csv',export_csv, name='export-csv'),
    path('export_excel',export_excel, name='export-excel'),
    path('export_pdf',export_pdf,name='export-pdf'),


]