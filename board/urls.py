from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path("addboard/", views.addboard, name="addboard"),
    path("editboard/<int:id>/", views.editboard, name="editboard"),
    path("deleteboard/<int:id>/", views.deleteboard, name="deleteboard"),
]