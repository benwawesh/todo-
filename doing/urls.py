from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('todonext', views.what_todo,name='todonext'),
    path('complete/<id>', views.completeTodo, name='complete'),
    path('deletecompleted', views.deletecompleted, name='deletecompleted'),
    path('deleteall', views.deleteall, name='deleteall'),
    path('delete/<id>', views.delete, name='delete'),
    path('edit/<id>', views.editing, name='edit'),
    path('update<id>',views.update, name='update')
]