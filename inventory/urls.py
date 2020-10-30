from django.urls import path
from .views import *

urlpatterns = [
    path('all/', list_objects),
    path('view/<str:slug>/', single_object),
    path('create/', create),
    path('update/<str:slug>/', update),
    path('delete/<str:slug>/', delete)
]
