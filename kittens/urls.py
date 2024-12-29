from django.urls import path
from . import views

app_name='kittens'
urlpatterns = [
    path('', views.index, name='index'),
    path('show/<int:pk>/', views.show, name='show'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.destroy, name='destroy')
]