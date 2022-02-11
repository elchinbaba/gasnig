from django.urls import path
from .views import *

app_name = 'gallery'

urlpatterns = [
    path('', gallery, name='gallery'),
    path('drawing/', drawing, name='drawing'),
    path('design/', design, name='design'),
    path('create/', create, name='create'),
    path('<int:id>/', detail, name='detail'),
    path('<int:id>/delete/', delete, name='delete'),
]